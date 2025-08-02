# Use base Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy only the necessary files
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Optional: copy .env (only if safe)
# COPY .env .
# Copy the rest of the app
COPY . .

# Command to run
CMD ["python", "app.py"]
