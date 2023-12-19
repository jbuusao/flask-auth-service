import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

# Get environment variables
DBNAME = os.getenv('DBNAME')
DBUSER = os.getenv('DBUSER')
DBPASSWORD = os.getenv("DBPASSWORD")
AUTHSECRET = os.getenv("AUTHSECRET")
EXPIRESSECONDS = os.getenv('EXPIRESSECONDS')

mydb = mysql.connector.connect(
  host="localhost",
  user=DBUSER,
  password=DBPASSWORD
)

print(mydb)
