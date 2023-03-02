# import the docker registry import python image
FROM python:3.10-slim-buster

# create a folder named backend-flask at the root of our container (the container has a Linux OS -> guess OS)
# that folder will be our working directory
WORKDIR /backend-flask

 # copy the requirements.txt in the host OS to the working directory of the guess Os in the container
COPY requirements.txt requirements.txt

# inside the container -> install the python library used for the app
RUN pip3 install -r requirements.txt

 # copy everything from the current directory in the host OS to the  working directory in the container  guess OS
 # first period . -> /backend-flask in the host Os
 # second period  . -> /backend-flask in container OS
COPY . .

# set an environement variable inside the container -> will remain set when the container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# CMD = command = command that will be run inside the container
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]