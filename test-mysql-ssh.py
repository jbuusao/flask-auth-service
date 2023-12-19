import mysql.connector
import sshtunnel
import os
from dotenv import load_dotenv
load_dotenv()

SSH_HOST = os.getenv('SSH_HOST')
SSH_USER = os.getenv('SSH_USER')
SSH_PASSWORD = os.getenv("SSH_PASSWORD")

PA_SERVICE = os.getenv('PA_SERVICE')
PA_DBNAME = os.getenv('PA_DBNAME')
PA_DBUSER = os.getenv('PA_DBUSER')
PA_DBPASSWORD = os.getenv("PA_DBPASSWORD")


sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0
print("About to open tunnel...")
with sshtunnel.SSHTunnelForwarder(
    (SSH_HOST),
    ssh_username=SSH_USER, ssh_password=SSH_PASSWORD,
    remote_bind_address=(PA_SERVICE, 3306)
) as tunnel:
    print(f"About to connect on tunnel port ${tunnel.local_bind_port}...")  
    connection = mysql.connector.connect(
      db = PA_DBNAME,
      user=PA_DBUSER,
      password=PA_DBPASSWORD,
      host='127.0.0.1', port=tunnel.local_bind_port
    )    
    # Do stuff
    print("Connected!")  
    connection.close()