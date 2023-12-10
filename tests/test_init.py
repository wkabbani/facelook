from facelook import hello_world


def test_hello_world(capsys):
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == 'This is facelook package!\n'
    assert captured.err == ''
