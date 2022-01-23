import contextlib
import tempfile

from merge_sorted_files.reader import IntReader


@contextlib.contextmanager
def temp_file(s: str):
    with tempfile.TemporaryFile("w+") as fp:
        fp.write(s)
        fp.seek(0)
        yield fp


def test_correct_file():
    with temp_file("1204\n11\n294\n2302") as fp:
        nums = list(IntReader(fp))
        assert nums == [1204, 11, 294, 2302]


def test_windows_file():
    with temp_file("102\r\n11\r\n355") as fp:
        nums = list(IntReader(fp))
        assert nums == [102, 11, 355]


def test_skip_incorrect_lines():
    with temp_file("12\nO,..,O\nboo1112haha\n1124") as fp:
        nums = list(IntReader(fp))
        assert nums == [12, 1124]


def test_empty_lines():
    with temp_file("12\n\n\n107\n") as fp:
        nums = list(IntReader(fp))
        assert nums == [12, 107]
