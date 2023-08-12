from main import sendtext


def test_hello():
    assert sendtext() == "Hello, World!"
