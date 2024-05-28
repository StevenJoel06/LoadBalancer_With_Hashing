FROM python:3.11-slim

WORKDIR /app

# Copy the requirements.txt from the root directory
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . .


CMD ["python", "app.py"]