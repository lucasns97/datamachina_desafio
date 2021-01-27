'''
    author: lucas@datamachina.com.br
    date: 27/01/2021
'''

# [START LIBRARY IMPORTS]

from py3dbp import Item

# [END LIBRARY IMPORTS]

def get_item(item):
  '''
  Constroi e retorna o objeto Item a partir dos dados de um veículo

  item = {
    name: string
    dimentions: {
      'length': float (cm)
      'height': float (cm)
      'depth': float (cm)
      'weight': float (kg)
    }
  }
  '''

  item_ = Item(
    item['name'],                 # name
    item['dimentions']['length'], # length 
    item['dimentions']['height'], # height
    item['dimentions']['depth'],  # depth
    item['dimentions']['weight'], # weigth
  )

  return item_