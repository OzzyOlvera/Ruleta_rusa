import os
import random

pregunta_1 = input("Quieres jugar a la ruleta rusa?  Y/N >:) ")



if pregunta_1 == "Y" or pregunta_1 == "y":
    input("Esta bien, Solo no lloeres depues..")
    
    pregunta_de_harcor = input("quieres introducir una ruta de acceso o te quieres ir por lo hardcor, introduce la letra H si quieres algo harcord y si no una G: ")
    
    if pregunta_de_harcor == "h" or pregunta_de_harcor == "H":
        #optine la ruta de la carpeta sistem32
        ruta = os.path.join(os.environ['WINDIR'], 'System32')
        carpetas = [nombre for nombre in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, nombre))]
        #hace una comprobacion y elije un archivo random
        if carpetas:
            carpeta_aleatoria = random.choice(carpetas)
            carpeta_a_borrar = os.path.join(ruta, carpeta_aleatoria)
            if not os.listdir(carpeta_a_borrar):
                os.rmdir(carpeta_a_borrar)
                print("Carpeta borrada con éxito.")

    if pregunta_de_harcor == "g" or pregunta_de_harcor == "G":
        ruta = input("Intrduce una ruta de acceso a la carpeta que quieres fusilar los archivos: ")
        #verifica que la ruta sea valida
        if os.path.exists(ruta):
            carpetas = [nombre for nombre in os.listdir(ruta) if os.path.isdir(os.path.join(ruta, nombre))]
            carpeta_aleatoria = random.choice(carpetas)
            #hace una comprobacion y elije un archivo random
            if carpetas:
                carpeta_aleatoria = random.choice(carpetas)
                carpeta_a_borrar = os.path.join(ruta, carpeta_aleatoria)
                
                if not os.listdir(carpeta_a_borrar):
                    os.rmdir(carpeta_a_borrar)
                    print("Carpeta borrada con éxito.")
            
            
        else:
            print("ta mal prro")
    
    
elif pregunta_1 == "n" or pregunta_1 =="N": 
    print("Mendiga Miedosa")
