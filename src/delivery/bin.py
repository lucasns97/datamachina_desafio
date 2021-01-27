'''
    author: lucas@datamachina.com.br
    date: 27/01/2021
'''

# [START LIBRARY IMPORTS]

from py3dbp import Bin

# [END LIBRARY IMPORTS]

def get_bin(vehicle):
  '''
  Constroi e retorna o objeto Bin a partir dos dados de um veículo

  vehicle = {
    name: string
    dimentions: {
      'length': float (cm)
      'height': float (cm)
      'depth': float (cm)
      'weight': float (kg)
    }
  }
  '''

  bin_ = Bin(
    vehicle['name'],                 # name
    vehicle['dimentions']['length'], # max length 
    vehicle['dimentions']['height'], # max height
    vehicle['dimentions']['depth'],  # max depth
    vehicle['dimentions']['weight'], # max weigth
  )

  return bin_