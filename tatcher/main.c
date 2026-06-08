#include <stdio.h>
#include <sys/inotify.h>
#include <unistd.h>

#include "DATA.h"

int main(int argc, char **argv)
{
  // 1. get path
  if (argc < 2) {
    printf("Usage: %s <dir>\n", PROG_NAME);
    printf("See: %s --help\n", PROG_NAME);
    return 0;
  }

  const char *path = argv[1];
  char buf[4096];

  // 2. init inotify
  int fd = inotify_init();
  if (fd < 0) {
    perror("inotify_init");
    return -1;
  }

  // 3. put watcher  types
  inotify_add_watch(fd, path,
        ( IN_MODIFY | IN_CLOSE_WRITE | IN_DELETE |
        IN_MOVED_FROM | IN_MOVED_TO )
  );

  // 4. while loop
  while (T_RUE)
  {
    ssize_t len = read(fd, &buf, sizeof(buf));
    if (len < 0) {
      perror("read");
      return -1;
    }

    for (size_t i=0; i<len;) {
      struct inotify_event *event = (struct inotify_event*)&buf[i];

      // the checker
      if (event->mask & IN_MODIFY)      printf("Modify: %s\n", event->name);
      if (event->mask & IN_CLOSE_WRITE) printf("Create: %s\n", event->name);
      if (event->mask & IN_DELETE)      printf("Delete: %s\n", event->name);
      if (event->mask & IN_MOVED_FROM)  printf("MoveFrom: %s\n", event->name);
      if (event->mask & IN_MOVED_TO)    printf("MoveTo: %s\n", event->name);
      if (event->mask & IN_ISDIR)       printf("(directory)\n");

      i += sizeof(struct inotify_event) + event->len;
    }
  }

  return 0;
}
