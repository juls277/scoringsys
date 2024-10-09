# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /scoringsys

# Install system dependencies
RUN apt-get update \
    && apt-get install -y gcc libpq-dev

# Install Python dependencies
COPY requirements.txt /scoringsys/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copy project
COPY . /scoringsys/

# Run migrations and collect static files
RUN python manage.py migrate --noinput
RUN python manage.py collectstatic --noinput

# Expose the port the app will run on
EXPOSE 8000

# Command to run the application using Daphne ASGI server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "scoringsys.asgi:application"]