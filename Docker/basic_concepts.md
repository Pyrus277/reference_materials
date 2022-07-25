## Docker is a platform for building, runnng, and shipping applications. 
It's to ensure that if it runs on the development machine, you can share it and it'll work on other machines. 

### Works by way of Containers - isolated environments for running applications. 
These are similar to Virtual Machines, but more are lightweight--they don't take a slice of the actual hardware--and they also use the OS(kernel) of the host machine. This means a Linux machines can only run Lunux containers, but a Windows machine can do Windows and Linux containers since Windows 10 has a Linux kernel embedded. Docker on Mac has to use a lightweight Linux VM.

### Docker Architecture
It uses a client-server (Docker Engine) architecture that uses a REST API. A container is a process. 
  
### Setup
Make sure you see the server block when you run $ Docker version
If you get a permission error, go:
```bash
$ sudo usermod -a -G docker [user]
$ newgrp docker
```
  
### Basic Workflow  
#### Create an **image**
We take an application and "Dockerize" it-- we make a small change so it can be run by docker. This is adding a special plaintext file that includes instructions that docker uses to package everything into an image.
This image contains things such as:
- A cut-down OS
- A runtime environment
- Application files
- 3rd party libraries
- Environment variables.

#### Create a Container  
Once we have an image, we tell Docker to start a container using that image. A container is a process that has its own filesystem provided by the image-- it's an isolated environment. 
When we run the application we do it inside the container using Docker with a special CLI command. 
We can store our container on Docker Hub and from there to any machine running Docker. 
hub.docker.com is a registry for Docker images and you can find the names for official Docker images.


