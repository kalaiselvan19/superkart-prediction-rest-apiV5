
# use a minimal python 3.9 image as the base

FROM python:3.9-slim;

#set the working directory in the container
WORKDIR /app

#Copy the requirements files and install dependencies
COPY . .

#Install dependencies from the requirements files without using cache to reduce image test_size
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#Expose the port on which the applications will run
EXPOSE 5000

#Command to run the applications using gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:7860", "app:app"]

