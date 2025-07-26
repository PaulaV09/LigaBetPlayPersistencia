import os

def validateInt(msg:str)->int:
    try:
        x = int(input(msg))
    except ValueError:
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validateInt(msg)
    else:
        return x

def validatetext(msg):
    x = input(msg)
    if all(c.isalpha() or c.isspace() for c in x):
        return x
    elif x.isdigit():
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validatetext(msg)
    elif x.isalnum():
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validatetext(msg)
    else:
        print("ERROR: VALOR INVALIDO")
        os.system("pause")
        return validatetext(msg)
    
def validatefloat(msg:str)->float:
    while True:
        try:
            x = float(input(msg))
            return x
        except ValueError:
            print('ERROR: Ingrese un valor numérico válido.')
            os.system("pause")

def validate_string(msg: str) -> str:
    while True:
        x = input(msg).strip()
        if x:
            return x
        else:
            print("ERROR: La entrada no puede estar vacía.")
            os.system("pause")

def validateBoolean(msg: str) -> bool:
    while True:
        x = input(msg).strip().upper()
        if x == 'S':
            return True
        elif x == 'N':
            return False
        else:
            print("ERROR: Debe ingresar 'S' o 'N'.")
            os.system("pause")