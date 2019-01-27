""" Módulo pycompletbar """

from sys import stdout, argv  # noqa
from time import sleep


def autoWriter(texto: str, tempo: float = 0.4):
    """
    Função que emula uma pessoa digitando.
        args:
            texto - texto onde será imprimido na tela.
            tempo - tempo para ser imprimido.
    """

    for a in texto:
        print(a, end='')
        stdout.flush()
        sleep(tempo)
    print()


def clt(funcao):
    """
    Decorator que recebe uma função.
    Função ainda não implementada.
    """
    def inner(*args):
        pass
    pass


def progressbar(items: iter, inner='-#', decor='[]') -> iter:
    """
    Função que imprime na tela uma barra de progresso.
    args:
        items: recebe qualquer iterável como objeto
        inner: recebe uma string contendo 2 caracteres que irá decorar o inte-
               rior da barra de progresso.
        decor: recebe uma string contendo 2 caracteres que irá decorar o exter-
               no da barra de progresso.
    exemplos:
        exemplo 1
        lista = []
        for a in progressbar('algum item iterável'):
            lista.append(ord(a))
        print(lista)
        * será exibido na tela uma barra de progresso em tempo de execução
        e enquanto isso vc pode iterar com os itens normalmente.

        exemplo 2
        print([ord(a) for a in progressbar('algum item iterável')])
    """
    items = list(items)
    t = len(items)
    a, b, c, d = inner + decor
    dormir = 0.01 if t < 1000 else 0
    for z in range(len(items)):
        p = abs(((len(items) * 100) / t) - 100)  # porcent
        e = int(p / 5)  # range line
        print((f'\rloading: {c}{b * e + a * abs(e - 20)}'
               f'{d} - {p:.2f}%   '), end='')
        sleep(dormir)
        yield items.pop(0)
    print(f'\rloading: {c}{b * 20}{d} - 100.00%   ')


