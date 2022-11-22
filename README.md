# 15-Docker-Flask-Template
>>>>  Adding Render Template to Flask App

Templates are files that display static and dynamic content to users who visit your application. 

#So, first let's create home.html

    sudo nano app/templates/home.html

#which contains


    <!doctype html>
    <html lang="en-us">   
      <head>
        <meta charset="utf-8">
        <meta http-equiv="x-ua-compatible" content="ie=edge">
        <title>Welcome home</title>
      </head>
  
      <body>
        <h1>Home Page</h1>
        <p>This is the home page of our application.</p>
      </body> 
    </html>

#Next, modify app/views.py file so that users are served the contents of the home.html file whenever they visit the /template route on your application.

    sudo nano app/views.py

#which contains

    from flask import render_template
    from app import app 

    @app.route('/')
    def home():
        return "Hello world!"

    @app.route('/template')
    def template():
        return render_template('home.html')
        
#As we created a new project in our local directory and named it 

    15-Docker-Flask-Template

#then we have to change our PATH in 

    Dockerfile

#wich will contain

    FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
    RUN apk --update add bash nano
    ENV STATIC_URL /static
    ENV STATIC_PATH /home/vit/Desktop/15-Docker-Flask-Template/app/static
    COPY ./requirements.txt /home/vit/Desktop/15-Docker-Flask-Template/requirements.txt
    RUN pip install -r /home/vit/Desktop/15-Docker-Flask-Template/requirements.txt
        
#as well as we need to change the name of our app to "docker.test15"

    start.sh

#which contains

    #!/bin/bash
    app="docker.test15"
    docker build -t ${app} .
    docker run -d -p 56733:80 \
      --name=${app} \
      -v $PWD:/app ${app}

#and finally, to create and start new container "docker.test15"

    cd 15-Docker-Flask-Template

#
    sudo bash start.sh
    
#to verify that docker is running

    sudo docker ps
    
#if nor running, start it

    sudo start docker.test15

***

#To verify visit browser page 

    localhost:56733/template



****

#If we were developed our app withing the same local directory, we would have just stop and restart the Docker containers

    sudo docker stop docker.test && sudo docker start docker.test

