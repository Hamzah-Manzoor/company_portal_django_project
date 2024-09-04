# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /company_portal_app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt /company_portal_app/

# Install any necessary dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /company_portal_app/

# Expose the port the app runs on
EXPOSE 8000

# Define the environment variable
ENV DJANGO_SETTINGS_MODULE=company_portal.settings

# Run the command to start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "company_portal.wsgi:application"]

## Collect static files during the build process, for production environment
#RUN python3 manage.py collectstatic --noinput

