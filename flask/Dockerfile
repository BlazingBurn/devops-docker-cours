FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy requirements.txt to the image and install the required packages
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Install additional dependencies
RUN apt-get update -y && apt-get install -y python3 python3-pip

# Copy the app.py file and templates folder to the image
COPY templates /app/templates
COPY app.py /app

# Expose port 5000
EXPOSE 5000

# Start the application using CMD
CMD ["python3", "app.py"]
