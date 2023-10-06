import pyautogui

# width,heigth=pyautogui.size()

# print(width, heigth)
# print(pyautogui.position())
# pyautogui.moveTo(810,540,1.5)
# pyautogui.moveRel(200,0)


# pyautogui.click(100,100);pyautogui.typewrite('Hello World !!', interval=0.2)
pyautogui.click(100,100);pyautogui.typewrite(['a','b','left','left','X','Y'], interval=0.2)
pyautogui.press('f1')

pyautogui.hotkey('win','r')

pyautogui.screenshot('d:/screenshot_example.jpg')
pyautogui.locateCenterOnScreen('d:/screenshot_example.jpg')


