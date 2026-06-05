from pathlib import Path

import typer

from app.organizer import organize_files

app = typer.Typer()


@app.command()
def organize(ruta: Path):
    """Verify if the directory exists and organize files."""
    if not ruta.is_dir():
        typer.echo("Invalid directory.")
        raise typer.Exit(code=1)

    organized_files = organize_files(ruta)

    if organized_files == 0:
        typer.echo("No files to organize.")
        raise typer.Exit(code=0)

    typer.echo(f"{organized_files} file(s) organized successfully.")


if __name__ == "__main__":
    app()
