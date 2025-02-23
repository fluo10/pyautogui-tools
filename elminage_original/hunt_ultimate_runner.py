import pyautogui
import pywinctl
import time

WINDOW_TITLE="Proving Grounds of the Mad Overlord  "

pyautogui.useImageNotFoundException()

window=None
window_region=None
healthy_member_count=None

def init():
    global window
    global window_region
    global healthy_member_count

    window = pywinctl.getWindowsWithTitle(WINDOW_TITLE)[0]
    window_region=window.box
    
    print(window_region)
    window.activate()
    time.sleep(1)

def is_my_turn():
    try:
        pyautogui.locateOnScreen("img/enemy_icon.png",  confidence=0.95, region=window_region)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def exists_third_row_enemies():
    try:
        pyautogui.locateOnScreen("img/enemy_icon_last_row.png",  confidence=0.95, region=window_region)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def main():
    init()

    while window.isActive:
        if is_my_turn():
            if exists_third_row_enemies():
                pyautogui.typewrite(["enter", "enter", "enter", "enter", "enter", "enter"], interval=1)
            else:
                pyautogui.typewrite(["e"], interval=1)
        
        time.sleep(1)

if __name__ == '__main__':
    main()