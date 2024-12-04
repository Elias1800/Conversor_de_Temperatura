def opcao(op):
    match op:

        # Celsius para Kelvin
        case 1 :
            celsius = float(input("Qual o valor de Celsius? "))
            print("K = ",celsius + 273.15)

        # Celsius para Fahrenheit
        case 2 :
            celsius = float(input("Qual o valor de Celsius? "))
            print("°F = ",celsius * 1.8 + 32)

        # Kelvin para Celsius
        case 3 :
            kelvin = float(input("Qual o valor de Kelvin? "))
            print("°C = ", kelvin - 273.15)

        # Kelvin para Fahrenheit
        case 4 :
            kelvin = float(input("Qual o valor de Kelvin? "))
            print("°F = ", (kelvin - 273.15) * 9/5 + 32)

        # Fahrenheit para Kelvin
        case 5 :
            fahrenheit = float(input("Qual o valor de Fahrenheit? "))
            print("K = ", (fahrenheit - 32) * 5/9 + 273.15)

        # Fahrenheit para Celsius
        case 5 :
            fahrenheit = float(input("Qual o valor de Fahrenheit? "))
            print("°C = ", (fahrenheit - 32) * 5 / 9)

        case outher : "Opção invalida!"


