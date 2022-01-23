import subprocess
import tempfile

from merge_sorted_files.reader import IntReader


def test_main():
    temp_file1 = tempfile.NamedTemporaryFile("w")
    temp_file2 = tempfile.NamedTemporaryFile("w")
    temp_file3 = tempfile.NamedTemporaryFile("w")

    temp_file1.write("124\n1045\n9999")
    temp_file2.write("2\n100000\n\n\n")
    temp_file3.write("70\n150")

    for f in [temp_file1, temp_file2, temp_file3]:
        f.flush()

    output_dir = tempfile.TemporaryDirectory()
    output_filename = f"{output_dir.name}/output"

    r = subprocess.run(
        ".venv/bin/python3 merge_sorted_files/main.py "
        f"{temp_file1.name} {temp_file2.name} {temp_file3.name} "
        f"{output_filename}",
        shell=True,
    )

    assert r.returncode == 0
    with open(output_filename, "r") as fp:
        result = list(IntReader(fp))

    assert result == [2, 70, 124, 150, 1045, 9999, 100000]
