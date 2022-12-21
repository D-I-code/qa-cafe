from validation import *

def test_input_name_success(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "Mark")
        i = input_name()
        assert i == "mark"


def test_input_drink_success(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        i = input_drink()
        assert i == "latte"


def test_input_size_success(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "0")
        i = input_size()
        assert i == "small"


def test_input_extras_success(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "0")
        i = input_extras()
        assert i == "none"


def test_input_id_success(monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: "1")
        i = input_id()
        assert i == "1"


def test_input_id_letter(monkeypatch):
        inputs = iter(['a', '1'])
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        i = input_id()
        assert i == "1"