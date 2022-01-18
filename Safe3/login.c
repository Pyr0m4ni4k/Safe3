#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int login(void)
{

    FILE *loginfile;                                // definition pointer of file
    loginfile = fopen("loginfile.txt", "r");        // loginfile point at loginfile.txt

    if(loginfile == NULL)                               // verify the correct opening of the file
    {                                                   //
        loginfile = fopen("loginfile.txt", "w");        //
        fclose(loginfile);                              //
    }                                                   //


    system("python3 login.py");                 // start login.py script

    FILE *filetmp = fopen("tmp.txt", "r");              // control if password is correct
    FILE *filelog = fopen("loginfile.txt", "r");        //
    char ftmp[20], flog[40], nflog[20];                 //
                                                        //
    fscanf(filetmp, "%s", ftmp);                        //
    fscanf(filelog, "%s", flog);                        //

    for(int l=20, m=0; l < 40; l++, m++)
    {
        nflog[m] = flog[l];
    }

    if(strcmp(ftmp, nflog))
    {   system("python3 verify.py");                // start verify.py script
        return 0;
    }
    else
    {   FILE *detent;
        detent = fopen("rxwts98.txt", "w");
        fprintf(detent, "%d", 1);
        fclose(detent);
        return 1;
    }
}
