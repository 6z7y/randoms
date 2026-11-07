# nconv

**nconv** is a simple command-line number system converter written in C.

## Build

Clone repo
```bash
git clone https://github.com/6z7y/randoms.git
cd randoms/nconv
```

Compile and install with `make`:

``` sh
sudo make install
```

-   `make uninstall` --- Remove the installed binary executable.

## Usage

``` sh
./nconv [OPTION] NUM
```

### Options

-   `--binary` --- Convert the number to binary.
-   `--hex` --- Convert the number to hexadecimal.
-   `--octal` --- Convert the number to octal.
-   `--help` --- Display the help message.
-   `--version` --- Display the program version.

If no conversion option is provided, nconv prints all three
representations.

## Examples

``` sh
./nconv --binary 512
./nconv --hex 255
./nconv --octal 64
./nconv 42
```
