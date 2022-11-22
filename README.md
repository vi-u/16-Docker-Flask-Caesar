# 16-Docker-Flask-Caesar
>>>>   Building Caesar Cipher Tool  in Docker using Flask, uWSGI, and Nginx

In this final tutorial we will build our final app comprising of Flask Caesar Cipher Tool which we built in 


This tool now built in Docker which can be depolyed in a variety of cloud based servers such as Amazon, Azure, Digital Ocean, etc.

>>> First, let's add input form to get text and step and output form to show encrypted message.

    sudo nano /app/templates/input.html

#which contains

    <form action="/output" method = "POST">
       <p>Please enter Phrase to Encript: <input type = "text" name = "Phrase" /></p>
       <p>Please choose your Step: <input type = "text" name = "Step" /></p>
   
       <p><input type = "submit" value = "Submit" /></p>
    </form>

#and output.html

    sudo nano /app/templates/output.html

#which contains

    <p> ... </p>
    <p> Encoded message:  </p> <h2> {{result}} </h2>
    <p> ... </p>

#

