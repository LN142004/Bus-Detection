from src.ocr import extract_text_from_image
from src.announce import announce

def test_text_extraction():
    text = extract_text_from_image("data/test_bus.jpg")
    assert isinstance(text, str)
    assert len(text) > 0

def test_announcement():
    try:
        announce("Bus number 88C is arriving.")
    except Exception as e:
        assert False, f"Announce failed: {e}"
