#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *ed(char string[])
{
    char *new_string;
    new_string = malloc(strlen(string) * sizeof(char *));
    strcpy(new_string, string);
    for(int i=0; i < strlen(string); i++)
        new_string[i]--;

    return new_string;
}

int main(void)
{
    // save name pass number on num variable
    FILE *tmp;
    char num[3];
    tmp = fopen("tmp.txt", "r");
    fscanf(tmp, "%s", num);
    fclose(tmp);

    // open data file
    FILE *data_file;
    char name_data_file[20];
    strcpy(name_data_file, "files/");
    strcat(name_data_file, num);
    strcat(name_data_file, ".txt");
    data_file = fopen(name_data_file, "r");

    // cretion struct
    struct data
    {
        char name_pass[40];
        char username[40];
        char email[40];
        char ID[40];
        char password[40];
    };

    // read data in data_file decode and save in a struct variable
    struct data data2;

    int i = 0;
    char buffer[40];
    while(fgets(buffer, 40, data_file))
    {
        switch(i)
        {
            case 0: strcpy(data2.name_pass, ed(buffer)); break;
            case 1: strcpy(data2.username, ed(buffer)); break;
            case 2: strcpy(data2.email, ed(buffer)); break;
            case 3: strcpy(data2.ID, ed(buffer)); break;
            case 4: strcpy(data2.password, ed(buffer)); break;
        }
        i++;
    }

    // open and write struct data in tmp.txt
    FILE *temp;
    temp = fopen("tmp.txt", "w");
    fprintf(temp, "%s", data2.name_pass);
    fprintf(temp, "%s", data2.username);
    fprintf(temp, "%s", data2.email);
    fprintf(temp, "%s", data2.ID);
    fprintf(temp, "%s", data2.password);
    fclose(temp);
}
