#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float f(float x)
{
    double fx;

    fx = pow(x, 3) - 9 * x + 5;

    return fx;
}

float raiz(float a, float b, float precisao, int reps)
{
    int i;
    float fa, fb, fxn, fxnabs, x0;

    for(i = 0; i < reps; i++)
    {
        fa = f(a); //valor do f(a) no eixo y
        fb = f(b); //valor do f(b) no eixo y

        if(fa * fb < precisao)
        {
            x0 = (a+b)/2; //ponto médio do intervalo no eixo x

            fxn = f(x0); //valor do f(x) do ponto médio no eixo y

            fxnabs = fabs(fxn); //valor absoluto do f(x)

            if(fxn < 0) //se f(x) for negativo est� mais pr�ximo do f(a) no eixo y
            {
                if(fb < 0)
                {
                    b = x0; // Da� a no eixo x � substitu�do pelo ponto m�dio

                    if(fxnabs < precisao) //se f(x) for menor que a precis�o para a repeti��o
                    {
                        break;
                    }
                }
                else
                {
                    a = x0;

                    if(fxnabs < precisao) //se f(x) for menor que a precis�o para a repeti��o
                    {
                        break;
                    }
                }

            }
            else //se f(x) for positivo est� mais pr�ximo do f(b) no eixo y
            {
                if(fb > 0)
                {
                    b = x0;

                    if(fxnabs < precisao) //se f(x) for menor que a precis�o para a repeti��o
                    {
                        break;
                    }
                }

                else
                {
                    a = x0; // Da� b no eixo x � substitu�do pelo ponto m�dio

                    if(fxnabs < precisao) //se f(x) for menor que a precis�o para a repeti��o
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


    }
    printf("Raiz Aproximada = %.3f \n", x0);
    printf("Numero de Iteracoes = %d \n", i+1);
}

int main()
{
    int i, reps;
    float a, b, precisao;

    a = 0.5; //intervalo no eixo x
    b = 1;  //intervalo mo eixo x
    reps = 100; //numero de iterações
    precisao = pow(10, -2); //precisão
    raiz(a, b, precisao, reps);


    return 0;
}



