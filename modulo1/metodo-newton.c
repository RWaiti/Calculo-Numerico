#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double deriv(double x , double fx);
double f(double x);

double newton(double x, double precisao, int inter)
{
    double fx;
    int i, cont;
    cont = 0;

    for(i = 0; i < inter; i++)
    {
      fx = f(x);
      
      if(fabs(fx) < precisao)
      {
        break;
      }
      else
      {
        x = deriv(x, fx);

        cont++;
      }
    }
    printf("Raiz aproximada: %lf\nNumero de interacoes: %d\n", x, i);
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

    newton(x, precisao, interacoes);

    return 0;
}

double f(double x)
{
  double funcao;
  funcao = pow(x, 3) - 9 * x + 5;
  return funcao;
}
double deriv(double x , double fx)
{
    double xk, devx;

    devx = 3 * pow(x, 2) - 9;

    xk = x - (fx / devx);

    return xk;
}