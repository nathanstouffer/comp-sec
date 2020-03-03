/* uid.c */

/* A short program to test how environment
   variables can affect a privilenged 
   program (owned by root) */

#include <stdio.h>
#include <stdlib.h>

extern char **environ;

void main() {
    int i = 0;
    while (environ[i] != NULL) {
        printf("%s\n", environ[i]);
        i++;
    }
}
