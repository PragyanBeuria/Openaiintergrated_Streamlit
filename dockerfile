# Use the official Python base image
FROM python:3.10

RUN pip install --upgrade pip
# Set the working directory in the container
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install the required dependencies

RUN pip install --no-cache-dir  -r requirements.txt

# Expose the port where the Streamlit app will run (if using a custom port, change 8501 to your desired port)
EXPOSE 8501

# Set the command to run the Streamlit app when the container starts
CMD ["streamlit", "run", "app.py"]
