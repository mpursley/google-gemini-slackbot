# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the environment variable for the port
ENV PORT 8080

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code to the working directory
COPY . .

# Command to run the application using Gunicorn
# Gunicorn is a production-ready WSGI server.
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app
