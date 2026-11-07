#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PROG_NAME "nconv"
#define PROG_VER "1.0.0"

 void
print_help(void)
{
  printf("nconv - Number System Converter\n"
         "===============================\n\n"
         "Usage:\n"
         "  nconv [OPTION] [NUM]\n\n"
         "Options:\n"
         "  -binary    Convert number to binary\n"
         "  -hex       Convert number to hexadecimal\n"
         "  -octal     Convert number to octal\n"
         "  -help      Display this help message\n\n"
         "Examples:\n"
         "  nconv -binary 512\n"
         "  nconv -hex 255\n"
         "  nconv -octal 64\n"
  );
}

 void
print_binary(unsigned long num)
{
  int bits = 8;
  // check if up
  while ((num >> bits) != 0)
  {
    bits +=8;
  }

  // Print
  printf("Binary: ");
  for (int i=bits - 1; i>=0; i--)
  {
    printf("%ld", (num >> i) & 1);

    if (i > 0 && i % 8 == 0) printf(" ");
  }
  printf("\n");
}

 void
print_hex(unsigned long num)
{
  printf("Hex: ");
  printf("%lX\n", num);
}

 void
print_octal(unsigned long num)
{
  printf("Octal: ");
  printf("%lo\n", num);
}


 int
main(int argc, char **argv)
{
  if (argc < 2) {
    fprintf(stderr, "usage: %s [OPTION] [NUM]\n", PROG_NAME);
    return -1;
  }
  char *option = argv[1];

  if (!strcmp(option, "--help")) {
    print_help();
    return 0;
  }
  else if (!strcmp(option, "--version")) {
    printf("%s: %s\n", PROG_NAME, PROG_VER);
    return 0;
  }


  char *end;
  unsigned long num = strtoul(argv[argc-1], &end, 10);

  if (*end != '\0' || end == argv[argc - 1] ) {
    fprintf(stderr, "Invalid number!");
    return -1;
  }

  if (num < 0) {
    printf("can't read < 0\n");
    return -1;
  }


  if (!strcmp(option, "--binary")) print_binary(num);

  else if (!strcmp(option, "--hex")) print_hex(num);

  else if (!strcmp(option, "--octal")) print_octal(num);


  // print all types
  else {
    print_binary(num);
    print_hex(num);
    print_octal(num);
  }

  return 0;
}
