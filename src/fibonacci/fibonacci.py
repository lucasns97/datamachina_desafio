'''
    author: lucas@datamachina.com.br
    date: 27/01/2021
'''

class Fibo():

  def __init__(self):

    self.input = None

  def __verify_input(self):
    '''
    Verifica se o input usado para calcular o valor de Fibonacci é valido

    retorna:

    response = {
      'success': bool,
      'message': string,
    }
    '''

    response = {}

    try:
      self.input = int(self.input)
    except:
      pass
    
    # Verifica se é um inteiro não negativo
    if not isinstance(self.input, int) or self.input < 0:
      
      response['success'] = False
      response['message'] = 'O valor inserido não é um número inteiro positivo'

    else:
      
      response['success'] = True

    return response


  def calculate(self, n):
    '''
    Calcula o n-ésimo termo da sequencia de fibonacci

    retorna:

    response = {
      'success': bool,
      'message': string,
      'value': integer
    }
    '''  

    self.input = n
    verify_response = self.__verify_input()

    if not verify_response['success']:

      return verify_response

    response = {
      'success': True
    }

    # Termo 0
    if self.input == 0:

      response['value'] = 0

    # Termo 1
    elif self.input == 1:
      
      response['value'] = 1

    # Termo > 1
    else:

      # Variáveis acumulativas
      sum_b = 0
      sum_a = 1

      # Contador
      i = 0
      while i < self.input-1:
        
        # F(N) = F(N-1) + F(N-2)
        fibo_number = sum_a + sum_b

        sum_b = sum_a
        sum_a = fibo_number

        i += 1
      
      response['value'] = fibo_number

    return response