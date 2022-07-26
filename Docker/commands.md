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
  
List the running containers. -a lets you see stopped containers as well.  
```bash
$ docker ps 
```  
  
Start a container. If you run $ docker ps -a, you can start up a stopped image by typing:
```bach
$ docker start -i <first few characters of the container ID>
```  
  
  Enter into a running process, one of the ones listed after typing $ docker ps. If you don't specify the username with -u it'll default to root:
  ```bash
  $ docker exec -it -u <username> <container id> bash
  ```
### Instruction keywords:

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
#### RUN:   
Executes OS commands. All the Bash lines you want to execute go here.
#### ENV:   
Set environment variables.
#### EXPOSE:  
Tells docker that our container is starting on a specific port.
#### USER:  
Specifies the user that should run the app. Usually one with limited privileges.
#### CMD & Entrypoint:  
Specifies the command that should be executed when you start your container.
