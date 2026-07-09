#ifndef ARG_MATCH_H
#define ARG_MATCH_H

#include <string.h>

void arg_pop(int *argc, char *argv[], int index)
{
  for (int i=index; i<*argc; i++) argv[i] = argv[i+1];

  (*argc)--;
  argv[*argc] = NULL;
}

// fn for match 1 options with argv
// 1 = matched
// 0 = not matched
int arg_match_opt(int *argc, char *argv[], const char *opt)
{
  for (int i=1; i<*argc; i++)
  {
    if (!strcmp(argv[i], opt)) { arg_pop(argc, argv, i); return 1;}
  }
  return 0;
}

// fn for match options with argv
// 1 = matched
// 0 = not matched
int arg_match_opts(int *argc, char *argv[], const char *opts[])
{
  for (int i=1; i<*argc; i++)
  {
    for (int j=0; opts[j] != NULL; j++) {
      if (!strcmp(argv[i], opts[j])) { arg_pop(argc, argv, i); return 1; }
    }
  }
  return 0;
}


// fn for option with value
// 1 = matched
// 0 = not matched
// -1 = matched but value not there
int arg_match_opt_with_value(int *argc, char *argv[], const char *opt, const char *value)
{
  for (int i=1; i<*argc; i++)
  {
    if (!strcmp(argv[i], opt)) {
      if (i + 1 >= *argc) return -1;
      if (!strcmp(argv[i+1], value)) {
        // pop shift
        int rem = *argc - i - 2;
        for (int m=0; m<rem; m++) argv[i + m] = argv[i + m + 2];
        *argc -= 2;
        argv[*argc] = NULL;
        return 1;
      }
    }
  }
  return 0;
}

// fn for options with values
// 1 = matched
// 0 = not matched
// -1 = matched but value not there
int arg_match_opts_with_value(int *argc, char *argv[], const char *opts[], const char *values[])
{
  for (int i=1; i<*argc; i++)
  {
    for (int j=0; opts[j] != NULL; j++) {
      if (!strcmp(argv[i], opts[j])) {
        if (i + 1 >= *argc) return -1;
        for (int k=0; values[k] != NULL; k++) {
          if (!strcmp(argv[i+1], values[k])) {
            // pop: shift remaining element left by 2
            int rem = *argc - i - 2;
            for (int m=0; m<rem; m++) {
              argv[i + m] = argv[i + m + 2];
            }
            *argc -= 2;
            // arg_pop(argc, argv, i); return 1; 
          }
        }
      }
    }
  }
  return 0;
}

#endif
