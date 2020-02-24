import pyautogui
import time

imagensBaixadas = 222

def goBackArrow():
    if isOnHomePage():
        lock()
        return
    
    print("Procurando goBackArrow")
    element = pyautogui.locateOnScreen('goBackArrow.png', grayscale = True, confidence=.9)
    print(element)
    if element == None:
        time.sleep(2)
        goBackArrow()
        return

    print("goBackArrow Achado")
    buttonx, buttony = pyautogui.center(element)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)
    time.sleep(3)
    lock()

def saved():
    if isOnHomePage():
        lock()
        return

    print("Procurando saved")
    tentativas = 5
    savedAchado = False
    while tentativas > 0 and savedAchado == False:
        print("Tentativa:", 5 - tentativas + 1)
        element = pyautogui.locateOnScreen('saved.png', grayscale = True, confidence=.8)
        if element != None:
            savedAchado = True
        tentativas -= 1
        time.sleep(0.5)
    time.sleep(1.5)
    global imagensBaixadas
    imagensBaixadas = imagensBaixadas + 1
    print("-------IMAGENS BAIXADAS:", imagensBaixadas, "------------")
    goBackArrow()

def saveToGalerry():
    if isOnHomePage():
        lock()
        return

    print("Procurando saveToGalerry")
    element = pyautogui.locateOnScreen('saveToGalerry.png', grayscale = True, confidence=0.9)
    print(element)
    if element == None:
        time.sleep(1)
        saveToGalerry()
        return

    print("saveToGalerry Achado")
    buttonx, buttony = pyautogui.center(element)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(2)
    pyautogui.click(buttonx, buttony)
    time.sleep(2)
    saved()

def downloading():
    if isOnHomePage():
        lock()
        return

    print("Procurando downloading")
    tentativas = 5
    downloadingAchado = False
    while tentativas > 0 and downloadingAchado == False:
        print("Tentativa:", tentativas)
        element = pyautogui.locateOnScreen('downloading.png', grayscale = True, confidence=.8)
        if element != None:
            downloadingAchado = True

        tentativas -= 1
        time.sleep(1)

    time.sleep(2)
    tentativas = 120
    while tentativas > 0:
        element = pyautogui.locateOnScreen('downloading.png', grayscale = True, confidence=.8)
        if element == None:
            break
        print("downloading Achado. Esperando...")
        tentativas -= 1
        time.sleep(1)
    time.sleep(2)
    saveToGalerry()


def unlock():
    if isOnHomePage():
        lock()
        return
    
    print("Procurando unlock")
    element = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.8)
    print(element)
    if element == None:
        time.sleep(1)
        unlock()
        return

    print("unlock Achado")
    buttonx, buttony = pyautogui.center(element)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)
    time.sleep(3)
    downloading()

def unlockForFree():
    if not isLocked():
        print("Esta imagem já esta desbloqueada, mudando para proxima...")
        pyautogui.press('right')
        time.sleep(0.7)
        unlockForFree()
        return

    print("Procurando UnlockForFree")
    unlockForF = pyautogui.locateOnScreen('unlockForFree.png', grayscale = True, confidence=.9)

    contador = 5
    while unlockForF == None and contador > 0:
        time.sleep(1)
        unlockForF = pyautogui.locateOnScreen('unlockForFree.png', grayscale = True, confidence=.9)
        contador -= 1

    if unlockForF == None:
        print("Não foi possivel achar o UnlockForFree. Reiniciando...")
        time.sleep(1)
        centralizeAndFocus()
        return

    print("UnlockForFree Achado")
    buttonx, buttony = pyautogui.center(unlockForF)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)

    contador = 5
    unlockOnly = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.9)
    while unlockOnly == None and contador > 0:
        time.sleep(1)
        pyautogui.click(buttonx, buttony)
        unlockOnly = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.9)
        contador -= 1
    if unlockOnly == None:
        print("Não foi possivel achar o Unlock. Reiniciando...")
        time.sleep(1)
        centralizeAndFocus()
        return

    # unlock()
    print("UNLOCK")

# def lock():
#     print("Procurando Lock")
#     pyautogui.moveTo(550, 550)
#     element = pyautogui.locateOnScreen('lock.png', grayscale = True, confidence=.95)
#     print(element)
#     if element == None:
#         pyautogui.scroll(-1)
#         time.sleep(1)
#         lock()
#         return

#     buttonx, buttony = pyautogui.center(element)
#     if buttony > 950:
#         print("Lock Muito Abaixo")
#         pyautogui.scroll(-1)
#         time.sleep(1)
#         lock()
#         return
#     print("Lock Achado")
#     pyautogui.moveTo(buttonx, buttony)
#     time.sleep(0.5)
#     pyautogui.click(buttonx, buttony)
#     time.sleep(2)
#     unlockForFree()



def centralizeAndFocus():
    print("Procurando goBackArrow")
    arrow = pyautogui.locateOnScreen('goBackArrow.png', grayscale = True, confidence=.9)
    if arrow == None:
        time.sleep(1)
        print("goBackArrow não achado")
        goBackArrow()
        return

    print("goBackArrow achado")
    buttonx, buttony = pyautogui.center(arrow)
    pyautogui.moveTo(buttonx + 200, buttony + 100)
    time.sleep(0.5)
    pyautogui.click(buttonx + 200, buttony + 100)
    time.sleep(1)
    unlockForFree()

def isLocked():
    setWallPaper = pyautogui.locateOnScreen('setWallPaper.png', grayscale = True, confidence=.95)
    if setWallPaper != None:
        return False
    else:
        return True

def isOnHomePage():
    element2 = pyautogui.locateOnScreen('popular.png', grayscale = True, confidence=.95)
    if element2 == None:
        return False
    else:
        return True

def isOnImagePage():
    element3 = pyautogui.locateOnScreen('goBackArrow.png', grayscale = True, confidence=.8)
    if element3 == None:
        return False
    else:
        return True

print("Iniciando Programa...")
time.sleep(4)
print("Programa Iniciado")
centralizeAndFocus()
# lock()
# saved()
