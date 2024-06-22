glossary = {
    'python' : 'lenguaje de programación',
    'lista' : 'grupo de palabras o números que se puede editar',
    'tupla' : 'grupo de palabras o números que no se puede editar',
    'diccionario' : 'grupo de palabras o números que se relacionan entre sí',
    'variable' : 'palabra que puede cambiar su valor', 
    'callback' : 'A subroutine function which is passed as an argument to be executed at some point in the future.',   
    'class' : 'A template for creating user-defined objects. Class definitions normally contain method definitions which operate on instances of the class.',
    'generator' : 'A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.',
    'generator iterator' : 'An object created by a generator function.',
    'Indentation' : 'Indentation refers to the spaces at the beginning of a code line'
}

for key,value in glossary.items():
    print(f"\n {key.title()}: {value}")