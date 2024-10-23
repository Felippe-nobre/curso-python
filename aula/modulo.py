#Módulos são arquivos que contêm definições e implementações de funções, classes e variáveis que você pode reutilizar em diferentes partes do seu código. Python possui muitos módulos padrão que você pode importar para ampliar suas funcionalidades, sem ter que reinventar a roda.

import math#Para importar um módulo, usamos a palavra-chave import. Por exemplo, o módulo math contém funções matemáticas avançadas:
print(math.sqrt(16))

from math import pi#Você também pode importar apenas uma parte do módulo usando from ... import ....
print(pi)

import math as m#Você pode usar a palavra-chave as para renomear um módulo ou função para simplificar seu uso.
print(m.sqrt(25))


import meu_modulo   #Assim como o Python oferece módulos, você também pode criar os seus. Basta criar um arquivo .py com funções e variáveis que deseja reutilizar.
print(meu_modulo.saudacao("Felippe"))

import requests
response = requests.get("https://api.github.com")
print(response.status_code)  # Saída: 200
