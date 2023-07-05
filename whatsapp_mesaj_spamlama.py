import time
import pyautogui

# WhatsApp uygulamasını etkinleştirme
pyautogui.press('win')
time.sleep(1)
pyautogui.write('WhatsApp', interval=0.1)
pyautogui.press('enter')
time.sleep(2)

# Hedef kişinin numarasını seçme
target = "telefon numarası girin"

# Mesaj gönderme işlemi
count = 1000
number = 1

# Hedef kişinin profiline girme
pyautogui.hotkey('ctrl', 'l')
time.sleep(1)
pyautogui.write(target, interval=0.1)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)
pyautogui.press('enter')

# Mesaj gönderme işlemi
for i in range(count):
    message = str(number)
    pyautogui.typewrite(message, interval=0.05)
    pyautogui.press('enter')
    time.sleep(0.5)
    number += 1
