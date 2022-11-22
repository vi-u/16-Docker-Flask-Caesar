FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /home/vit/Desktop/16-Docker-Flask-Caesar/app/static
COPY ./requirements.txt /home/vit/Desktop/16-Docker-Flask-Caesar/requirements.txt
RUN pip install -r /home/vit/Desktop/16-Docker-Flask-Caesar/requirements.txt
