# Week 1 — App Containerization

Docker file contain  instruction on how to run your app 
- Learn about DockerFile and the Docker import structure
- Learn about Dockerfile syntax
- was able to run the application locally 
- was able to build my backend application docker image with the command docker build -t  backend-flask ./backend-flask 
- was able to run the image with this command FRONTEND_URL="*"  BACKEND_URL="*" docker  run --rm -p 4567:4567 -d backend-flask