dia =int(input())
if dia > 31:
    print('Dia inexistente')
    exit()
    
mes = int(input())
if mes > 12:
    print('Mês inexistente')
    exit()
elif mes in [1,3,5,7,8,10,12]:
    if dia > 31:
        print('Esse dia não existe nesse mês')
        exit()
elif mes in [4,6,9,11]:
    if dia > 30:
        print('Esse dia não existe nesse mês')
        exit()
elif mes == 2:
    if dia > 29:
        print('Esse dia não existe nesse mês')
        exit()
    
ano = int(input())
if ano < 1900 or ano > 2020:
    print('Ano inexistente')
    exit()
if mes == 2 and dia == 29:
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if not bissexto:
        print('Esse ano não é bissexto')
        exit()
print('Data Validada')
