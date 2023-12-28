# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy your Python script(s) into the container at /app
COPY staff_record.py /app

# Install any needed dependencies specified in requirements.txt
# RUN pip install -r requirements.txt

# Define environment variable
# ENV VARIABLE_NAME=value

# Run your Python script when the container launches
CMD ["python", "./staff_record.py"]
