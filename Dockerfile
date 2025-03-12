# Use Python 3.12 as base image
FROM python:3.12

# Set working directory inside the container
WORKDIR /app

# Copy all project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development 
ENV DEBUG=True

# Expose port 8080
EXPOSE 8080

# Run the application
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]
