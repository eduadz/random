#Esse programa é pra conferir o cpf e descobrir os digitos verificadores
cpf = str(input('Digite seu 9 primeiros dígitos: '))
lista = []

#adicionar valores na lista
for i in cpf:
    lista.append(int(i))

#pegando a soma1 e digito1
c = 0
j = 10
for i in lista:
    i *=  j
    c +=  i
    j -= 1
if (c % 11) == 0 or (c%11) == 1:
    d1 = 0
else:
    d1 = 11- (c%11)
print(d1)

lista2 = []
for i in cpf[1:]:
    lista2.append(int(i))
lista2.append(d1)

#pegando a soma2 e digito2
soma2 = 0
j = 10
for i in lista2:
    i *= j
    soma2 += i
    j -= 1
if (soma2 % 11) == 0 or (soma2 % 11) == 1:
    d2 = 0
else:
    d2 = 11- (soma2%11)

print(f'Seu cpf é {cpf}-{d1}{d2} ')











