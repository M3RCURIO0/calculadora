#calculando a idade de uma pessoa
print("****Qual é a sua idade?****")
from datetime import datetime

#pede a data de nascimento do usuário
data_nascimento = input("Digite sua data de nascimento (no formato dd/mm/aaaa): ")

#converte a data de nascimento para o formato datetime
data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")

#pega a data atual
data_hoje = datetime.now()

#clacula a idade com base no ano
idade = data_hoje.year - data_nascimento.year

#ajusta a idade se o aniversário ainda não tiver ocorrido este ano
if (data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day): idade -= 1 

#exibe a idade
if idade < 0:
    print("Você ainda não nasceu!")
elif idade >= 50:
    print(f"Você tem {idade} anos, então você é um idoso.")
else:
    print(f"Você tem {idade} anos, então você é jovem.")

