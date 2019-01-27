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
    """Decorator que recebe uma função."""
    def inner(*args):
        pass
    pass


def progressbar(items: iter, before: str = '-', after: str = '#') -> iter:
    """
    Função que imprime na tela uma barra de progresso.
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
    test = '[----------]'
    print(test)
    items = list(items) # == (0 ate 9)
    t = len(items) # t inicial == 10
    #print(f'[{"-" * t}]', end = '')
    for a in range(len(items)):        
        print(f'\r[{("#" * (abs(len(items) - t))) }]', end='')
        stdout.flush()
        sleep(1)  # ?
        yield items.pop(0)

if __name__ == '__main__':
    lista = []
    for a in progressbar(range(11)):
        lista.append(a)
    print('fim')
    print(lista)
