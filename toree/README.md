# toree

A simple directory tree viewer — a recursive practice project.

## What it does

Recursively walks a directory and prints its structure.

## Options

- `--layout <1|2|3>` — choose layout style
- `--help` — help message
- `--version` — version info

## Layouts

```
1: normal (default)
2: tree-style
3: xml
```

## get from source
```bash
git clone https://codeberg.org/6z7y/randoms
cd toree
```

## Usage

```bash
python3 src/main.py <path>
python3 src/main.py --layout 2 <path>
```

