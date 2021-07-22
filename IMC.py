def mensaje():
    mensaje = """
    ---------------------------------------------
             Vamos amedir tu IMC
    ---------------------------------------------
    """
    print(mensaje)

  
def calcularIMC(peso_en_libras,altura_en_metros):
    peso_en_libras = float(peso_en_libras)
    altura_en_metros = float(altura_en_metros )
    peso_en_kg =  0.45*peso_en_libras;
    IMC = peso_en_kg/(altura_en_metros*altura_en_metros)
    return IMC

def informe(elIMC):
    if elIMC < 18.5:
        print('Bajo peso')
        print('Comer bastantes proteinas')
        print('Ingerir carbohidratos')
        print('Consumir grasas naturales')
      
    elif elIMC > 18.5 and elIMC < 24.9:
        print("""
        -------------------------------------
        Peso normal ☜(⌒▽⌒)☞
        -------------------------------------
        """)
        print('Moderar los carbohidratos')
        print('Consumir menos grasas trans')
        print('Realizar un deficit calórico')
      
    elif elIMC > 25 and elIMC < 29.9:
        print("""
        -------------------------------------
        Sobrepeso (´･_･`)
        -------------------------------------
        """)
        print('Consumir cierto porcentaje de proteinas')
        print('Realizar un deficit calorico')
        print('Tener una injesta baja en carbohidratos')
      
    elif elIMC >= 30 :
        print("""
        -------------------------------------
        Obesidad ಥ﹏ಥ
        -------------------------------------
        """)
        print('No consumir carbohidratos')
        print('Hacer un deficit calorico elevado')
        print('Comer carnes megras en general')



      
#LÓGICA DEL PROGRAMA
mensaje()

peso = input('Tu peso en lb: ') 
altura = input('Tu altura en mt: ')

elIMC = calcularIMC(peso, altura)

informe(elIMC)
