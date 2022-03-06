import pytest
from .tetris_utils import Board, detect_end, map_to_pixel


@pytest.mark.parametrize(
    "map_x,map_y,expected_pixel_x,expected_pixel_y",
    [
        (0, 0, 0, 0),
        (1, 0, 22, 0),
        (0, 1, 0, 22),
        (1, 1, 22, 22),
        (2, 2, 44, 44),
        (2, 0, 44, 0),
        (0, 2, 0, 44),
    ],
)
def test_map_to_pixel(map_x, map_y, expected_pixel_x, expected_pixel_y):
    """Test dat de conversie van map posities naar pixels werkt"""
    pixel_x, pixel_y = map_to_pixel(map_x, map_y)
    assert pixel_x == expected_pixel_x
    assert pixel_y == expected_pixel_y


def test_create_board_2x4_size():
    """Test dat bij het aanmaken van een bord de breedte en hoogte opgeslagen worden"""
    result = Board(2, 4)

    assert result.width == 2
    assert result.height == 4


def test_create_board_4x8_size():
    """Test dat bij het aanmaken van een bord de breedte en hoogte opgeslagen worden"""
    result = Board(4, 8)

    assert result.width == 4
    assert result.height == 8


def test_create_board_2x4_data():
    """Test dat bij het aanmaken van een bord de property data correct aangemaakt wordt"""
    result = Board(2, 4)
    expected = [
        [-1, -1],
        [-1, -1],
        [-1, -1],
        [-1, -1],
    ]
    assert result.data == expected


def test_create_board_4x8_data():
    """Test dat bij het aanmaken van een bord de property data correct aangemaakt wordt"""
    result = Board(4, 8)
    expected = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]
    assert result.data == expected


@pytest.mark.parametrize(
    "player_x,expected",
    [
        (0, False),
        (1, False),
        (100, False),
        (-1, True),
        (-2, True),
        (-3, True),
    ],
)
def test_edges_left_border(player_x, expected):
    """Test dat het buiten de linkerrand van het bord komen gedetecteerd wordt"""
    board = Board(3, 2)

    result = board.out_of_left_border(player_x)
    assert result is expected


@pytest.mark.parametrize(
    "player_y,expected",
    [
        (0, False),
        (1, False),
        (100, False),
        (-1, True),
        (-2, True),
        (-3, True),
    ],
)
def test_edges_top_border(player_y, expected):
    """Test dat het buiten de bovenrand van het bord komen gedetecteerd wordt"""
    board = Board(3, 2)

    result = board.out_of_top_border(player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,expected",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, True),
        (100, True),
        (-1, False),
        (-3, False),
    ],
)
def test_edges_right_border(player_x, expected):
    """Test dat het buiten de rechterrand van het bord komen gedetecteerd wordt"""
    board = Board(3, 2)
    shape = [[1, 1]]
    result = board.out_of_right_border(shape, player_x)
    assert result is expected


