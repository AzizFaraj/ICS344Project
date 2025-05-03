# Phase 3: Defensive Strategy Proposal

## Installing Fail2Ban

The defense mechnaism we propose is the "Fail2Ban" security tool that prevents guessing passwords and bans users if they brute force exploits such as the SSH exploit we used. Therefore, we install it in the Metasploitable 3 VM.

<img src="https://github.com/user-attachments/assets/09c2c6a4-a05f-42ab-9713-e3f0f8c23e3f" alt="Alt Text" style="width:50%; height:auto;">

---

We then configure Fail2Ban and add "bantime =600" and "maxretry =3" as such

<img src="https://github.com/user-attachments/assets/469f52fd-bf05-4aef-832b-fbf38c90c13c" alt="Alt Text" style="width:50%; height:auto;">

---

Now after trying to attack and failing for the fourth time, the attacker's IP is banned for 600 seconds

<img src="https://github.com/user-attachments/assets/78a3d219-6bf5-4d4c-8b6c-dc98623ebd92" alt="Alt Text" style="width:50%; height:auto;">

---

After this process, we can see the banned IP by writing sudo **"fail2ban-client status ssh"** in the Metasploitable 3 VM

<img src="https://github.com/user-attachments/assets/7e6059e2-7bee-4ac7-8452-cc7faa8a85bb" alt="Alt Text" style="width:50%; height:auto;">

Which proves that the Fail2Ban security tool works to counter the SSH exploit.
