/* system-test. */

/* A short program to test how the system()
   function works */

#include <stdio.h>
#include <stdlib.h>

int main() {
    system("/usr/bin/env");

    return 0;
}
