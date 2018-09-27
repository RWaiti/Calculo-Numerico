#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double fi(double x)
{
    double fi1;
    fi1 = (pow(x, 3) + 5) / 9 ;

    return fi1;
}

/*double f12(double x)
{
    fi2 = sqrt(6 - x);

    return fi2;
}

double f13(double x)
{
    fi1 = 6 / (x + 1);

    return fi3;
}*/

double pontofixo(double x, double precisao, int inter)
{
    double fx;
    int i;

    for(i = 0; i < inter; i++)
    {
        if(fabs(fx) < precisao)
        {
            break;
        }

        else
        {
            fx = pow(x, 3) - 9 * x + 5;

            x = fi(x);

        }
    }

    printf("%lf\n%d\n", x, i);
}

int main()
{
    double x, precisao, I, a, b;
    int interacoes;

    a = 0.5;
    b = 1;
    I = (a + b) / 2;
    x = I;

    precisao = pow(10, -2);
    interacoes = 100;

    pontofixo(x, precisao, interacoes);

    return 0;
}
