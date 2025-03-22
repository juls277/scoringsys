import asyncio
import pytest
from channels.testing import WebsocketCommunicator
from scoringsys.asgi import application


@pytest.mark.asyncio
@pytest.mark.django_db(transaction=True)
async def test_websocket_court_isolation_strict():
    # Players (senders)
    court1 = WebsocketCommunicator(application, "/wss/court/court1/")
    court2 = WebsocketCommunicator(application, "/wss/court/court2/")

    # Scoreboards (listeners)
    scoreboard1 = WebsocketCommunicator(application, "/wss/scoreboard/court1/")
    scoreboard2 = WebsocketCommunicator(application, "/wss/scoreboard/court2/")

    # Connect all
    assert (await court1.connect())[0]
    assert (await court2.connect())[0]
    assert (await scoreboard1.connect())[0]
    assert (await scoreboard2.connect())[0]

    # Receive initial state dumps
    await court1.receive_json_from()
    await court2.receive_json_from()

    # ⚠️ Send update from COURT 1
    await court1.send_json_to({
        "player1_name": "C1_Player",
        "player2_name": "C1_Opponent",
        "player1_score": 8,
        "player2_score": 11,
        "current_set": 1,
        "player1_set1": 0,
        "player2_set1": 0,
        "player1_set2": 0,
        "player2_set2": 0,
        "player1_set3": 0,
        "player2_set3": 0
    })
    await asyncio.sleep(0.1)  # Let async flow

    # ✅ Court1 should receive back its own message
    data = await court1.receive_json_from()
    assert data["player1_name"] == "C1_Player"

    # ✅ Scoreboard1 should also get the broadcast
    data = await scoreboard1.receive_json_from()
    assert data["player1_name"] == "C1_Player"

    # ❌ Scoreboard2 should NOT receive anything
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(scoreboard2.receive_json_from(), timeout=0.5)
    print("✅ Scoreboard2 stayed silent when Court1 sent data")

    # ⚠️ Now send update from COURT 2
    await court2.send_json_to({
        "player1_name": "C2_Player",
        "player2_name": "C2_Opponent",
        "player1_score": 15,
        "player2_score": 13,
        "current_set": 1,
        "player1_set1": 0,
        "player2_set1": 0,
        "player1_set2": 0,
        "player2_set2": 0,
        "player1_set3": 0,
        "player2_set3": 0
    })
    await asyncio.sleep(0.1)

    # ✅ Court2 should get its own message
    data = await court2.receive_json_from()
    assert data["player1_name"] == "C2_Player"

    # ✅ Scoreboard2 gets court2's update
    data = await scoreboard2.receive_json_from()
    assert data["player1_name"] == "C2_Player"

    # ❌ Scoreboard1 should NOT receive anything from Court2
    with pytest.raises(asyncio.TimeoutError):
        await asyncio.wait_for(scoreboard1.receive_json_from(), timeout=0.5)
    print("✅ Scoreboard1 stayed silent when Court2 sent data")

    # Clean up
    await court1.disconnect()
    await court2.disconnect()
    await scoreboard1.disconnect()
    await scoreboard2.disconnect()
