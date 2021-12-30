from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

link = os.getenv('PYTHON_APP_LINK') 
nik = os.getenv('PYTHON_APP_NIK')
password = os.getenv('PYTHON_APP_PASS')
is_active = os.getenv('PYTHON_APP_ACTIVE')