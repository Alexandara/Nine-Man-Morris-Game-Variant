import io
import pytest
from _pytest.monkeypatch import MonkeyPatch
import sys
sys.path.append("../morris_game")

from morris_game.morris_game import MorrisGame

@pytest.fixture
def create_morris():
    morris = MorrisGame()
    return morris
def test_count_piece(create_morris):
    morris = create_morris
    morris.player_color = "W"
    count_w = morris.count_piece("W",['B', 'W', 'B', 'W', 'B', 'W', 'x', 'B', 'x', 'x',
                        'W', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])
    count_b = morris.count_piece("B", ['B', 'W', 'B', 'W', 'B', 'W', 'x', 'B', 'x', 'x',
                                     'W', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])
    assert count_w == 4
    assert count_b == 4

def test_static_estimate(create_morris):
    morris = create_morris
    morris.game_stage = "o"
    est = morris.static_estimation(['B', 'W', 'B', 'W', 'B', 'W', 'x', 'B', 'x', 'x',
                        'W', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'])
    assert est == 0
