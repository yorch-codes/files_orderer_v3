
# File Orderer V3

A python script that automatically organizes files into folders based on their extension. This project is the third iteration of my file organizer. Unlike the original version build with `os` and `shutil` and the second version build with `pathlib`, this version uses `typer` for cleaner and more modern file management. 
---

## Features

* Organize files by extension
* Automatically create destination folders
* Validate user-provided directories
* Built with `typer`

---

## Tech Stack

* Python 3
* typer
* pathlib

---

## Installation

Clone the repository:

```bash
git clone git@github.com:yorch-codes/files_orderer_v3.git
cd files_orderer_v3
```

---

## Usage

Run the project:

```bash
# Add your directory path directly as an argument
python3 main.py /home/user/downloads
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
