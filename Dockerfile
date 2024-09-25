# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Expose the port on which the Django app will run (default is 8000)
EXPOSE 8000

# Collect static files
RUN python manage.py collectstatic --noinput

# Run database migrations
RUN python manage.py migrate

# Start the Django app
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
