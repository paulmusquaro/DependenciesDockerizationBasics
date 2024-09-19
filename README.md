# DependenciesDockerizationBasics

The application is designed to manage various tasks and was developed using Python, with the environment managed via "pipenv". It includes all necessary dependencies, specified in the configuration files "Pipfile". Additionally, a Dockerfile is provided to containerize the application, allowing it to run as a standalone app inside a Docker container. The project showcases virtual environment setup, dependency management, and containerization, all while maintaining a simple and interactive command-line interface.

P.S: This repository contains the project "Personal Assistant".

## Project Setup

### 1. Setting up the Virtual Environment with pipenv

Follow these steps to set up the virtual environment:

1. Install pipenv (if not already installed):
   ```
   pip install pipenv
   ```
2. Activate the virtual environment:
    ```
    pipenv shell
    ```
3. Install project dependencies:
    ```
    pipenv install
    ```
4. Verify Python version (ensure it matches the one specified in Pipfile):
    ```
    pipenv --py
    ```

### 2. Building the Docker Image

To build a Docker image from the Dockerfile and push it to Docker Hub, follow these steps:

1. Build the Docker image:
   ```
   docker build -t <your-dockerhub-username>/personal-assistant:latest .
   ```
2. Verify the image is built:
    ```
    docker images
    ```
3. Login to Docker Hub:
    ```
    docker login
    ```
4. Tag the image for Docker Hub (if necessary):
    ```
    docker tag <image-id> <your-dockerhub-username>/personal-assistant:latest
    ```
5. Push the image to Docker Hub:
    ```
    docker push <your-dockerhub-username>/personal-assistant:latest
    ```

### 3. Running the Docker Container

+ Once the image is pushed to Docker Hub, you can run it locally by executing the following command:

    ```
        docker run -it <your-dockerhub-username>/personal-assistant:latest /bin/bash
    ```

    *Ensure to replace <your-dockerhub-username> with your actual Docker Hub username.

This will start the container and drop you into the interactive shell where you can run the Personal Assistant application.