# README

A simple Python web application running on Docker Compose. The application uses the Flask framework and maintains a commandline logging for the hits to the api endpoint localhost:8001/info . This is a basic api which could be deployed by using the shell script deploy.sh

<!-- GETTING STARTED -->
## Getting Started

The below steps would define on how you would get a local copy up and running follow these simple example steps. To make the api work on your local machine.

### Prerequisites

Make sure you have already installed both Docker Engine and Docker Compose. You don’t need to install Python or Flask, as both are provided by Docker images.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/anz-ecp/Mohammad-Shiraz-.git
   ```
2. Change directory to the api deployment folder with the below command
   ```sh
   cd Mohammad-Shiraz-/interview/
   ```
3. Excecute the below command to activate the deployment script.
   ```sh
   sh deploy.sh
   ```

<!-- Post Deployment -->

Once the deployment has been completed open your browser and enter (http://localhost:8001/info)

   ```JS
   {"environment":{"log_level":"INFO","service_port":"8001"},"git_commit_sha":"5edcb3f","service_name":"myapplication","version":"1.0.0"}
   ```


if you check the command line you would be able to see the standard log set in the below format with the IP address of the requester

```sh
anz_master       | [2021-06-16 11:57:09 +0000] [9] [INFO] in app: /info accessed from IP: 172.22.0.1
anz_master       | [2021-06-16 12:00:05 +0000] [9] [INFO] in app: /info accessed from IP: 172.22.0.1
anz_master       | [2021-06-16 12:00:06 +0000] [9] [INFO] in app: /info accessed from IP: 172.22.0.1
anz_master       | [2021-06-16 12:00:07 +0000] [9] [INFO] in app: /info accessed from IP: 172.22.0.1

```

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [GitHub Pages](https://pages.github.com)
* [DockerCompose.css](https://docs.docker.com/compose/reference/)
* [FlaskLogging.css](https://flask.palletsprojects.com/en/2.0.x/logging/)


