# Use an official Python runtime as a base image
FROM python:3.11-slim

# Enable logging
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy environment variables and application code
#COPY .env /app/
COPY . /app/

# Copy AWS credentials and config
COPY credentials /root/.aws/credentials
COPY config /root/.aws/config

# Install AWS CLI
RUN pip3 install awscli
RUN aws s3 ls

# Expose the port on which the Django app will run
EXPOSE 8080

# Set the entry point for the container
ENTRYPOINT ["python3", "manage.py", "runserver", "0.0.0.0:8080"]

# Optionally, you can uncomment these lines for production use
# CMD ["gunicorn", "--bind", "0.0.0.0:8080", "myproject.wsgi:application"]

# NB: It's generally good practice but may take significant time to run
# RUN python manage.py collectstatic --noinput
# RUN python3 manage.py migrate
