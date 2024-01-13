import pyautogui
import time

nexusBtn = 'nexus-download-btn.png'
siteBtn = 'site-btn.png'

while True:
    if pyautogui.locateOnScreen(nexusBtn, grayscale=False, confidence=.9):
        print('esta na tela nexusBtn')
        pyautogui.click(nexusBtn)
        time.sleep(10)
    else: 
        print('nao esta na tela nexusBtn')
        

    if pyautogui.locateOnScreen(siteBtn, grayscale=False, confidence=.9):
        pyautogui.click(siteBtn)
        time.sleep(15)
        pyautogui.hotkey("ctrlleft", "w")
    else:
        print('não esta na tela siteBtn')




# debug
# src=pyautogui.locateOnScreen(nexusBtn, grayscale=False, confidence=.9)
# print(src)
# im = pyautogui.screenshot(region=(1051, 346, 59, 20))
# im.save('my_screenshot.png')
    