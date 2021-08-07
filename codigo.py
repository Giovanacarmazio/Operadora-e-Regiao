import phonenumbers
from phonenumbers import geocoder , carrier

#Inserir o número com codigo do país e o ddd
phoneNumer = phonenumbers.parse("+5551999999999")

#Procura a operadora
operadora = carrier.name_for_number(phoneNumer, 'pt-br')

#Procura a regiao
regiao = geocoder.description_for_number(phoneNumer, 'pt-br')

#Printa os resultados
print("A Operadora é: " + operadora)
print("O estado é: " + regiao)
