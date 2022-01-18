#include <stdio.h>
#include "login.c"
#include "ecdof.c"

int main(void)
{
    system("mkdir files");  // creation files directory

    if(!login())            // verify if login is correct
          return 0;         //

    system("python3 GUI.py");

    FILE *temp, *detect;
    temp = fopen("tmp.txt", "w");
    detect = fopen("rxwts98.txt", "w");
    fprintf(detect, "%s", "0");
    fprintf(temp, "%s", " ");

}
