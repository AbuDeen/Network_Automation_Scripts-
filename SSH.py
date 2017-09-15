import paramiko
import time

ip_address = "172.16.206.232 "
username = "python"
password = "cisco"

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print "Successful connection", ip_address

remote_connection = ssh_client.invoke_shell()

remote_connection.send("configure terminal\n")
remote_connection.send("int loop 0\n")
remote_connection.send("ip address 1.1.1.1 255.255.255.255\n")

remote_connection.send("end\n")
remote_connection.send("wr\n")

time.sleep(1)
output = remote_connection.recv(65535)
print output

ssh_client.close
