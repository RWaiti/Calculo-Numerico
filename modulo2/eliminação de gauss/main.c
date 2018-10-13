#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void gauss(float E[3][4])
{
    int i, j;
    float aux, x[3], mataux[3][4];

    for(i = 0; i < 4; i++)
    {
        aux = E[1][i];
        E[1][i] = E[0][i];
        E[0][i] = aux;
    }
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 4; j++)
        {

            printf("%0.f ", E[i][j]);


        }
        printf("\n");

    }
    printf("\n\n");

    for(i = 0; i < 4; i++)
    {
        mataux[0][i] = E[0][i];
        mataux[1][i] = E[1][i] - (E[0][i] * (E[1][0] / E[0][0]));
        mataux[2][i] = E[2][i] - (E[0][i] * (E[2][0] / E[0][0]));
    }
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 4; j++)
        {

            printf("%0.f ", mataux[i][j]);


        }
        printf("\n");

    }
    printf("\n\n");

    for(i = 0; i < 4; i++)
    {
        mataux[2][i] = mataux[2][i] - (mataux[1][i] * (mataux[2][1] / mataux[1][1]));
    }

    printf("\n\n");
    for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 4; j++)
        {

            printf("%0.f ", mataux[i][j]);


        }
        printf("\n");

    }
    printf("\n\n");

    x[2] = mataux[2][3] / mataux[2][2];
    x[1] = (mataux[1][3] - (mataux[1][2] * x[2])) / mataux[1][1];
    x[0] = (mataux[0][3] - (mataux[0][2] * x[2]) - (mataux[0][1] * x[1])) / mataux[0][0];

   /* for(i = 0; i < 3; i++)
    {
        for(j = 0; j < 4; j++)
        {

            printf("%0.f, ", E[i][j]);


        }
        printf("\n");

    }*/
    printf("\n\n x:\n\n");
    printf("{");
    for(i = 0; i < 3; i++)
    {
        if(i >= 0 && i < 2)
            {
                printf("%0.f, ", x[i]);
            }
            else if(i < 3)
            {
                printf("%0.f", x[i]);
            }
    }

    printf("}");
    printf("\n\n");

}

int main()
{
    float mat[3][4] = {{3,2,4,1},
    {1,1,2,2},
    {4,3,-2,3}};

    gauss(mat);

    return 0;
}
