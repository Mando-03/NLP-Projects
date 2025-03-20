# Use Python 3.10 as the base image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose port 8000 for the Flask API
EXPOSE 8000

# Run the Flask API
CMD ["python", "app.py"]