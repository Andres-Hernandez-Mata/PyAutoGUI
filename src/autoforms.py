import pyautogui,time

F1 = "El misterio de la vida no es un problema a resolver, sino una realidad a experimentar"
F2 = "Tengo esperanza o podría no vivir"

C1 = "juanito123@gmail.com"
C2 = "panchito321@gmail.com"

i = 0
while i <= 2:
    i=i+1
    if i==1:
        #Pregunta1
        pyautogui.click(x=338, y=525, clicks=1)
        time.sleep(2)
        #Pregunta2
        pyautogui.click(x=347, y=707, clicks=1)
        pyautogui.typewrite(F1)
        time.sleep(2)
        pyautogui.press('tab')

        #Pregunta3
        pyautogui.click(x=384, y=440, clicks=1)
        time.sleep(1)
        pyautogui.click(x=398, y=636, clicks=1)
        time.sleep(2)
        #Pregunta4
        pyautogui.click(x=369, y=596, clicks=1)
        pyautogui.typewrite(C1)
        time.sleep(2)
        #Enviar
        pyautogui.click(x=355, y=687, clicks=1)
        time.sleep(3)

        #2 vez
        pyautogui.click(x=367, y=461, clicks=1)
    else:
        #Pregunta1
        pyautogui.click(x=335, y=444, clicks=1)
        time.sleep(2)
        #Pregunta2
        pyautogui.click(x=347, y=707, clicks=1)
        pyautogui.typewrite(F2)
        time.sleep(2)
        pyautogui.press('tab')

        #Pregunta3
        pyautogui.click(x=384, y=440, clicks=1)
        time.sleep(1)
        pyautogui.click(x=391, y=481, clicks=1)
        time.sleep(2)
        #Pregunta4
        pyautogui.click(x=369, y=596, clicks=1)
        pyautogui.typewrite(C2)
        time.sleep(2)
        #Enviar
        pyautogui.click(x=355, y=687, clicks=1)
        time.sleep(3)



