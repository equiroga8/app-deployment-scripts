
# App Deployment Scripts

The goal of this project is to be able to offer a quiz app service to end users (c1, c2, host), by deploying
web servers where the app is hosted. These servers make use of a database and some storage servers. 
To do this we have created some scripts using python and [Ansible](https://www.ansible.com/) to automate the 
deployement of this service.

## Arquitecture

The scenario provided consists of the following elements:
* Two client machines (c1, c2).
* A Firewall (fw).
* A load balancer (lb).
* Three web servers (s1, s2, s3).
* A database machine (bbdd).
* Three disk servers (nas1, nas2, nas3).

These components are connected using four LANs (LAN 1, LAN 2, LAN 3, LAN 4) as follows:

![arquitecture](https://edu-quiroga.neocities.org/Selection_002.png)

 ## Authors

* **Rodrigo Martín** - [rodrimart97](https://github.com/rodrimart97)
* **Eduardo Quiroga** - [equiroga8](https://github.com/equiroga8)
