# PDF Creator from Kindle

This project captures screenshots of your Kindle and converts them into PDF files. It utilizes `pipenv` for dependency management and virtual environment setup.

## Requirements

- Python 3.12
- pipenv

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/pdf-creator.git
   cd pdf-creator-from-kindle
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   pipenv install
   ```

## Usage

Run the script with `pipenv` and provide the necessary arguments:

```bash
pipenv run python main.py -n output.pdf -p 5 -d right
```

### Arguments

- `-n` or `--pdf_name`: Name of the output PDF file (default: `output_{yyyymmdd}_{hhmmss}.pdf`)
- `-p` or `--page`: Number of pages to capture (default: 5)
- `-d` or `--direction`: Direction to turn pages (`left` or `right`, default: `right`)

### Virtual Environment Management

Activate the virtual environment:

```bash
pipenv shell
```

Exit the virtual environment:

```bash
exit
```

### Clean Up

Remove the virtual environment:

```bash
pipenv --rm
```

### Caution

Confirmed to work on Mac, but may not work on Windows.
