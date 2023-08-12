from main import sendString


def test_hello():
    assert sendString() == "Hello, World!"
