import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect("andcsv-devdb13d", 22, "oracle", "changeme")

sftp = ssh.open_sftp()
from_path = "/d00/ESCMSharedFolder/batch_file.bat"
local_path = "D:\\Learn_Devops\\Learn_Devops_Latest\\RestAssured\\RestAssured\\Udemy_Python\\sshConnection\\batch_file_downloaded.bat"
sftp.get(from_path, local_path)