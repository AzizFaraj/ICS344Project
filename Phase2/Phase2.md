# Phase 2: Visual Analysis with a SIEM Dashboard\

# Installing the Splunk Server (SIEM)

## Installing Splunk Server

We first install the splunk server package in the attacker machine (Kali Linux)

<img src="https://github.com/user-attachments/assets/2043462a-3d50-473c-bd2d-e95c8bd32fb4" alt="Alt Text" style="width:50%; height:auto;">

---

## Downloading the Splunk Server .deb Package

Then we download the Splunk server .deb package

<img src="https://github.com/user-attachments/assets/31d61abe-8c2e-4125-836d-6fa6fd07a906" alt="Alt Text" style="width:50%; height:auto;">

---

## Starting Splunk for the First Time

We start Splunk for the first time

<img src="https://github.com/user-attachments/assets/89aa6ff9-7ef9-4332-801f-df1ee5641657" alt="Alt Text" style="width:50%; height:auto;">
<img src="https://github.com/user-attachments/assets/46d5d22a-67e6-4a90-aea3-cc0f17b89e0b" alt="Alt Text" style="width:50%; height:auto;">

---

## Starting Splunk Web Interface

We then can access the Splunk web interface by running **localhost:8000**

<img src="https://github.com/user-attachments/assets/b4dc1b3f-a3d0-4b24-851b-b9bcb47ea8b3" alt="Alt Text" style="width:50%; height:auto;">

---

# Installing Splunk Forwarder 

This will be done in the victim machine as shown below

<img src="https://github.com/user-attachments/assets/eb47eb00-8b02-4294-aced-97ce64119f2b" alt="Alt Text" style="width:50%; height:auto;">

---

## Starting Splunk Forwarder

We then start Splunk Forwarder and accepting the license

<img src="https://github.com/user-attachments/assets/0b2a3341-2883-45ff-97ab-76d509f4e6e8" alt="Alt Text" style="width:50%; height:auto;">
<img src="https://github.com/user-attachments/assets/0f219a6f-85dc-4071-b2f3-aba029a480e1" alt="Alt Text" style="width:50%; height:auto;">

---

## Connecting Forwarder to Splunk Server

After that, we connect the forwarder to Splunk server

<img src="https://github.com/user-attachments/assets/edb74538-656a-4a77-9ef5-070178608340" alt="Alt Text" style="width:50%; height:auto;">

---

## Adding Data Inputs (Log Files)

We add the data inputs as such

<img src="https://github.com/user-attachments/assets/e866c475-ed3b-4ad2-9c24-adec896cdaae" alt="Alt Text" style="width:50%; height:auto;">

---

## Attack Logs of Failed and Accepted Passwords

After executing the attack, the logs will be shown in Splunk with the "Failed password" and "Accepted password" 

<img src="https://github.com/user-attachments/assets/2c6bfe8d-251c-4770-946d-48a96dd801dd" alt="Alt Text" style="width:50%; height:auto;">
<img src="https://github.com/user-attachments/assets/c299368c-139f-48bb-9316-54b0f0ba41aa" alt="Alt Text" style="width:50%; height:auto;">

---

## Visualization of the Attack

Here is a visualization of the attacks that shows the number of failed passwords and the number of accepted passwords

<img src="https://github.com/user-attachments/assets/a62b857d-2177-4d6b-83ed-09f79177532e" alt="Alt Text" style="width:50%; height:auto;">

---

## Logs from Both Enviornments 

Below are screenshots of the logs from both the attacker and victim enviornments, the first one is for the attacker and the second is for the victim:

<img src="https://github.com/user-attachments/assets/4bf1cf58-a003-4993-baef-49525b4a4941" alt="Alt Text" style="width:50%; height:auto;">
<img src="https://github.com/user-attachments/assets/d37f386a-1415-4042-85db-e404115806b6" alt="Alt Text" style="width:50%; height:auto;">

