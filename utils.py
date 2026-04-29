import time
import pyautogui

def click(x, y, button="left"):
    """
    Click at specific screen coordinates.
    """
    pyautogui.click(x=x, y=y, button=button)

def sleep(seconds):
    """
    Pause execution for given seconds.
    """
    time.sleep(seconds)

def is_image_visible(template, confidence=0.8):
    """
    Check if image is visible on screen.

    Returns:
        (x, y) if found, otherwise None
    """
    location = pyautogui.locateCenterOnScreen(template, confidence=confidence)
    return location  # None if not found


def wait_for_image(template, timeout=5, interval=0.2, confidence=0.8):
    """
    Wait until image appears on screen.

    Returns:
        (x, y) if found, otherwise None
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        location = is_image_visible(template, confidence)

        if location:
            return location

        time.sleep(interval)

    return None


def wait_click(template, timeout=5, interval=0.2, confidence=0.8):
    """
    Wait for image and click it.

    Returns:
        True if clicked, False if timeout
    """
    location = wait_for_image(template, timeout, interval, confidence)

    if location:
        x, y = location
        pyautogui.click(x, y)
        return True

    return False