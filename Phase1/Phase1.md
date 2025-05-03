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

Note that the IP of the attacker machine, which is the Kali Linux, is **10.0.2.15**.

# Compromising the Victim Machine

The vulnerable service we choose is SSH, where we brute force guessing passwords using the exploit (auxiliary/scanner/ssh/ssh_login)

<img src="https://github.com/user-attachments/assets/b76c88ec-467e-4ee5-b4cc-3772e3634fe1" alt="Alt Text" style="width:50%; height:auto;">

The USER_FILE and PASS_FILE files are provided in the repository.

We automate this process by making a Python script as such:

<img src="https://github.com/user-attachments/assets/5eaf9d01-0177-48e0-a829-d91ead5e468b" alt="Alt Text" style="width:50%; height:auto;">

Then we execute the script to compromise the victim machine:

<img src="https://github.com/user-attachments/assets/8aabcb7e-3ccd-47b0-9aba-fa4c364331c8" alt="Alt Text" style="width:50%; height:auto;">

The script (ssh_brute_force.py) file is provided in the repository.

The victim machine is compromised now by executing the script.







