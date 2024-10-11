# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set environment variables to disable buffered output and enable pip's new resolver
ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1

# Set the working directory in the container
WORKDIR /app

# Dependencies
RUN apt-get update && apt-get install -y gcc
COPY requirements.txt /app/requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /app/

# Expose port
EXPOSE 8080

RUN chmod +x /app/entrypoint.sh

# Set the entry point for the container
ENTRYPOINT ["/app/entrypoint.sh"]


# NB: It's generally good practice but may take significant time to run
# RUN python manage.py collectstatic --noinput
# RUN python3 manage.py migrate
