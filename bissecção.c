#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float raiz(float a, float b, float precisao, int reps)
{
    int i;
    float fa, fb, fxn, fxnabs, pm;

    for(i = 0; i < reps; i++)
    {
        fa = pow(a,5)+22*pow(a,3)-8*pow(a,2)-18*a; //valor do f(a) no eixo y
        fb = pow(b,5)+22*pow(b,3)-8*pow(b,2)-18*b; //valor do f(b) no eixo y

        pm = (a+b)/2; //ponto médio do intervalo no eixo x

        fxn = pow(pm,5)+22*pow(pm,3)-8*pow(pm,2)-18*pm; //valor do f(x) do ponto médio no eixo y

        fxnabs = fabs(fxn); //valor absoluto do f(x)

        if(fxn<0) //se f(x) for negativo está mais próximo do f(a) no eixo y
        {
            a = pm; // Daí a no eixo x é substituído pelo ponto médio

            if(fxnabs < precisao){ //se f(x) for menor que a precisão para a repetição
                break;
            }

        }
        else //se f(x) for positivo está mais próximo do f(b) no eixo y
        {
            b = pm; // Daí b no eixo x é substituído pelo ponto médio

            if(fxnabs < precisao){ //se f(x) for menor que a precisão para a repetição
                break;
            }
        }

    }
    printf("Raiz Aproximada = %.3f \n", pm);
    printf("Numero de Iteracoes = %d \n", i+1);
}

int main()
{
    int i, reps;
    float a, b, fa, fb, fxn, fxnabs, pm, precisao;

    printf("Ponto a: ");
    scanf("%f", &a);
    printf("Ponto b: ");
    scanf("%f", &b);
    printf("precisao: ");
    scanf("%f", &precisao);
    printf("Repeticoes: ");
    scanf("%d", &reps);

    raiz(a, b, precisao, reps);
    /*a = 0.1; //intervalo no eixo x
    b = 2;  //intervalo mo eixo x
    reps = 100; //numero de iterações
    precisao = 0.0001; //precisão
    */

    return 0;
}



