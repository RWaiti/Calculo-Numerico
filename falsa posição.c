#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double f(double x)
{
    double fx;

    fx = pow(x, 3) - 9 * x + 5;

    return fx;
}

double falsaposicao(double a, double b, double precisao, int reps)
{
    int i;
    double fa, fb, fxn, fxnabs, x0;

    for(i = 0; i < reps; i++)
    {
        fa = f(a); //valor do f(a) no eixo y
        fb = f(b); //valor do f(b) no eixo y

        if(fa * fb < precisao)
        {
            x0 = ((a * fb) - (b * fa))/(fb - fa); //ponto médio do intervalo no eixo x

            fxn = f(x0); //valor do f(x) do ponto médio no eixo y

            fxnabs = fabs(fxn); //valor absoluto do f(x)

            if(fxn < 0) //se f(x) for negativo está mais próximo do f(a) no eixo y
            {
                if(fb < 0)
                {
                    b = x0; // Daí a no eixo x é substituído pelo ponto médio

                    if(fxnabs < precisao) //se f(x) for menor que a precisão para a repetição
                    {
                        break;
                    }
                }
                else
                {
                    a = x0;

                    if(fxnabs < precisao) //se f(x) for menor que a precisão para a repetição
                    {
                        break;
                    }
                }

            }
            else //se f(x) for positivo está mais próximo do f(b) no eixo y
            {
                if(fb > 0)
                {
                    b = x0;

                    if(fxnabs < precisao) //se f(x) for menor que a precisão para a repetição
                    {
                        break;
                    }
                }

                else
                {
                    a = x0; // Daí b no eixo x é substituído pelo ponto médio

                    if(fxnabs < precisao) //se f(x) for menor que a precisão para a repetição
                    {
                        break;
                    }
                }
            }

        }
        else
        {
            break;
        }

        printf("%f\n%f\n", fa, fb);

    }
    printf("Raiz Aproximada = %.3f \n", x0);
    printf("Numero de Iteracoes = %d \n", i);
}

int main()
{

    double a, b, precisao;
    int rep;

    a = 0.5;
    b = 1;
    precisao = pow(10, -3);
    rep = 100;

    falsaposicao(a, b, precisao, rep);

    return 0;
}
