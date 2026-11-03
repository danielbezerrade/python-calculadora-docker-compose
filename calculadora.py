
### CRIANDO CALCULADORA

def calculadora():

        
    try:
        digite1 = float(input("Digite o primeiro número: "))
        digite2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador(+,-,*,/): ").strip()
            

        if operador == "+":
            resultado = digite1 + digite2
            return f"O resultado é de : {resultado}"
                

        elif operador == "-":
            resultado = digite1 - digite2
            return f"O resultado é de : {resultado}"
                 

        elif operador == "*":
            resultado = digite1 * digite2
            return f"O resultado é de : {resultado}"
                   

        elif operador == "/":
            resultado = digite1 / digite2
            return f"O resultado é de : {resultado}"

        else:
            return f"OPERADOR NÃO VÁLIDO: {operador}"
                

    except ValueError as e:
        return f"ERRO: Digite apenas valores numéricos para os números da operação.\nERRO ENCONTRADO: {e}"

    except ZeroDivisionError:
        return f"NÃO DIVISÍVEL POR 0"

if __name__ == "__main__":
    print(calculadora())

            






