<center>

<h1><b>0x03. AirBnB clone - Deploy static</b></h1><center>

<center>

**DevOps**

**Python**

**SysAdmin**

**Scripting**

**CI/CD**

**Background Context**<center>

---

<h3>Ever since you completed project 0x0F. Load balancer of the SysAdmin track, you’ve had 2 web servers + 1 load balancer but nothing to distribute with them.</h3>

<b><em><h4>It’s time to make your work public!</h4></em></b>

<h3>In this first deployment project, you will be deploying your web_static work. You will use Fabric (for Python3). Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution. This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s). Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.</h3>

<h3>NOTE: Before starting, please fork the repository AirBnB_clone_v2 from your partner if you don’t have it.</h3>

**General**

```markdown
* What is Fabric
* How to deploy code to a server easily
* What is a tgz archive
* How to execute Fabric command locally
* How to execute Fabric command remotely
* How to transfer files with Fabric
* How to manage Nginx configuration
* What is the difference between root and alias in a Nginx configuration
```

<b>More Info</b>

<b>Install Fabric for Python 3 - version 1.14.post1</b>

```python
$ pip3 uninstall Fabric
$ sudo apt-get install libffi-dev
$ sudo apt-get install libssl-dev
$ sudo apt-get install build-essential
$ sudo apt-get install python3.4-dev
$ sudo apt-get install libpython3-dev
$ pip3 install pyparsing
$ pip3 install appdirs
$ pip3 install setuptools==40.1.0
$ pip3 install cryptography==2.8
$ pip3 install bcrypt==3.1.7
$ pip3 install PyNaCl==1.3.0
$ pip3 install Fabric3==1.14.post1
```