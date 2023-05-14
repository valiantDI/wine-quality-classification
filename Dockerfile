# Install base Python image
FROM python:3.9-slim-buster

# Copy files to the container
COPY source/*.py /app/
COPY source/model.joblib /app/
COPY requirements.txt /app/

# Set working directory to previously added app directory
WORKDIR /app/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port uvicorn is running on
EXPOSE 80

# Run uvicorn server
CMD ["uvicorn", "server:app", "--reload", "--host", "0.0.0.0", "--port", "80"]