# Phase 1: Setup and Compromise the Service 

# Setting Up the Victim Machine

We first import the Metasploitable 3 virtual machine.

![image](https://github.com/user-attachments/assets/6da81074-0f70-4f0f-bf4f-a252a38b3aaa)

Then Configure Appliance Settings and set the RAM and CPU to 2.

![image](https://github.com/user-attachments/assets/a7f7b1e9-b4ac-4ca2-813e-48661041aa61)

After logging in into the Metasploitable 3 we find the IP address of the victim machine by using ifconfig to see the IP, which is **10.0.2.6**.

![image](https://github.com/user-attachments/assets/d7837404-e210-4563-a554-0aefd716fd8a)

We check the reachability by  pinging the victim machine in Kali Linux.

![image](https://github.com/user-attachments/assets/cabc2528-c2df-417b-a471-2d6f60a8c9b4)

<img src="(https://github.com/user-attachments/assets/cabc2528-c2df-417b-a471-2d6f60a8c9b4)" alt="drawing" width="200"/>

Note that the IP of the attacker machine, which is the Kali Linux, is **10.0.2.15**.

