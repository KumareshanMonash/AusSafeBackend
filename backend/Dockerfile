# Use the official Python image
FROM python:3.10

# Set the working directory
WORKDIR /backend/app

# Copy project files
COPY . /backend/app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8080 (required by Cloud Run)
EXPOSE 8000

# Run FastAPI using Uvicorn
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "main:app", "--bind", "0.0.0.0:8000"]
