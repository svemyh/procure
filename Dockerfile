# Use an official Python runtime as a base image
FROM python:3.11-slim

RUN mkdir /app
# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

COPY .env /app/
COPY . /app/

# Expose the port on which the Django app will run (default is 8000)
EXPOSE 8000

# NB is generally good practice but this will take a significant amount of time
# RUN python manage.py collectstatic --noinput

# RUN python3 manage.py migrate

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]

# gunicorn --bind 0.0.0.0:8000 myproject.wsgi:application
