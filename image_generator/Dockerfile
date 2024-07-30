# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pip and upgrade to the latest version
RUN pip install --upgrade pip

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=image_generator.settings

# Run the application
CMD ["gunicorn", "--workers", "3", "--bind", "0.0.0.0:8000", "image_generator.wsgi:application"]
