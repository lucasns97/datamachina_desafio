'''
    author: lucas@datamachina.com.br
    date: 27/01/2021
'''

# [START LIBRARY IMPORTS]

from py3dbp import Packer, Bin, Item

# Company vehicles
from src.delivery.company import COMPANY_VEHICLES

# Bin
from src.delivery.bin import get_bin

# Item
from src.delivery.item import get_item

# [END LIBRARY IMPORTS]


class Delivery():

  def __init__(self):
    
    # Inicializando bins disponíveis
    self._initialize_bins()
  
  def _initialize_bins(self):
    '''
    Inicializa os bins disponíveis para o empacotamento separados por empresa
    '''

    self.available_companies = list(COMPANY_VEHICLES.keys())
    self.available_bins      = {}

    for company in self.available_companies:
      
      self.available_bins[company] = []

      for vehicle in COMPANY_VEHICLES[company]:
        
        bin_ = get_bin(vehicle)

        self.available_bins[company].append(bin_)

  def _restart_delivery(self):
    '''
    Reinicia o empacotamento
    '''

    self.__init__()

  def _verify_items(self, input_items):
    '''
    Verifica se a lista input_items está de acordo com os requisitos de um item

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

    response = {
      'success': True
    }

    for input_item in input_items:

      item_name       = input_item.get('name')
      item_dimentions = input_item.get('dimentions')

      if not item_name or not item_dimentions:

        response['success'] = False
        response['message'] = 'Existe pelomenos um item na lista de itens que não está adequado. Parâmetros faltantes: \'name\' ou \'dimentions\'.'
        break

      item_length = item_dimentions.get('length')
      item_height = item_dimentions.get('height')
      item_depth  = item_dimentions.get('depth')
      item_weight = item_dimentions.get('weight')

      if not item_length or not item_height or not item_depth or not item_weight:

        response['success'] = False
        response['message'] = 'Existe pelomenos um item na lista de itens que não está adequado. Parâmetros faltantes: \'length\' ou \'height\' ou \'depth\' ou \'weight\'.'
        break
        
      if not isinstance(item_length, float) or not isinstance(item_height, float) or not isinstance(item_depth, float) or not isinstance(item_weight, float):

        response['success'] = False
        response['message'] = 'Existe pelomenos um item na lista de itens que não está adequado. Parâmetros incorretos: \'length\' ou \'height\' ou \'depth\' ou \'weight\'. Devem ser float.'
        break
      
    return response

  def fit_company(self, company, input_items):
    '''
    Empacota os itens nos veículos de uma empresa e retorna uma lista de bins em que os itens couberam
    '''

    # Empacotador
    packer = Packer()

    # Seleciona os bins de uma empresa
    bins = self.available_bins[company]

    # Adiciona os bins ao empacotador
    for bin_ in bins:
      
      packer.add_bin(bin_)

    # Adiciona os itens ao empacotador
    for input_item in input_items:
      
      item = get_item(input_item)
      packer.add_item(item)

    # Empacota
    packer.pack()

    # Lista com os bins que couberam
    fitted_bins = []
    for bin_ in packer.bins:

      if len(bin_.unfitted_items) > 0:
        continue

      else:
        fitted_bins.append(bin_)

    return fitted_bins

  def best_bin(self, bins):
    '''
    Retorna o melhor bin com base na heurística de volume (bin com menor volume)
    '''

    bins = sorted(bins, key = lambda x : x.get_volume())

    return bins[0]

  def best_fit(self, input_items):
    '''
    Empacota os nos veículos de cada empresa e retorna para cada empresa o menor veículo (menor volume máximo) em que couberam todos os itens

    retorna:

    response = {
      'success': bool,
      'message': string,
      'data': {
        'company1': 'vehicle_name' ou None,
        'company2': 'vehicle_name' ou None,
      }
    }
    '''

    verify_response = self._verify_items(input_items)

    if not verify_response['success']:

      return verify_response

    response = {
      'data': {}
    }
    
    unfitted_companies = 0

    for company in self.available_companies:

      fitted_bins = self.fit_company(company, input_items)

      # Nenhum veículo desta empresa couberam os itens
      if len(fitted_bins) == 0:
        response['data'][company] = None
        unfitted_companies        += 1

      else:
        best_bin = self.best_bin(fitted_bins)
        response['data'][company] = best_bin.name

    # Verifica se nenhuma empresa foi capaz de levar os itens
    if unfitted_companies == len(self.available_companies):
      response['success'] = False
      response['message'] = 'Nenhuma empresa foi capaz de carregar os itens passados no request.'

    else:
      response['success'] = True

    return response

      



    