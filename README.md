# docker-compose-experiment
An experiment with Docker Compose.  

This project will create a python webserver, which can be connected to at [http://localhost:8000].
The webserver holds an api which can increment the count in the redis database by one, and return the number in the database.  
The index page will show how many times the button has been clicked (which calls the api through an XHR).

Using my base-alpine docker image, and the official redis image.
