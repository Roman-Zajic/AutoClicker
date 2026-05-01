import time
import pyautogui

pyautogui.FAILSAFE = True  # Move mouse to corner to abort

def click(x=None, y=None, button="left"):
    """
    Click at specific screen coordinates.
    If x and y are not provided, clicks the current mouse location.
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
    try:
        location = pyautogui.locateCenterOnScreen(template, confidence=confidence)
        return (location.x, location.y) if location else None
    except pyautogui.ImageNotFoundException:
        return None


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

        sleep(interval)

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