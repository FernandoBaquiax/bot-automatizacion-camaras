from interfaces.InterfaceStep import Interface_step
import pyautogui as pyi
import time as setTime

class Step3(Interface_step):
    def __init__(self, path):
        super().__init__(path)
        self.path = path;
    def run(self) -> bool:
        """
        Este paso mueve las camaras a sus lugares
        """
        try:
            #------Darle Click al grid-------      
            location_grid=pyi.locateOnScreen(self.path+"step3.1.png",confidence=0.9)
            pyi.moveTo(location_grid,duration=3)
            
            #------movimiento de camaras-----
            location =pyi.locateOnScreen(self.path+"step3.png",confidence=0.9)

            pyi.moveTo(location,duration=3)
            setTime.sleep(1)
            x,y = location.left, location.top
            y=y+15
            x=x+15

            #arreglo de posiciones de camaras
            camaras=[y + (i*24) for i in range(0,15) ] 
            
            duracion_colocacion=5;
            
            anexo_parqueo=camaras[0]
            corredor_lateral=camaras[1]
            lector_de_parqueo=camaras[3]
            entrada_parqueo=camaras[8]
            salida_parqueo=camaras[9]
            parqueo_anexo=camaras[10]
            entrada_principal=camaras[12]
            
            

            self.move_mouse(origen_x=x,origen_y=anexo_parqueo,destiono_x=x+400,destino_y=anexo_parqueo,duration=duracion_colocacion)
            self.move_mouse(origen_x=x,origen_y=corredor_lateral,destiono_x=x+800,destino_y=corredor_lateral-50,duration=duracion_colocacion)
            self.move_mouse(origen_x=x,origen_y=lector_de_parqueo,destiono_x=x+800,destino_y=lector_de_parqueo,duration=duracion_colocacion)
            self.move_mouse(origen_x=x,origen_y=entrada_parqueo,destiono_x=x+800,destino_y=entrada_parqueo+10,duration=duracion_colocacion)
            self.move_mouse(origen_x=x,origen_y=salida_parqueo,destiono_x=x+800,destino_y=salida_parqueo+100,duration=duracion_colocacion)
            self.move_mouse(origen_x=x,origen_y=parqueo_anexo,destiono_x=x+650,destino_y=parqueo_anexo+100,duration=duracion_colocacion)
            self.move_mouse(origen_x=x,origen_y=entrada_principal,destiono_x=x+450,destino_y=entrada_principal+100,duration=duracion_colocacion)
            pyi.moveTo(x,entrada_principal,duration=3)
            #pyi.hscroll(300)
            #TODO: Falta un paso
            
            #-------Click a full screen-----
            location_full_screen=pyi.locateOnScreen(self.path+"step3.2.png",confidence=0.9)
            pyi.moveTo(location_full_screen,duration=4)
            return True
        except Exception as ex:
            return False
       
    def move_mouse(self,origen_x,origen_y,destiono_x,destino_y,duration):
            """Esto agarra mueve y suelta el mouse

            Args:
                origen_x (_type_): origen del eje x
                origen_y (_type_): origen del eje y
                destiono_x (_type_): el destino x
                destino_y (_type_): el destino y
                duration (_type_): duracion de ejecucion
            """        
            pyi.mouseDown(origen_x, origen_y)#agarra
            pyi.moveTo(destiono_x,destino_y,duration=duration)#mueve
            pyi.mouseUp()#suelta