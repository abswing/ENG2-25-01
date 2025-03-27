from datetime import datetime


data_nasc = input("digite sua data de nacimento (dd/mm/yyyy): " )
nacimento= datetime.strptime(data_nasc, '%d/%m/%Y')
hoje = datetime.today()
idade = hoje.year - nacimento.year 

print(f"voce tem {idade} anos.")
