# API-3tier-app

## Reqirements

* docker-compose 

testet with version:

    docker-compose version 1.23.2, build 1110ad0
    docker-py version: 3.7.0
    CPython version: 3.6.5
    OpenSSL version: OpenSSL 1.1.0g  2 Nov 2017

* docker

tested with version

    Client:
     Version:           18.09.3
     API version:       1.39
     Go version:        go1.10.8
     Git commit:        774a1f4
     Built:             Thu Feb 28 06:53:11 2019
     OS/Arch:           linux/amd64
     Experimental:      false
    
    Server: Docker Engine - Community
     Engine:
      Version:          18.09.3
      API version:      1.39 (minimum version 1.12)
      Go version:       go1.10.8
      Git commit:       774a1f4
      Built:            Thu Feb 28 05:59:55 2019
      OS/Arch:          linux/amd64
      Experimental:     false


### update the submodules

    git submodules update --init
    

## USAGE
### build the images

    bash fetch
    
### run the container

* blocking mode:


    docker-compose up 

    
* daemon mode:


    bash run

    
### destroy everything

    bash sink
    
## check

* API

Call in a webbrowser "localhost:<exposed port>/api/status"

* WEB

Call in a webbrowser "localhost:<exposed port>/"

To get the local ports check the

    docker-compose port web 80
    docker-compose port api 80
    
output


# TODO 

* find out how to use the WEB and the API apps
* find out what it should do