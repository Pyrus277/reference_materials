## Docker Commands

Pulls the specified image onto your machine:
```bash
$ docker pull <image_name>
```      
   
     
The run command is how you execute your packaged images.
If you have this image locally, docker will store this container with his image.
Otherwise it will pull this image behind the scenes and then start the container.
Will only maintain the container if we **interact with it by using the -it (interactive) flag**
The -it flag will start an interactive shell with a generated name.
On hub.docker.com we can find official container names. 
How to start a container from an image.
```bash
$ docker run -it <image_name> 
```
To run the container and the app within:
```bash
$ docker run <app-name> npm start # npm start in the case of a js node app.
```
To run the container in detached mode.
After this, when you run docker ps, you'll see it running in the background. 
```bash
$ docker run -d react-app
```
List the running containers. -a lets you see stopped containers as well.  
```bash
$ docker logs <first few chars of id>
$ docker logs -n 5 -t <first few chars of id> # show the 5 most recent lines 
```  
Reading logs - for running containers in the background, if you're having issues or want to see
the outputs, you can check the logs:
```bash
#
```

Start a container. If you run $ docker ps -a, you can start up a stopped image by typing:
```bach
$ docker start -i <first few characters of the container ID>
```  
  
  Enter into a running process, one of the ones listed after typing $ docker ps. If you don't specify the username with -u it'll default to root:
  ```bash
  $ docker exec -it -u <username> <container id> bash
  ```
#### The recurring combo:
```bash
# When you create or update the Dockerfile, run this command to apply.
$ docker build -t <app name> . 
# Then to build and enter the container go:
$ docker run -it react-app bash
   # if we don't specify bash or sh, it'll default to the runtime language. 
```
### Removing dangling images
```bash
$ docker container prune
$ docker image prune
```
#### Publishing Ports
Running a web app in the container will publish to a port within the container, but not on the host machine.
To send traffic to the host machine port, you need to publish a port:  
1. Run $ docker ps to see the running containers and look at the Image Ports column.  
2. You'll then have to start a new container and publish the port as part of the run command.  
3. $ docker run -d -p <host port>:<container port> --name <name you want> <image name>
Example:
```bash
docker run -d -p 80:3000 -name c1 react-app
```
Now if you open a browser and visit localhost:<host port>, you'll see your app in action.  

#### Executing commands in a running container.
For a single command:
$ docker exec <container name> <command>
```bash
docker exec c2 ls
```
To get a shell session going:
```bash
$ docker exec -it c2 sh   
```
**NOTE:** $ Run starts a new containers, $ start resumes a stopped one.
   
#### Removing containers
You can't remove a running container. You must stop it first, or force the remove.
```docker
$ docker rm -f <container name> # -f tag forces removal.
```
  
#### Persisting Data with Volumes.
   
## Instruction keywords:

#### Keyword: FROM
Used to specify the base image which we build on.
This command takes an OS or and OS + a runtime environment. 
See Google "node docker image" and go to the result for Dockerhub for examples of docker files for different tech stacks. 
Never use the :latest flag. Always go with a specific version. 
On that site, search the scripting platform you want. In the case of Javascript, we would seach for Node.
Then from there, we can go to the tags tab to look for the OS we want. This approach will get you a FROM statement that looks like:  
```bash
FROM node:14.16.0-alpine3.13
```
Alpine being a super lightweight distro of Linux. 


#### WORKDIR:   
Specifies the working directory. All the subsequent commands will be executed in the current working directory. 
#### COPY & ADD:   
Copies files and directories.  
COPY will copy one or more files from the working dir into the image.  
```docker
COPY <filename> <filename2>... /folder/ # if the folder in the folder argument doesn't exist, Docker will create.
# We're in a Linux env, so wildcards are good to use here.
# To just go ahead and copy everything in the curret directory into the app dir, we can just go like
COPY . /app/
# The dir argument can be aboslute, but it can be relative if we set the working directory first:
WORKDIR /app
COPY . .
# If any of the arguments after copy take a filename with a space in it, all the arguments need to go in [], and each one within ""
```
ADD has syntax just like copy, except it can take URLs as arguments if you have files hosted online.
It can also take compressed files and decompress them into the directory. 
You can also make a .dockerignore file to list things you don't want copied over.

#### RUN:   
Executes OS commands. All the Bash lines you want to execute go here.
#### ENV:   
Set environment variables. For examples:
```docker
ENV API_URL=http://api.myapp.com
```
#### EXPOSE:
```docker
EXPOSE <port number> 
```
Tells docker that our container is starting on a specific port.
#### **Important** If from a Docker container you run an app that runs a webserver from a specific port, the port that is open is from the container, not the host computer.  
Tells what port the container will be listening on. 
Doesn't automatically publish the port on the host, it's just a form of documentation form of documentation to communicate what port the container will eventually listen on.


#### USER:  
Specifies the user that should run the app. Usually one with limited privileges.
#### CMD & Entrypoint:  
Specifies the command that should be executed when you start your container.
CMD is different from RUN in that it executes after the container is made. 
With command, use execute form ["",""] so as to not spin up a new shell. Saves resources:
```bash
CMD ["npm","start"]
```

