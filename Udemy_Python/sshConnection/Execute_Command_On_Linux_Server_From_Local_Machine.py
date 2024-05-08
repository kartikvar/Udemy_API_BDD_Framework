import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("andcsv-devdb13d", 22, "oracle", "changeme")


stdin, stdout, stderr = ssh.exec_command("cd /d00/ESCMSharedFolder \n ls")
print(stdout.readlines())
ssh.close()