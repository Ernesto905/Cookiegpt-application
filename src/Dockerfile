# syntax=docker/dockerfile:1

# Will be using a python base image to run the flask application 
FROM python:3.7.17-slim-buster

WORKDIR /src

## Copy the contents of our requirements into our container
COPY requirements.txt requirements.txt


# Install the necessary dependancies 
RUN pip3 install --upgrade pip 
RUN pip3 install -r requirements.txt
COPY . .


# Set the environment variable to listen on all interfaces
ENV FLASK_RUN_HOST=0.0.0.0

# # Expose the port which the flask app will run on 
EXPOSE 5000
# Run the application 
CMD ["flask", "run"]

