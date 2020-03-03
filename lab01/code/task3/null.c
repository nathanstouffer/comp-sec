/* exec-test.c */

/* A short program to test the functionality
   of function execve(); */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

extern char **environ;

int main() {
    char *argv[2];
    
    argv[0] = "/user/bin/env";
    argv[1] = NULL;

    execve("/usr/bin/env", argv, NULL);
    //execve("/usr/bin/env", argv, environ);

    return 0;
}
