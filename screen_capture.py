import base64
import io
import mss
from PIL import Image


def capture_screen(monitor_number: int = 1) -> str:
    """
    Capture the screen and return it as a base64-encoded string.

    Args:
        monitor_number: Which monitor to capture (1 = primary, 0 = all monitors)

    Returns:
        Base64-encoded PNG image string
    """
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_number]
        screenshot = sct.grab(monitor)

        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")

        buffer = io.BytesIO()
        img.save(buffer, format="PNG", optimize=True)
        buffer.seek(0)

        base64_image = base64.b64encode(buffer.read()).decode("utf-8")

        return base64_image


def capture_screen_to_file(filepath: str = "screenshot.png", monitor_number: int = 1) -> str:
    """
    Capture the screen and save it to a file.

    Args:
        filepath: Path to save the screenshot
        monitor_number: Which monitor to capture

    Returns:
        Path to the saved file
    """
    with mss.mss() as sct:
        monitor = sct.monitors[monitor_number]
        screenshot = sct.grab(monitor)

        img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")
        img.save(filepath, format="PNG")

        return filepath
