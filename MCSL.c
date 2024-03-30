#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fp;
    char command[100];

    // Check if Python 3 is available
    fp = popen("python3 --version", "r");
    if (fp != NULL) {
        pclose(fp);
        strcpy(command, "python3 MCSL.py");
        system(command);
        return 0;
    }

    // Check if Python 2 is available
    fp = popen("python --version", "r");
    if (fp != NULL) {
        pclose(fp);
        strcpy(command, "python MCSL.py");
        system(command);
        return 0;
    }

    // Neither Python 3 nor Python 2 is available
    printf("Error: Python not found\n");
    return 1;
}
