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
    healthy_member_count=get_healthy_member_count()
    print(healthy_member_count)


def is_my_turn():
    try:
        pyautogui.locateOnScreen("img/quick_selection.png",  confidence=0.95, region=window_region)
        return True
    except pyautogui.ImageNotFoundException:
        return False

def is_on_field():
    try:
        pyautogui.locateOnScreen("img/camp.png",  confidence=0.95, region=window_region)
        return True
    except pyautogui.ImageNotFoundException:
        return False
def get_healthy_member_count():
    return len(list(pyautogui.locateAllOnScreen("img/hp_bar.png", confidence=0.97, region=window_region)))

def is_healthy():
    return healthy_member_count==get_healthy_member_count()

#pyautogui.click("img/test.png")

def main():
    init()

    while window.isActive:
        if is_my_turn():
            pyautogui.typewrite(["ctrlleft", "enter"], interval=1)
        elif is_on_field():
            if is_healthy():
                pyautogui.press('space')
            else:
                break

if __name__ == '__main__':
    main()