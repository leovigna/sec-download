# Use an official Python runtime as a parent image
FROM python:3.6.5-slim

ENV PYTHONUNBUFFERED 1

# Create the working directory /app
RUN mkdir /app

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
#--trusted-host pypi.python.org
RUN pip install -r requirements.txt

CMD ["python", "app.py"]