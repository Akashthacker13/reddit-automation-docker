FROM selenium/standalone-chrome:latest

USER root

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip

WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy bot script
COPY bot.py .

# Run bot
CMD ["python3", "bot.py"]
