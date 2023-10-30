# Use the Python 3.8 base image
FROM python:3.8

# Set the working directory to /saufbot
WORKDIR /saufbot

# Copy the requirements file and install dependencies
COPY requirements.txt /saufbot/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python script and other necessary files
COPY saufbot.py /saufbot/
COPY 1_1.png /saufbot/
COPY 1_2.png /saufbot/
COPY 1_3.png /saufbot/
COPY 1_4.png /saufbot/
COPY 1_5.png /saufbot/
COPY 1_6.png /saufbot/
COPY 2_1.png /saufbot/
COPY 2_2.png /saufbot/
COPY 2_3.png /saufbot/
COPY 2_4.png /saufbot/
COPY 2_5.png /saufbot/
COPY 2_6.png /saufbot/
COPY 3_1.png /saufbot/
COPY 3_2.png /saufbot/
COPY 3_3.png /saufbot/
COPY 3_4.png /saufbot/
COPY 3_5.png /saufbot/
COPY 3_6.png /saufbot/

# Set environment variables and run your Python script
CMD ["python", "saufbot.py"]
