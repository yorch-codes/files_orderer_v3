
# File Orderer V3

A python script that automatically organizes files into folders based on their extension. This project is the third iteration of my file organizer. Unlike the original version build with `os` and `shutil` and the second version build only using `pathlib`, this new version uses `typer` with `pathlib` for cleaner and more modern file management. 
---

## Features

* Organize files by extension
* Automatically create destination folders
* Validate user-provided directories
* Built with `typer`

---

## Tech Stack

* Python 3.14
* pathlib
* typer
* pytest

---

## Installation

Clone the repository:

```bash
git clone git@github.com:yorch-codes/files_orderer_v3.git
cd files_orderer_v3
```

---

## Create environment and install dependencies:

### Using uv

```bash
# Create environment with uv
uv venv
```

```bash
# Use uv to install dependencies
uv pip install -r requirements.txt
```

### Using pip

```bash
# Create environment with pip in windows
python -m venv venv
```

```bash
# Create environment with pip in linux/macOS
python3 -m venv venv
```

```bash
# Use pip to install dependencies
pip install -r requirements.txt
```

---

## Usage

Run the project:

```bash
# Run the application in windows
# Add your directory path directly as an argument
python main.py /home/user/downloads
```

```bash
# Run the application in Linux/MacOS
# Add your directory path directly as an argument
python3 main.py /home/user/downloads
```

---

## Testing

Run the tests:

```bash
# Run the tests
pytest
```

---

## Project Structure

```text
project/
├── README.md
├── docs/
│   ├── planning.md
│   └── architecture.md
├── app/
│   ├── __init__.py
│   └── organizer.py
└── tests/
│   ├── __init__.py
│   └── test_main.py
├── main.py
└── .gitignore
```

---

## Documentation

Additional project documentation:

  * Planning → [Planning](docs/planning.md)
  * Architecture → [Architecture](docs/architecture.md)

---

## Roadmap

Planned improvements:

* [ ] Summary of moved files
* [ ] Dry-run mode
* [ ] Support for subdirectories
* [ ] Custom categories
* [ ] Configuration file

---

## License

MIT
