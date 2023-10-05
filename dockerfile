# Use the official Python image as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY requirements.txt .

RUN pip install --upgrade pip
# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose port 8000 for the FastAPI application to listen on
EXPOSE 8000

# Command to run your FastAPI application
CMD ["uvicorn", "test:app", "--host", "0.0.0.0", "--port", "8000"]
