def sandTop(*items):
    print('\n You ordered a sandwich with this tops:')
    for item in items:
        print(f'- {item}')

sandTop('carne','tomate')
sandTop('carne')
sandTop('carne','huevo','chorizo')