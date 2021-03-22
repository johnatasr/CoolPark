# CoolPark

Coolpark é uma API de registros de estacionamento, onde é possível ser integrada de forma fácil com qualquer dispositivo via Rest


## Requisitos

* Docker
* Python 3.7 >

# Tecnologias

* Django
* Django RestFramework 
* Poetry
* Black
* Docker
* Gitlab CI


## Iniciando

Passos para configurar o projeto com docker:

1. `cd` na pasta do projeto
2. `docker-compose up --build`

Caso não deseje o uso de docker:
1. `Inicie um virtual env`
3. `pip install -r requirements.txt`
2. `python manage.py runserver`

O projeto por padrão estará em localhost:8000 

## Como usar ? 

Check-in

Para fazer o check-in via api é necessário apenas a placa do veículo no payload da requisição. O endpoint responsável é: 

```
curl --request POST \
  --url http://localhost:8000/parking \
  --header 'Content-Type: application/json' \
  --data '{
	"plate": "ABC-1234"
}
	'
```

Check-out

Para fazer o check-out é necessário passar o ID do parking na url e ter feito o pagamento no endpoint de pagamento. O endpoint responsável é: 

```
curl --request PUT \
  --url http://localhost:8000/parking/10/out
```

Do-Payment

Este é o endpoint de pagamento, no caso, é passado o ID do parking na url e logo após processado pode ser feito o check-out. Abaixo o enpoint de pagamento:

```
curl --request PUT \
  --url http://localhost:8000/parking/10/pay
```

Parking-History

Por esse endpoint é possível obter o histórico de registros de um determinado veículo pela placa. Será apenas necessário passar a placa na url como no exemplo abaixo: 

```
curl --request GET \
  --url http://localhost:8000/parking/ABC-1234
```




