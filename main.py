import random

import pyautogui
import time

# Установите время, в течение которого мышь должна быть неактивна в секундах
INACTIVE_TIME = 5 * 60  # 5 минут

# Получите текущие координаты мыши
current_x, current_y = pyautogui.position()

# Установите время последнего движения мыши
last_active_time = time.time()

while True:
    # Проверьте, прошло ли достаточно времени с момента последнего движения мыши
    if time.time() - last_active_time > INACTIVE_TIME:
        # Если мышь была неактивна достаточно долго, переместите ее на случайное место экрана
        current_x, current_y = pyautogui.position()
        x, y = current_x + random.randint(-10, 10), current_y + random.randint(-10, 10)
        pyautogui.moveTo(x, y)
        pyautogui.click(button='right')
        print(f"Движения не было {INACTIVE_TIME / 60} минут, мышка перемещена ({x}, {y})")

        # Обновите время последнего движения мыши
        last_active_time = time.time()

    # Проверьте, было ли движение мыши
    if pyautogui.position() != (current_x, current_y):
        # Если мышь двигалась, обновите текущие координаты мыши
        current_x, current_y = pyautogui.position()

        # Обновите время последнего движения мыши
        last_active_time = time.time()

    # Подождите некоторое время перед повторной проверкой
    time.sleep(1)
