from interfaces.InterfaceStep import Interface_step
import pyautogui as pyi

class Step1(Interface_step):
    def __init__(self, path):
        super().__init__(path)
        self.path = path;
    def run(self) -> bool:
        """
        Este paso da click en las camaras
        """       
        try:
            location =pyi.locateOnScreen(self.path+"step1.png",confidence=0.9)
            
            print(location)
            pyi.moveTo(location,duration=3)
            
            pyi.click(location)

            x,y = location.left, location.top

            return True
        except Exception as ex:
            return False
       