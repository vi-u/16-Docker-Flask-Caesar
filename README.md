# 16-Docker-Flask-Caesar
>>>>  Composing Caesar Cipher Flask App into Docker with uWSGI ang Ngix server

#So, first let's create ywo more template files: form.html for input , and data.html for encrypted message output

    sudo nano app/templates/form.html

#which contains


    <form action="/data" method = "POST">
        <p>Please enter Phrase to Encript: <input type = "text" name = "Phrase" /></p>
        <p>Please choose your Step: <input type = "text" name = "Step" /></p>

        <p><input type = "submit" value = "Submit" /></p>
    </form>

#

    sudo nano app/templates/data.html
    
#which contains

    <p> ... </p>
    <p> Encoded message:  </p> <h2> {{result}} </h2>
    <p> ... </p>

#Next, modify app/views.py file so that input /form are encripted and have output to /data


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

    16-Docker-Flask-Caesar

#then we have to change our PATH in 

    Dockerfile

#wich will contain

    FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
    RUN apk --update add bash nano
    ENV STATIC_URL /static
    ENV STATIC_PATH /home/vit/Desktop/16-Docker-Flask-Caesar/app/static
    COPY ./requirements.txt /home/vit/Desktop/16-Docker-Flask-Caesar/requirements.txt
    RUN pip install -r /home/vit/Desktop/16-Docker-Flask-Caesar/requirements.txt
        
#as well as we need to change the name of our app to "docker.test15"

    start.sh

#which contains

    #!/bin/bash
    app="docker.test16"
    docker build -t ${app} .
    docker run -d -p 56733:80 \
      --name=${app} \
      -v $PWD:/app ${app}

#and finally, to create and start new container "docker.test15"

    cd ..
    cd 16-Docker-Flask-Template

#
    sudo bash start.sh
    
#to verify that docker is running

    sudo docker ps
    
#if nor running, start it

    sudo start docker.test16

***

#To verify visit browser page 

    localhost:56733/form



****

#If we were developed our app withing the same local directory, we would have just stop and restart the Docker containers

    sudo docker stop docker.test16 && sudo docker start docker.test16

