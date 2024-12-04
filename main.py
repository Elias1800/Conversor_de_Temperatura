import functions as fc

print("---- CONVERSOR DE TEMPERATURA ----")
print("")
print("1. Celsius para Kelvin")
print("2. Celsius para Fahrenheit")
print("3. Kelvin para Celsius")
print("4. Kelvin para Fahrenheit")
print("5. Fahrenheit para Kelvin")
print("6. Fahrenheit para Celsius")
print("")

op = int(input("Escolha uma opção: "))
print(fc.opcao(op))