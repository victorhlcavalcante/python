#calculadora em python

print("\n**************** Python Calculator by Victor *******************")

def add(x, y):
	return x + y

def subtract(x,y):
	return x - y

def divide(x,y):
	return x / y

def multiplication(x,y):
	return x * y

print('\nSelecione a operação matemática que deseja  fazer: \n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Divisão')
print('4 - Multiplicação')

escolha = input('\nDigite uma das opções acima (1/2/3/4): ')

num1 = int(input('\nDigite o primeiro número: '))
num2 = int(input('\nDigite o segundo número: '))

if escolha == '1':
	print('\n')
	print("O resultado de", num1, "+", num2, "é igual a: ", add(num1, num2))
	print('\n')

elif escolha == '2':
	print('\n')
	print("O resultado de", num1, "-", num2, "é igual a: ", subtract(num1, num2))
	print('\n')

elif escolha == '3':
	print('\n')
	print("O resultado de", num1, "/", num2, "é igual a: ", divide(num1, num2))
	print('\n')

elif escolha == '4':
	print('\n')
	print("O resultado de", num1, "*", num2, "é igual a: ", multiplication(num1, num2))
	print('\n')

else:
	print('\nEscolha uma opção valida!')



