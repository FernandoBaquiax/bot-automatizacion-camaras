from interfaces.InterfaceStep import Interface_step
import pyautogui as pyi
import time as setTime

class Step4(Interface_step):
    def __init__(self, path):
        super().__init__(path)
        self.path = path;
    def run(self) -> bool:
        try:
            # location =pyi.locateOnScreen(self.path+"step2.png",confidence=0.9)
            # bottom1 = pyi.locateOnScreen(self.path+"step2.1.png",confidence=0.9)
            
            # pyi.moveTo(location)
            # setTime.sleep(4)
            # pyi.moveTo(bottom1)
            # pyi.click(bottom1)
            # #file = open("./camaraEsperanza.png")


            # #pyautogui.click('./image.png')


            # #pyi.moveTo(location)
            # x,y = location.left, location.top

            # pyi.mouseDown(x, y)  # Presiona el botón del mouse
            # pyi.moveTo(x + 300, y, duration=4)  # Lo mueve 200 píxeles a la derecha
            # pyi.mouseUp()
            # #pyautogui.hscroll(600)
            # #pyautogui.click()
            
            return True
        except Exception as ex:
            return False
       
       