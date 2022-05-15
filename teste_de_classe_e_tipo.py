# programa para validar o tipo da classe da variavel

something = input('Digite algo: ')

print('\nFoi digitado {}' .format(something))

print('\nO tipo de {} é {}' .format(something, type(something)))


# teste de tipo

print('\nO item inserido na variavel é númerico?\n', something.isnumeric())

print('\nO item inserido na variavel é albetico?\n', something.isalpha())

print('\nO item inserido na variavel é alfanumerico?\n', something.isalnum())