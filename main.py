'''
    author: lucas@datamachina.com.br
    date: 27/01/2021
'''

# [START LIBRARY IMPORTS]

# Http Libs
from flask import Flask, request, abort
from flask_cors import CORS

# Settings
from settings import PORT
from settings import DEBUG, API_KEY

# Fibonacci
from src.fibonacci.fibonacci import Fibo

# Delivery
from src.delivery.delivery import Delivery

# [END LIBRARY IMPORTS]


# [START ENDPOINT]

app = Flask(__name__)
CORS(app)

def oauth(request):
  '''
  Verifica se o request está com a autenticação correta

  return:

  response = {
    'success': bool,
    'message': string
  }
  '''

  # Autenticação
  oauth = request.headers.get('Authentication')

  if oauth != API_KEY:

    response = {
      'success': False,
      'message': 'Credenciais inválidas. Preencha o \'header\' com o campo Authentication'
    }

  else:
    response = {
      'success': True
    }
  
  return response

@app.route('/fibonacci', methods=['GET'])
def fibonacci_route(*args, **kwargs):
  """Rota para o problema 1 (Fibonacci)"""

  oauth_response = oauth(request)

  # Caso não esteja com a autenticação correta
  if not oauth_response['success']:
    return oauth_response, 403

  input_value = request.values.get('value')

  if not input_value:

    response = {
      'success': False,
      'message': 'Preencha o campo \'value\' da query do request.'
    }

    return response, 400

  fibo = Fibo()
  
  response = fibo.calculate(input_value)
  
  return response


@app.route('/delivery', methods=['POST'])
def delivery_route(*args, **kwargs):
  """Rota para o problema 2 (Empacotamento)"""

  oauth_response = oauth(request)

  # Caso não esteja com a autenticação correta
  if not oauth_response['success']:
    return oauth_response, 403
  
  try:
    input_items = request.json.get('items')

  except:
    response = {
      'success': False,
      'message': 'O request deve ser feio com um json body.'
    }

    return response, 400

  if not input_items:

    response = {
      'success': False,
      'message': 'Preencha o json body do request com o campo \'items\'.'
    }

    return response, 400

  delivery = Delivery()
  
  response = delivery.best_fit(input_items)
  
  return response

# [END ENDPOINT]


if __name__ == '__main__':

    PORT = int(PORT) if PORT else 8080
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG)