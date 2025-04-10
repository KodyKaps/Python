# Use an official Python image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your app
COPY . .

# Run the CLI app when the container starts
# Replace 'cli_app.py' with your actual entrypoint script
# CMD ["python", "cli_app.py"]