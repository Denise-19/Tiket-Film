# set base image (host OS)
FROM python:3.8

# set the working directory in the container
WORKDIR /flask

# copy the content of the local src directory to the working directory
COPY . /flask

# install dependencies
RUN pip install -r requirements.txt


# command to run on container start
CMD [ "python", "app.py" ]