@pytest.mark.parametrize(
    "player_y,expected",
    [
        (0, False),
        (1, False),
        (2, True),
        (3, True),
        (4, True),
        (100, True),
        (-1, False),
        (-3, False),
    ],
)
def test_edges_bottom_border(player_y, expected):
    """Test dat het buiten de onderste rand van het bord komen gedetecteerd wordt"""
    board = Board(3, 3)
    shape = [[1], [1]]
    result = board.out_of_bottom_border(shape, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, False),
        (1, 0, False),
        (0, 1, False),
        (1, 1, False),
        (2, 0, True),
        (3, 0, True),
        (2, 1, True),
        (0, 2, True),
        (1, 2, True),
        (2, 2, True),
        (3, 2, True),
        (-1, 0, True),
        (-1, 1, True),
        (-2, 1, True),
    ],
)
def test_edges_two_blocks(player_x, player_y, expected):
    """Test dat het buiten de rand van het bord komen gedetecteerd wordt"""
    board = Board(3, 2)
    shape = [[1, 1]]

    result = board.out_of_border(shape, player_x, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, False),
        (0, 1, False),
        (0, 2, True),
        (1, 0, True),
        (1, 1, True),
        (1, 2, True),
        (2, 0, True),
        (2, 1, True),
        (2, 2, True),
        (3, 0, True),
        (3, 1, True),
        (3, 2, True),
    ],
)
def test_edges_shape_i(player_x, player_y, expected):
    """Test dat het buiten de rand van het bord komen gedetecteerd wordt"""
    board = Board(4, 2)
    shape = [[1, 1, 1, 1]]

    result = board.out_of_border(shape, player_x, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, False),
        (1, 0, False),
        (2, 0, False),
        (3, 0, True),
        (0, 1, True),
        (1, 1, True),
        (2, 1, False),
        (3, 1, True),
        (0, 2, True),
        (1, 2, True),
        (2, 2, True),
        (3, 2, True),
    ],
)
def test_detect_collision_shape_o(player_x, player_y, expected):
    """Test dat het botsen met reeds geplaatste blokken gedetecteerd wordt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, +2],
        [+2, +2, -1, -1, +2],
        [+2, +2, +2, +2, +3],
    ]
    shape = [[1, 1], [1, 1]]

    result = board.check_collision(shape, player_x, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, False),
        (0, 1, False),
        (0, 2, False),
        (0, 3, True),
        (1, 0, False),
        (1, 1, False),
        (1, 2, True),
        (1, 3, True),
        (2, 0, False),
        (2, 1, True),
        (2, 2, True),
        (2, 3, True),
        (3, 0, False),
        (3, 1, True),
        (3, 2, True),
        (3, 3, True),
        (4, 0, False),
        (4, 1, True),
        (4, 2, True),
        (4, 3, True),
        (5, 0, False),
        (5, 1, False),
        (5, 2, False),
        (5, 3, True),
    ],
)
def test_detect_collision_shape_o2(player_x, player_y, expected):
    """Test dat het botsen met reeds geplaatste blokken gedetecteerd wordt"""
    board = Board(7, 4)
    board.data = [
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, +3, +3, -1, -1],
        [-1, -1, +3, +3, -1, -1, -1],
    ]
    shape = [[1, 1], [1, 1]]

    result = board.check_collision(shape, player_x, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, False),
        (1, 0, False),
        (2, 0, True),
        (3, 0, True),
        (0, 1, False),
        (1, 1, True),
        (2, 1, True),
        (3, 1, True),
        (0, 2, True),
        (1, 2, True),
        (2, 2, True),
        (3, 2, True),
    ],
)
def test_detect_collision_shape_i_0(player_x, player_y, expected):
    """Test dat het botsen met reeds geplaatste blokken gedetecteerd wordt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, +2],
        [+2, +2, -1, -1, +2],
        [+2, +2, +2, +2, +3],
    ]
    shape = [[1, 1, 1, 1]]

    result = board.check_collision(shape, player_x, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, True),
        (1, 0, True),
        (2, 0, False),
        (3, 0, True),
        (0, 1, True),
        (1, 1, True),
        (2, 1, True),
        (3, 1, True),
        (0, 2, True),
        (1, 2, True),
        (2, 2, True),
        (3, 2, True),
    ],
)
def test_detect_collision_shape_i_1(player_x, player_y, expected):
    """Test dat het botsen met reeds geplaatste blokken gedetecteerd wordt"""
    board = Board(5, 5)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, +2],
        [+2, +2, -1, -1, +2],
        [+2, +2, -1, +2, +3],
        [+2, +2, +2, +2, +3],
    ]
    shape = [[1], [1], [1], [1]]

    result = board.check_collision(shape, player_x, player_y)
    assert result is expected


