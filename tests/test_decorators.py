import pytest

from src.decorators import log


def test_log_to_console_ok(capsys):
    @log
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3
    captured = capsys.readouterr()
    assert "my_function ok" in captured.out


def test_log_to_console_error(capsys):
    @log
    def boom(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        boom(1, 0)

    captured = capsys.readouterr()
    assert "boom error:" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_to_file_ok(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def my_function(x, y):
        return x + y

    assert my_function(1, 2) == 3
    content = log_file.read_text(encoding="utf-8")
    assert "my_function ok" in content


def test_log_to_file_error(tmp_path):
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def boom(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        boom(1, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "boom error:" in content
    assert "Inputs: (1, 0), {}" in content