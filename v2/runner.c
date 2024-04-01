#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    // Get the current directory
    char current_dir[1024];
    if (getcwd(current_dir, sizeof(current_dir)) == NULL) {
        perror("getcwd() error");
        return 1;
    }

    // Construct the command to run MCSL.py
    char command[1024];
    sprintf(command, "python3 %s/MCSL.py", current_dir);

    // Fork a child process
    pid_t pid = fork();

    if (pid == -1) {
        perror("fork() error");
        return 1;
    } else if (pid == 0) {
        // Child process
        // Execute the command
        system(command);
        return 0;
    } else {
        // Parent process
        // Wait for the child process to finish
        int status;
        waitpid(pid, &status, 0);

        if (WIFEXITED(status)) {
            printf("Child process exited with status %d\n", WEXITSTATUS(status));
        } else {
            printf("Child process exited abnormally\n");
        }
    }

    return 0;
}
