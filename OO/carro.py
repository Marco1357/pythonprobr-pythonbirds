"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por duas clsses:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dados de Velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A Direção terá a responsabilidade de contralar a direção. Ela ofereçe os seguintes
atributos:
1) valor da direção com valores possíveis: Norte ,sul, Leste, Oeste
2) Método girar a direita

  N
O   L
  S

    Ex:
    # Testando o motor
    >>> motor = motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> motor.frear()
    >>> motor.velocidade






"""