#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *ec(char string[])
{
    char *new_string;
    new_string = malloc(strlen(string));
    strcpy(new_string, string);
    for(int i=0; i < strlen(string); i++)
        new_string[i]++;

    return new_string;
}

