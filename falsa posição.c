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

        //fa = pow(a,3) - 9 * a + 3;
        //fa = pow(b,3) - 9 * b + 3;

        //pm = (a+b)/2; //ponto m�dio do intervalo no eixo x

        pm = ((a * fb) - (b * fa))/ fb - fa; //e tomado a m�dia aritm�tica ponderada entre a e b com pesos |f(b)| e |f(a)|


        fxn = pow(pm,5)+22*pow(pm,3)-8*pow(pm,2)-18*pm; //valor do f(x) do ponto m�dio no eixo y
        //fxn = pow(b,3) - 9 * b + 3;

        //fxnabs = fabs(fxn); //valor absoluto do f(x)

        if(fxn<0) //se f(x) for negativo est� mais pr�ximo do f(a) no eixo y
        {
            a = pm; // Da� a no eixo x � substitu�do pelo ponto m�dio

            if(fxnabs < precisao){ //se f(x) for menor que a precis�o para a repeti��o
                break;
            }

        }
        else //se f(x) for positivo est� mais pr�ximo do f(b) no eixo y
        {
            b = pm; // Da� b no eixo x � substitu�do pelo ponto m�dio

            if(fxnabs < precisao){ //se f(x) for menor que a precis�o para a repeti��o
                break;
            }
        }

    }
    printf("Raiz Aproximada = %.3f \n", pm);
    printf("Numero de Iteracoes = %d \n", i);
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
    reps = 100; //numero de itera��es
    precisao = 0.0001; //precis�o
    */

    return 0;
}





