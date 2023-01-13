import time
import digitalio
import board
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

keyboard = Keyboard(usb_hid.devices)
#--------F2----------
btnF2 = board.GP15

btnF2 = board.GP15
btnF2 = digitalio.DigitalInOut(btnF2)
btnF2.direction = digitalio.Direction.INPUT
btnF2.pull = digitalio.Pull.DOWN
#---------F3---------
btnF3 = board.GP13

btnF3 = board.GP13
btnF3 = digitalio.DigitalInOut(btnF3)
btnF3.direction = digitalio.Direction.INPUT
btnF3.pull = digitalio.Pull.DOWN
#---------F4---------
btnF4 = board.GP18

btnF4 = board.GP18
btnF4 = digitalio.DigitalInOut(btnF4)
btnF4.direction = digitalio.Direction.INPUT
btnF4.pull = digitalio.Pull.DOWN
#---------F5---------
btnF5 = board.GP14

btnF5 = board.GP14
btnF5 = digitalio.DigitalInOut(btnF5)
btnF5.direction = digitalio.Direction.INPUT
btnF5.pull = digitalio.Pull.DOWN
#----------ESC-------
btnESC = board.GP17

btnESC = board.GP17
btnESC = digitalio.DigitalInOut(btnESC)
btnESC.direction = digitalio.Direction.INPUT
btnESC.pull = digitalio.Pull.DOWN
#----------TILDA-----
btnTIL = board.GP16

btnTIL = board.GP16
btnTIL = digitalio.DigitalInOut(btnTIL)
btnTIL.direction = digitalio.Direction.INPUT
btnTIL.pull = digitalio.Pull.DOWN

def msg():#istediğiniz mesaj için Keycode.() kısımlarını değiştiriniz.
    keyboard.press(Keycode.L)
    time.sleep(0.01)
    keyboard.release(Keycode.L)
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)
        
    keyboard.press(Keycode.O)
    time.sleep(0.01)
    keyboard.release(Keycode.O)
    
    keyboard.press(Keycode.N)
    time.sleep(0.01)
    keyboard.release(Keycode.N)
    
    keyboard.press(Keycode.S)
    time.sleep(0.01)
    keyboard.release(Keycode.S)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)
    
    keyboard.press(Keycode.N)
    time.sleep(0.01)
    keyboard.release(Keycode.N)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.A)
    time.sleep(0.01)
    keyboard.release(Keycode.A)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.C)
    time.sleep(0.01)
    keyboard.release(Keycode.C)
    
    keyboard.press(Keycode.A)
    time.sleep(0.01)
    keyboard.release(Keycode.A)
    
    
    keyboard.press(Keycode.G)
    time.sleep(0.01)
    keyboard.release(Keycode.G)
    
    keyboard.press(Keycode.E)
    time.sleep(0.01)
    keyboard.release(Keycode.E)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    keyboard.press(Keycode.C)
    time.sleep(0.01)
    keyboard.release(Keycode.C)
    
    keyboard.press(Keycode.O)
    time.sleep(0.01)
    keyboard.release(Keycode.O)
    
    keyboard.press(Keycode.K)
    time.sleep(0.01)
    keyboard.release(Keycode.K)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)
    
    keyboard.press(Keycode.Y)
    time.sleep(0.01)
    keyboard.release(Keycode.Y)
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.S)
    time.sleep(0.01)
    keyboard.release(Keycode.S)
    
    keyboard.press(Keycode.A)
    time.sleep(0.01)
    keyboard.release(Keycode.A)
    
    keyboard.press(Keycode.R)
    time.sleep(0.01)
    keyboard.release(Keycode.R)
    
    keyboard.press(Keycode.K)
    time.sleep(0.01)
    keyboard.release(Keycode.K)
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.D)
    time.sleep(0.01)
    keyboard.release(Keycode.D)
    
    keyboard.press(Keycode.E)
    time.sleep(0.01)
    keyboard.release(Keycode.E)
    
    keyboard.press(Keycode.G)
    time.sleep(0.01)
    keyboard.release(Keycode.G)
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)
    
    keyboard.press(Keycode.L)
    time.sleep(0.01)
    keyboard.release(Keycode.L)
    
    keyboard.press(Keycode.SPACE)
    time.sleep(0.01)
    keyboard.release(Keycode.SPACE)
    time.sleep(0.01)
    
    
    keyboard.press(Keycode.M)
    time.sleep(0.01)
    keyboard.release(Keycode.M)
    
    keyboard.press(Keycode.I)
    time.sleep(0.01)
    keyboard.release(Keycode.I)

while True:
    if btnF2.value:
        print("buton F2 basıldı")
        msg()
        
        keyboard.press(Keycode.RETURN)
        time.sleep(0.01)
        keyboard.release(Keycode.RETURN)
        
    if btnF3.value:
#         time.sleep(2)
#         print("buton F3 basıldı")
#         keyboard.press(Keycode.COMMAND, Keycode.SPACE)
#         time.sleep(0.1)
#         keyboard.release(Keycode.COMMAND, Keycode.SPACE)
#         time.sleep(0.1)
#         
#         msg()
#          
#         for i in range(1,2):
#             keyboard.press(Keycode.DOWN_ARROW)
#             time.sleep(0.1)
#             keyboard.release(Keycode.DOWN_ARROW)
#          
#         keyboard.press(Keycode.RETURN)
#         time.sleep(0.1)
#         keyboard.release(Keycode.RETURN)
        
    if btnF4.value:
        print("buton F4 basıldı")
        #mesajı istediğiniz kadar tekrar ettirebilirsiniz
        for i in range(1,100): #range() içerisine girdiğiniz değer kadar kodu tekrar ettirir.
            msg()
            keyboard.press(Keycode.RETURN)
            time.sleep(0.01)
            keyboard.release(Keycode.RETURN)
            
    if btnF5.value:
        print("buton F5 basıldı")
        
    if btnESC.value:
        print("buton ESC basıldı")
        
    if btnTIL.value:
        print("buton TILDA basıldı")
        
    time.sleep(0.1)
