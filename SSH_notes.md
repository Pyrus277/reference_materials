## SSH - 3 Commmon Uses

### Accessing a Remote Virtual Machine  
  
Example: Using SSH to connect to a remote server in AWS Cloud:  
**Step 1**  
In the AWS Management Console go to EC2 to see running instances.
Then go to the security tab and click Security groups.
Scroll down to the Inbound rules section and click “Edit inbound rules.”  
**Step 2**  
Click Add rule, and select SSH from the Type dropdown, and Anywhere from 
the Source dropdown. Fill in a description. Now the port is open.  
**Step 3**  
Go back to EC2 and get to the running instances. In the Details tab you can find 
the Public IPv4 address. Write that down and go back to your terminal.  
**Step 4:**   
In your terminal go to your .ssh dir. Then copy the contents of the id_rsa.pub file 
(if it doesn’t exist, need to generate one with $ssh-keygen -t rsa).  
**Step 5:**   
Back in AWS, paste the copied public key from your terminal into ~/.ssh/authorized_keys  
**Step 6:** 
Finally, back at your terminal, go $ ssh <username ($whoami on remote terminal)> <ip address you wrote down>  
    
Note: ^^This is generally the same procedure for all remote hosts. Similar thing you did with Vultr, 
for instance. Copy your generated public SSH key into the vm provider, know the IP address of the instance, 
and run the ssh command with that address.
  
  
### Connecting to GitHub  
Example: Creating SSH KEys and using with GitHub:  
**Step 1:**   
Generate an SSH key:
```bash
$ ssh-keygen -t rsa
```
This creates a public and private key pair.  
**Step 2:**   
Copy the public key and paste it into GitHub.  
Go to your profile > settings > SSH and GPG keys  
**Step 3:**    
Go back to your local machine and run $ git clone….  
  
### SSH Tunneling  
This lets you forward your traffic to a remote location and makes your machine appear to be in that location.   
    
On the local machine, or the machine you’re tunneling from, go:  
```bash
$ ssh -N -L 8080:127.0.0.1:8080 <username>@<ip.address>
```
This example is saying “On my local machine (127.0.0.1), I want to connect the remote port 8080 to my port 8080 
using my SSH connection info (<username>@<ip.address>)
  
#### Didn't love this explanation. Find a good video on youtube for SSH tunneling. 
