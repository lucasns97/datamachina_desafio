# Resolução desafio de ingresso Data Machina

#### Autor: Lucas Nunes Sequeira (lucasnseq@gmail.com) - 27/01/2021

## Descrição do desafio

Desenvolver uma API para executar a solução de dois problemas. O primeiro problema consiste em calcular o n-ésimo termo da sequência de Fibonacci, enquanto o segundo problema consiste em determinar qual o melhor veículo em que cabe uma lista de itens com dimensões espaciais e peso para cada empresa enunciada.

## Solução

### 1. Preparando o ambiente para ligar a API

Primeiro devem ser instaladas as dependências listadas no arquivo ```requirements.txt``` na raiz do projeto.

Exemplo de uso (no terminal):

```
$ pip install -r requirements.txt
```

### 2. Ligando a API

Para ligar a API basta executar o seguinte comando na raiz do projeto (no terminal):

```
python main.py
```

Você deve obter uma resposta semelhante à esta:

```
* Serving Flask app "main" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
```

Nesse momento a API estará ligada, e o endereço base para fazer as chamadas locais mostra na resposta acima. Exemplo: ```http://0.0.0.0:5000```

### 3. Autenticação das requisições

Todas as requisições feitas para as rotas das respostas aos problemas 1 e 2 devem acompar de uma autenticação no ```header```. Para isso, o header deve conter:

```
"Authentication": "123123"
```

### 4. Problema 1

Para executar o problema 1 (Fibonacci), a requisição sobre a API deve ser feita pelo método GET no seguinte endpoint: ```/fibonacci```

A requisição deve conter uma ```query``` preenchida com o campo ```value``` e o número inteiro não negativo de interesse para determinar a solução do problema.

#### Exemplo de uso:

```json
# Request

query = {
  "value": 10
}
```

```json
# Response

{
  "success": true,
  "value": 12586269025
}
```

### 5. Problema 2

Para executar o problema 2 (Empacotamento), a requisição sobre a API deve ser feita pelo método POST no seguinte endpoint: ```/delivery```

A requisição deve conter um ```json``` preenchido com o campo ```items``` que representa uma lista de itens. Certifique-se que foi adicionado ao header o seguinte campo: ```"Content-Type": "application/json"```. Vale notar que cada item da lista de itens é dado da seguinte forma:

```
{
  "name": "Banana",
  "dimentions": {
    "length": 10.0, # float - cm
    "height": 5.0,  # float - cm
    "depth": 5.0,   # float - cm
    "weight": 1.5   # float - kg
  }
}
```

#### Exemplo de uso:

```json
# Request

json = {
	"items": [
		{
			"name": "Banana",
			"dimentions": {
				"length": 15.0,
				"height": 30.0,
				"depth": 45.0,
				"weight": 3.5
			}
		},
		{
			"name": "Laranja",
			"dimentions": {
				"length": 10.0,
				"height": 25.0,
				"depth": 35.0,
				"weight": 3.5
			}
		},
		{
			"name": "Mandioca",
			"dimentions": {
				"length": 10.0,
				"height": 20.7,
				"depth": 26.0,
				"weight": 5.0
			}
		}
	]
}
```

```json
# Response

{
  "data": {
    "Lala": "Fiorino",
    "Ogi": "Moto"
  },
  "success": true
}
```