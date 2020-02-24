import pyautogui
import time

imagensBaixadas = 222

def goBackArrow():
    # if isOnHomePage():
    #     return
    
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

def saved():
    if isOnHomePage():
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
    print("Procurando downloading")

    contador = 5
    donwloadingOBJ = pyautogui.locateOnScreen('downloading.png', grayscale = True, confidence=.9)
    while donwloadingOBJ == None and contador > 0:
        time.sleep(1)
        donwloadingOBJ = pyautogui.locateOnScreen('downloading.png', grayscale = True, confidence=.9)
        contador -= 1

    if donwloadingOBJ != None:
        print("Downloading achado. Esperando terminar...")

        contador = 120
        donwloadingOBJ = pyautogui.locateOnScreen('downloading.png', grayscale = True, confidence=.9)
        while donwloadingOBJ != None and contador > 0:
            time.sleep(1)
            donwloadingOBJ = pyautogui.locateOnScreen('downloading.png', grayscale = True, confidence=.9)
            contador -= 1
        print("Download terminado em", 120 - contador, "tentativas.")
    print("Download terminado. Prosseguindo...")
    time.sleep(2)
    # saveToGalerry()
    print("SAVETOGALERRY")


def unlock():
    print("Procurando unlock")

    contador = 5
    unlockOnly = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.9)
    while unlockOnly == None and contador > 0:
        time.sleep(1)
        unlockOnly = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.9)
        contador -= 1
    if unlockOnly == None:
        print("Não foi possivel achar o Unlock. Reiniciando...")
        time.sleep(1)
        centralize()
        return

    print("unlock Achado")
    buttonx, buttony = pyautogui.center(unlockOnly)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)
    time.sleep(0.5)
    downloading()

def unlockForFree():
    if not isLocked():
        print("Esta imagem já esta desbloqueada, voltando para o inicio...")
        time.sleep(0.7)
        goBackArrow()
        return

    print("Procurando UnlockForFree")
    unlockForF = pyautogui.locateOnScreen('unlockForFree.png', grayscale = True, confidence=.9)

    contador = 5
    while unlockForF == None and contador > 0:
        time.sleep(1)
        unlockForF = pyautogui.locateOnScreen('unlockForFree.png', grayscale = True, confidence=.9)
        contador -= 1

    if unlockForF == None:
        print("Não foi possivel achar o UnlockForFree. Voltando para o inicio...")
        time.sleep(1)
        goBackArrow()
        return

    print("UnlockForFree Achado")
    buttonx, buttony = pyautogui.center(unlockForF)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)
    time.sleep(1)
    contador = 5
    unlockOnly = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.9)
    while unlockOnly == None and contador > 0:
        time.sleep(1)
        pyautogui.click(buttonx, buttony)
        unlockOnly = pyautogui.locateOnScreen('unlock.png', grayscale = True, confidence=.9)
        contador -= 1
    if unlockOnly == None:
        print("Não foi possivel achar o Unlock. Voltando para o inicio...")
        time.sleep(1)
        goBackArrow()
        return
    time.sleep(1)
    unlock()


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

def clickOnNextImage():
    print("Procurando por proxima imagem")
    lock = pyautogui.locateOnScreen('lock.png', grayscale = True, confidence=.95)
    if lock == None:
        print("Nenhuma imagem encontrada. Rolando para baixo...")
        pyautogui.scroll(-1)
        time.sleep(1)
        clickOnNextImage()
        return
    print("Imagem encontrada")
    buttonx, buttony = pyautogui.center(lock)
    if buttony > 950:
        print("A Imagem esta muito abaixo. Rolando para baixo...")
        pyautogui.scroll(-1)
        time.sleep(1)
        clickOnNextImage()
        return
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)
    time.sleep(2)
    unlockForFree()

def centralize():
    print("Centralizando")
    popular = pyautogui.locateOnScreen('popular.png', grayscale = True, confidence=.9)
    if popular == None:
        time.sleep(1)
        print("Popular não achado")
        centralize()
        return

    print("Popular achado")
    buttonx, buttony = pyautogui.center(popular)
    pyautogui.moveTo(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.click(buttonx, buttony)
    time.sleep(0.5)
    pyautogui.moveTo(buttonx, buttony + 100)
    time.sleep(1)
    clickOnNextImage()

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
centralize()
# lock()
# saved()
