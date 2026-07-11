# Arg match

A small single-header C for parsing command-line arguments
is header file for argument matched

##functions 

These functions only check arguments without modify 'argv'
- `arg_check_opt` — check a single option.
- `arg_check_opts` — check one of multiple options.
- `arg_check_opt_with_value` — check a single option followed by a value.
- `arg_check_opts_with_value` — check one of multiple options followed by a value.

These functions matched arguments and remove them from 'argv'
- `arg_match_opt` — Match a single option.
- `arg_match_opts` — Match one of multiple options.
- `arg_match_opt_with_value` — Match a single option followed by a value.
- `arg_match_opts_with_value` — Match one of multiple options followed by a value.

## Example

```c
if (arg_match_opt(&argc, argv, "--help") == 1) {
    /* Handle --help */
}


const char *opts[] = {"-s", "--silent"};
if (arg_match_opts(&argc, argv, opts) == 1) {
    /* Handle -s or --silent */
}
```
