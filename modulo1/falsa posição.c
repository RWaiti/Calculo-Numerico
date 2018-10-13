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
            x0 = ((a * fb) - (b * fa))/(fb - fa); //ponto m�dio do intervalo no eixo x

            fxn = f(x0); //valor do f(x) do ponto m�dio no eixo y

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
