# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable to tell Flask to run in container
ENV FLASK_RUN_HOST=0.0.0.0

# Run flask command to start the app
CMD ["python3", "app.py"]
