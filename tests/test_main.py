from pathlib import Path

from typer.testing import CliRunner

from app.organizer import organize_files
from main import app

runner = CliRunner()


# tests for organize_files
def test_organize_files(tmp_path: Path):
    """Test that organize_files correctly organizes files by extension."""
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"
    file3 = tmp_path / "c.py"

    file1.write_text("hello")
    file2.write_text("world")
    file3.write_text("print('hi')")

    result = organize_files(tmp_path)

    assert result == 3

    assert (tmp_path / "txt" / "a.txt").exists()
    assert (tmp_path / "txt" / "b.txt").exists()
    assert (tmp_path / "py" / "c.py").exists()


def test_ignores_directory(tmp_path):
    """Test that organize_files ignores directories."""
    d = tmp_path / "folder"
    d.mkdir()

    result = organize_files(tmp_path)

    assert result == 0
    assert d.exists()


def test_files_without_extension(tmp_path):
    """Test that organize_files moves files without extensions to the root."""
    file = tmp_path / "README"
    file.write_text("no ext")

    result = organize_files(tmp_path)

    assert result == 0
    assert file.exists()


def test_organize_invalid_directory(tmp_path):
    """Test that the app exits with an error when given an invalid directory."""
    result = runner.invoke(app, ["/this/path/does/not/exist"])
    assert result.exit_code != 0

    assert "Invalid directory." in result.output


# test for cli
def test_cli(tmp_path):
    file = tmp_path / "a.txt"
    file.write_text("hello")

    result = runner.invoke(app, [str(tmp_path)])

    assert result.exit_code == 0
    assert (tmp_path / "txt" / "a.txt").exists()
