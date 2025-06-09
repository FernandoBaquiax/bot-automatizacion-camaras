import pyautogui as pyi
import os
import importlib
import inspect
import sys
"""
Este Proyecto Tiene como objetivo automatizar la apertura de camaras en Tienda esperanza
Autor: Fernando Baquiax
Fecha: 2025-06
"""
sys.path.append("./steps")
from interfaces.InterfaceStep import Interface_step
import time

#path_photos = "./fotos"

path_photos = "./img/"
path_steps = "./steps" #Carpeta donde estan las clases
total_attempts = 0 #inicio de intentos
attempts_limit = 5 #limite de intentos
time_steps = 5 #Tiempo de espera entre pasos



#Metodo reflection
reflection_list_files = [
    file_dir[:-3] #nombre solamente porque .py son los caracteres que se quita 
    for file_dir in os.listdir(path_steps) #listado de clases o archivos que exista
    if file_dir.endswith(".py") and file_dir != "__init__.py" #solo toma encuenta los que tengan extension py 
]

print("Total de pasos: ",reflection_list_files)
lists_steps= reflection_list_files[:]
print("Pasos a ejecutar: ",lists_steps)
reflection_list_files=lists_steps


for file in reflection_list_files:
    """
        Itera sobre los nombres de los archivos Py
    """  
    moduls = importlib.import_module(f"steps.{file}") 
    """ Obtiene todo el archivo como modulo
    """  

    for name, step_class in inspect.getmembers(moduls, inspect.isclass): #para iterar en cada clase que tenga la interfaz
        """Itera sobre cada clase en el modulo
        """        
        if issubclass(step_class, Interface_step) and step_class is not Interface_step: #verificamos que herede de la interfaz de sptep
            """Verifica que la clase implemente la interfaz 
            """            
            instance = step_class(path=path_photos)#argumento que espera el step
            result = False
            while not result  and total_attempts < attempts_limit:
                time.sleep(time_steps)#pausa
                result = instance.run() #la funcion retorna un booleano
                class_name = instance.__class__.__name__  #nombre de la clase dentro del archivo
                
                if not result:
                    print(f"Error en {class_name}, intento {total_attempts+1}")
                    total_attempts = total_attempts + 1
                else:
                    print(f"Exito en {class_name}")
