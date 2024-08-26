# Dockerizer Django App
Hi everyone! :wave:

Welcome to this dockerization of django repo. :boom:
### Motivation
This is the way to dockerize a django app. :star_struck:

This repo includes the Dokcerfile which is used to create a docker image of this app. :sunglasses:
### To Build a django app image, Run:
`docker build -t django-app:1.0 .`

This creates a docker image with the tag of django-app and vesrion is assigned as 1.0

### To Run and Test if it works, Run:
`docker run --name=my-django-app -p=8000:8000 django-app:1.0`

This command will 
  - run a container named my-django-app :heavy_check_mark:
  - use django-app image we have just created :heavy_check_mark:
  - opens the port 8000 in your local machine :heavy_check_mark:

Go to http://localhost:8000 to test if everything is OK.

