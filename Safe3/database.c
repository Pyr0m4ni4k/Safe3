#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "ecdof.c"
#include "safe3.h"

void database(void)               // creation database struct
{
    struct data
    {
        char name_pass[40];
        char username[40];
        char email[40];
        char ID[40];
        char password[40];
    };
    struct data data;       // creation struct variable


    FILE *count_file;                                   // open and read count_file file
    count_file = fopen("countfile.txt", "r");
    if(feof(count_file))
    {
        count_file = fopen("countfile.txt", "w");
        fprintf(count_file, "%d", 0);
        fclose(count_file);
        puts("new");
    }
    int counter;


    fscanf(count_file, "%d", &counter);         // save num in counter
    fclose(count_file);


    FILE *temp;                     // open and read tmp.txt
    temp = fopen("tmp.txt", "r");

    int i = 0;
    char buffer[40];
    while(fgets(buffer, 40, temp))
    {
        switch(i)
        {
            case 0: strcpy(data.name_pass, buffer); break;
            case 1: strcpy(data.username, buffer); break;
            case 2: strcpy(data.email, buffer); break;
            case 3: strcpy(data.ID, buffer); break;
            case 4: strcpy(data.password, buffer); break;
        }
        i++;
    }
    fclose(temp);


    FILE *memorize;                                     // creation memorize data file
    char name_of_file[15] = "files/";
    char txt[7];
    char counter2 = '\0';
    int real_count = counter;           // if counter is modified from itoa() real_count store his value
    strcpy(txt, ".txt");
    itoa(counter, &counter2);
    strcat(name_of_file, &counter2);
    strcat(name_of_file, txt);
    memorize = fopen(name_of_file, "w");


    fprintf(memorize, "%d\n", real_count);         // save data in memorize file

    char name_of_pass[strlen(data.name_pass)];
    strcpy(name_of_pass, data.name_pass);
    fprintf(memorize, "%s", ec(name_of_pass));

    char name_username[strlen(data.username)];
    strcpy(name_username, data.username);
    fprintf(memorize, "%s", ec(name_username));

    char name_email[strlen(data.email)];
    strcpy(name_email, data.email);
    fprintf(memorize, "%s", ec(name_email));

    char name_ID[strlen(data.ID)];
    strcpy(name_ID, data.ID);
    fprintf(memorize, "%s", ec(name_ID));

    char namepass[strlen(data.password)];
    strcpy(namepass, data.password);
    fprintf(memorize, "%s", ec(namepass));


    fclose(memorize);

    real_count += 1;                                // increment counter
    count_file = fopen("countfile.txt", "w");
    fprintf(count_file, "%d", real_count);
    fclose(count_file);
}


int main(void)
{
    database();
}
