# Week 1 — App Containerization

Docker file contain  instruction on how to run your app 
- Learn about DockerFile and the Docker import structure
- Learn about Dockerfile syntax
- was able to run the application locally 
- was able to build my backend application docker image with the command docker build -t  backend-flask ./backend-flask 
- was able to run the image with this command  : docker  run --rm -p 4567:4567 -d  -e FRONTEND_URL='*'  -e BACKEND_URL='*' backend-flask
- was able to open the OS bash CLI on which our container is running with this command Docker exec -it <dockerImageID> bash
- learn and run multiple docker like docker ps : docket logs : docker ps -a : docker stop 

---
##  Screenshot images
---

- Application running locally
![application running locally](assets/app-running-locally.png)

---

- Build Docker image - run container
![build-docker-image-run-docker-container-and-test-it](assets/build-docker-image-run-docker-container-and-test-it.png)

---

- see env-var-in-the-container-OS
![env-var-in-the-container-OS](assets/env-var-in-the-container-OS.png)

--

- build-frontend-docker-image-and-run-it.png
![build-frontend-docker-image-and-run-it.png](assets/build-frontend-docker-image-and-run-it.png)

--

- sfrontend-running.png
![frontend-running.png](assets/frontend-running.png)
