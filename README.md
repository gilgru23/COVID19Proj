# Corona Project Instructions

## Some important instructions for operating the project:
  - The python version that should be running on the machine is 3.8 or above !! If you use Docker image this Dockerfile below in the "Installations" section created an image that ran my project pretty well.
  - All the other dependencies are installed automatically in the Jenkinsfile through requirements.txt that was uploaded the Git repository.
  - I added initial queries as countries parameters to the Jenkinsfile. While activating the job these parameters will be queried automatically to the project and the output will be shown in the Jenkins job console.
  - You can add an unlimited number of countries as parameters to the Jenkins projects, they will be queried to the Flask service automatically by the Jenkinsfile.


## Operations on the project
  - you should enter countries as project paramaters and get: the hight peak and the date of new cases,recovered and deaths in the last 30 days.
  - The "status" request will return json with the content:"fail" if the last connection with the service was failed, or if there wan't connection with the service yet, else it will return json with the content:"success".
  - The service will run without stopping on http://127.0.0.1:5000/ once you activate the project. I added the option to shut this connection gracefully by typing the command: "curl 'http://127.0.0.1:5000/shutdown'".



### Installation

Docker file:
  ```sh
FROM jenkins/jenkins:lts-alpine
MAINTAINER Valery M. <manycoding@users.noreply.github.com>

USER root

RUN apk add --no-cache python3 python3-dev curl gcc g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --upgrade pip setuptools && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
    if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
    rm -r /root/.cache
RUN apk add libffi-dev
RUN apk add libressl-dev
USER jenkins
```
Open your favorite Terminal and run these commands afterwards:
```sh
docker build -t <Image name>:latest .
```
```sh
docker run -p 8080:8080 -p 5000:5000 <Image name>:latest
```

