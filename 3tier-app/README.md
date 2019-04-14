# 3 tier app example in docker

This repo is a example 3-tiered application that runs as a set of Docker 
containers. The application is built using nginx as a reverse proxy to handle 
client requests, a Python based Flask app to process requests, and a MongoDB 
database for persistence. As illustrated below, each component runs as its own 
Docker container.

The public net includes the Web and the app, The Database is only available in
the private net, where the app also has a link. So, the public net is only 
because we won't open the path to the app (port) through the private net.

Instructions for building these images from included docker-compose file are below.

<pre>
              public net                    private net
             +---------------------------------+ 
             |                   +-------------+---------------------+
          80 | +---------+  5000 | +---------+ | 27017   +---------+ |
(Client) ----> |  nginx  | ------> |  app    | --------> | MongoDB | |
             | +---------+       | +---------+ |         +---------+ |
             |                   +-------------+---------------------+
             +---------------------------------+
</pre>



## build the images

    docker-compose build -no-cache --force-rm --pull
    
## run the containers

    docker-compose up

This will block until all containers are exited. To exit the container use

CTRL-C

To daemonize the docker-compose, use the "-d" param.

## destroy the container

    docker-compose down -v

## check if it works

.NOTE: for this thest it is better to run the container in non-damon way.

To check if all works fine, run the containers and check the website

0.0.0.0:80/app

If you see the app output and a counter. Reloading the site will increase the 
counter by 1.

If you stop all container and re-run it the counter remember the last counter.

To reset the counter, remove the database container (after stopping it). This 
can be done by running

    docker rm -f db
    
in a terminal.
