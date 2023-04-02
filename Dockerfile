#The first instruction is what image we want to base our container on
#use an official python runtime as a parent image
FROM python:3.11.2-bullseye

#The environment variable below ensures that the python output is set straight
#to the terminal without buffering it first.
ENV PYTHONBUFFERED 1

#create a root directory for our project to sit in the container
RUN mkdir /todo_django

#set the working directory to /todo_django

WORKDIR /todo_django

#copy the current directory contents into the container at /todo_django

ADD . /todo_django/

#install any needed dependencies or packages from requirements.txt
RUN pip install -r requirements.txt


