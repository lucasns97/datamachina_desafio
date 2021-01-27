'''
    author: lucas@datamachina.com.br
    date: 27/01/2021
'''

# [START LIBRARY IMPORTS]

# .env handler
from dotenv import load_dotenv

# Directory handler
import os

# [END LIBRARY IMPORTS

# Carragando .env
load_dotenv()

# Variáveis de desenvolvedor
DEBUG = False
PORT  = 5000

# Chave de API
API_KEY = os.getenv("API_KEY")