@pytest.mark.parametrize(
    "player_x,player_y,expected",
    [
        (0, 0, True),
        (1, 0, True),
        (2, 0, False),
        (3, 0, True),
        (0, 1, True),
        (1, 1, True),
        (2, 1, True),
        (3, 1, True),
        (0, 2, True),
        (1, 2, True),
        (2, 2, True),
        (3, 2, True),
    ],
)
def test_check_move_illegal_shape_i_1(player_x, player_y, expected):
    """Test dat het botsen met reeds geplaatste blokken gedetecteerd wordt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, +2],
        [+2, +2, -1, -1, +2],
        [+2, +2, -1, +2, +3],
    ]
    shape = [[1], [1], [1], [1]]

    result = board.check_move_illegal(shape, player_x, player_y)
    assert result is expected


def test_copy_shape_0():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(2, 1)
    board.data = [
        [-1, -1],
    ]
    shape = [[1, 1]]

    board.copy_shape(shape, 0, 0, 4)
    expected = [
        [4, 4],
    ]
    assert board.data == expected


def test_copy_shape_10():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(2, 2)
    board.data = [
        [-1, -1],
        [-1, -1],
    ]
    shape = [[1, 1]]

    board.copy_shape(shape, 0, 0, 5)
    expected = [
        [+5, +5],
        [-1, -1],
    ]
    assert board.data == expected


def test_copy_shape_20():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(2, 2)
    board.data = [
        [-1, -1],
        [-1, -1],
    ]
    shape = [[1, 1]]

    board.copy_shape(shape, 0, 1, 6)
    expected = [
        [-1, -1],
        [+6, +6],
    ]
    assert board.data == expected


def test_copy_shape_30():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(2, 2)
    board.data = [
        [-1, -1],
        [-1, -1],
    ]
    shape = [[1], [1]]

    board.copy_shape(shape, 0, 0, 7)
    expected = [
        [7, -1],
        [7, -1],
    ]
    assert board.data == expected


def test_copy_shape_40():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(2, 2)
    board.data = [
        [-1, -1],
        [-1, -1],
    ]
    shape = [[1], [1]]

    board.copy_shape(shape, 1, 0, 4)
    expected = [
        [-1, 4],
        [-1, 4],
    ]
    assert board.data == expected


def test_copy_shape_50():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(4, 2)
    board.data = [
        [-1, -1, -1, -1],
        [-1, -1, -1, -1],
    ]
    shape = [[1, 1, 1, 1]]

    board.copy_shape(shape, 0, 0, 5)
    expected = [
        [+5, +5, +5, +5],
        [-1, -1, -1, -1],
    ]
    assert board.data == expected


def test_copy_shape_60():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    shape = [[1], [1], [1], [1]]

    board.copy_shape(shape, 0, 0, 6)
    expected = [
        [6, -1, -1, -1, -1],
        [6, -1, -1, -1, -1],
        [6, -1, -1, -1, -1],
        [6, -1, -1, -1, -1],
    ]
    assert board.data == expected


def test_copy_shape_70():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    shape = [[1, 1], [1, 1]]

    board.copy_shape(shape, 0, 0, 6)
    expected = [
        [+6, +6, -1, -1, -1],
        [+6, +6, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    assert board.data == expected


def test_copy_shape_80():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    shape = [[1, 1], [1, 1]]

    board.copy_shape(shape, 1, 1, 6)
    expected = [
        [-1, -1, -1, -1, -1],
        [-1, +6, +6, -1, -1],
        [-1, +6, +6, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    assert board.data == expected


def test_copy_shape_90():
    """Test dat het plaatsen van een blok werkt"""
    board = Board(5, 4)
    board.data = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
    ]
    shape = [[1, 1], [1, 1]]

    board.copy_shape(shape, 3, 2, 4)
    expected = [
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1],
        [-1, -1, -1, +4, +4],
        [-1, -1, -1, +4, +4],
    ]
    assert board.data == expected


def test_remove_full_rows_empty():
    """Test dat het verwijderen van volle rijen werkt, in dit geval is er geen volle rij"""
    board = Board(3, 2)
    board.remove_full_rows()
    expected = [
        [-1, -1, -1],
        [-1, -1, -1],
    ]
    assert board.data == expected


def test_remove_full_rows_empty_points():
    """Test dat het verwijderen van volle rijen correct punten gegeven worden"""
    board = Board(3, 2)
    points = board.remove_full_rows()
    assert points == 0


def test_remove_full_rows_none_full():
    """Test dat het verwijderen van volle rijen werkt, in dit geval is er geen volle rij"""
    board = Board(3, 2)
    board.data = [
        [-1, -1, 1],
        [-1, 1, -1],
    ]
    board.remove_full_rows()
    expected = [
        [-1, -1, 1],
        [-1, 1, -1],
    ]
    assert board.data == expected


def test_remove_full_rows_none_full_points():
    """Test dat het verwijderen van volle rijen correct punten gegeven worden"""
    board = Board(3, 2)
    board.data = [
        [-1, -1, 1],
        [-1, 1, -1],
    ]
    points = board.remove_full_rows()

    assert points == 0


def test_remove_full_rows_one_bottom_full():
    """Test dat het verwijderen van volle rijen werkt, in dit geval is er 1 volle rij onderaan"""
    board = Board(3, 2)
    board.data = [
        [-1, -1, 1],
        [1, 1, 1],
    ]
    board.remove_full_rows()
    expected = [
        [-1, -1, -1],
        [-1, -1, 1],
    ]
    assert board.data == expected


def test_remove_full_rows_one_bottom_full_points():
    """Test dat het verwijderen van volle rijen correct punten gegeven worden"""
    board = Board(3, 2)
    board.data = [
        [-1, -1, 1],
        [1, 1, 1],
    ]
    points = board.remove_full_rows()
    assert points == 100


def test_remove_full_rows_two_bottom_full():
    """Test dat het verwijderen van volle rijen werkt, in dit geval zijn er 2 volle rijen onderaan"""
    board = Board(3, 3)
    board.data = [
        [-1, -1, 1],
        [1, 1, 1],
        [1, 1, 1],
    ]
    board.remove_full_rows()
    expected = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, 1],
    ]
    assert board.data == expected


def test_remove_full_rows_one_middle_full():
    """Test dat het verwijderen van volle rijen werkt, in dit geval is er 1 volle rij in het midden"""
    board = Board(3, 3)
    board.data = [
        [-1, -1, 1],
        [1, 1, 1],
        [1, -1, 1],
    ]
    board.remove_full_rows()
    expected = [
        [-1, -1, -1],
        [-1, -1, 1],
        [1, -1, 1],
    ]
    assert board.data == expected


@pytest.mark.parametrize(
    "player_y,expected",
    [
        (0, True),
        (1, False),
        (2, False),
        (100, False),
    ],
)
def test_detect_end(player_y, expected):
    result = detect_end(player_y)
    assert result is expected