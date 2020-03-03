/* mylib.c */

/* a short function to override sleep() */

#include <stdio.h>

void sleep (int s) {
    /* If this is invoked in a privileged program
       you can do damages here! */
    printf("I am not sleeping!\n");
}
