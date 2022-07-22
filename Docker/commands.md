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
```bash
$ docker run -it <image_name> 
```    

List the running containers. -a lets you see stopped containers as well.  
```bash
$ docker ps 
```  


