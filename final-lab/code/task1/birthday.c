#include <stdio.h>

void main(char* args[]) {
    // number of students
    int n = 66;
    float prob = 1.0;
    
    // compute probability that there are no collisions
    int i;
    for (i = 0; i < n; i++) {
	// update probability
	prob *= ((365.0 - (float)i) / 365.0);
    }
 
    // answer is the complement
    prob = 1.0 - prob;
    printf("Probability that %d people have no birthday collisions: %.10f\n", n, prob);
}
