from interfaces.InterfaceStep import Interface_step
import pyautogui as pyi
import time as setTime
class Step2(Interface_step):
    def __init__(self, path):
        super().__init__(path)
        self.path = path;
    def run(self) -> bool:
        """
        Este paso abre el menu de camaras de esperanza
        """       
        try:
            location =pyi.locateOnScreen(self.path+"step2.png",confidence=0.9)
            bottom1 = pyi.locateOnScreen(self.path+"step2.1.png",confidence=0.9)
            
            pyi.moveTo(location,duration=3)
            setTime.sleep(4)
            pyi.moveTo(bottom1,duration=3)
            pyi.click(bottom1)

            x,y = location.left, location.top

            
            return True
        except Exception as ex:
            return False
       