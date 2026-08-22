#use a miminal base image with python 3.9 installed
FROM python:3.9-slim

#set the working directory in the container
WORKDIR /app

#copy all files from the current directory on the host to the container's /app directory
COPY . .

#Install python dependencies listed in requirements.txt
RUN pip3 install -r requirements.txt

#Define the command to run the streamlit app on port
CMD  ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.enableXsrfprotection=false"]
