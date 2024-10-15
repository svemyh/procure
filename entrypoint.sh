#!/bin/bash
echo "Starting Django development server..."

# Create AWS credentials file dynamically using environment variables
mkdir -p /root/.aws
echo "[default]" > /root/.aws/credentials
echo "aws_access_key_id = ${AWS_ACCESS_KEY_ID}" >> /root/.aws/credentials
echo "aws_secret_access_key = ${AWS_SECRET_ACCESS_KEY}" >> /root/.aws/credentials

# AWS CLI can be configured via aws/config and aws/credentials (which is created dynamically in entrypoint.sh from env-vars)
aws s3 ls

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py runserver 0.0.0.0:8080
echo "Running."
