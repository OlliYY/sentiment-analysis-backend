# Use Python 3.12 as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .

# Expose the application port (8080 as used in the Rahti deployment)
EXPOSE 8080

# Run the application using Waitress
CMD ["python", "app.py"]
