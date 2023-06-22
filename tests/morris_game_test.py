import io
import pytest
from _pytest.monkeypatch import MonkeyPatch

from morris_game.morris_game import MorrisGame

@pytest.fixture
def create_morris():
    monkeypatch = MonkeyPatch()
    monkeypatch.setattr('sys.stdin', io.StringIO('w'))
    morris = MorrisGame()
    return morris
def test_print_board(create_morris):
    morris = create_morris
    morris.print_board()

