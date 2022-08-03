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


### Dockerize a web app
Step 1. Add a docker file to your application files. This file contains instructions for building an image.  
Step 2. In that file, create an image with the FROM command after researching the platform and runtime environment you want your app to run on. In this case:
```docker
FROM node:14.16.0-alpine3.13
```
Step 3: In the terminal window for the working dir, build the image:
```bash
$ docker build -t react-app .  # react-app being the name we're assigning it
```
This is a main command - when you make updates to the docker file, need to rerun this build command.   
  
Step 4: Confirm the existence of the new image with
```bash
$ docker image ls
```
Step 5: Build the container in the image we just made:
```bash
$ docker run -it react-app
```
This will put us in the interactive mode for the programming language. We gotta get out and go back in with the above command, but append 'bash' to the end. In the case of Alpine in this example, Bash is not part of the os, so we actually append "sh" for shell.
You can also just run images you have saved if you want to play around on the command line to get a sense of what functionalities that particular shell has. 

Step 6: Copy application files into the image. 
```docker
WORKDIR /app
COPY . .
```
See notes in the commands.md file.

Step 7:
Create a system user on which your app will run.
On the cli it would go like,
```
$ addgroup app # app is just the name we assign
$ adduser -S -G app app # -S designates it as a system user (as opposed to a human account). -G assigns the group, app. Final argument, app, is the user name. Same as group, a linux best practice.
```
but we can just chain these commands and put them in our Dockerfile in a RUN statement. And then likewise set the user
```docker
RUN addgroup app && adduser -S -G app app
USER app
```

Step 8:
Set the entrypoint in your Docker file
```bash
CMD [“npm”, “start”]
```

### The Docker file so far
```docker
FROM node:14.16.0-alpine3.13

RUN addgroup app && adduser -S -G app app 
RUN mkdir /app && chown app:app /app # !! This line here not shown above, it resolves permission issues. !!
USER app

WORKDIR /app
COPY package*.json ./  # !! This line here not shown above it allows docker to reuse the npm package files from the cache, even if other changes to the file are made. !!
RUN npm install
COPY . . # copyting application files-- this layer should always be rebuilt. 
ENV API_URL=http://api.myapp.com
EXPOSE 3000

CMD [“npm”, “start”]
```

### Tagging images

Docker automatically puts the "latest" tag on files, but this can come to be misleading. So always tag your images. 
You can tag an image when you build it by appending :<tagname> to the usualy build commmand  
```docker
docker build -t react-app:<name> .
```
If the file is updated often usually a simple integer is used.  
If it's updated not so often, some groups use version numbers like 3.4.1  
Other groups use a code name.
  
You can also just use the tag command:
  ```docker
  docker image tag react-app:latest react-app:1
  ```

### Sharing images
How to share images without going to Dockerhub.  
This command saves a compressed file of the image in the current folder.
$ docker image save -o <compressed name> <repository name>:tag
```bash
docker image save -o react-app.tar react--app:3
```  
    
If you have a compressed image saves, you can then load it by:
$ docker image load -i react-app.tar
  
  
