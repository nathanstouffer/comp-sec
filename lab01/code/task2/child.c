/* child.c */

/* This program demonstrates environment variables transfer
   from parent to child programs */

// This file is provided by Kevin Du in the textbook used for this course

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

extern char **environ;

void printenv() {
    int i = 0;
        while (environ[i] != NULL) {
            printf("%s\n", environ[i]);
            i++;
        }
}

void main() {
    pid_t childPid;
	
    switch (childPid = fork()) {
        case 0: 	// child process
            printenv();
            exit(0);
        default: 	// parent process
            //printenv();
            exit(0);
    }
}
