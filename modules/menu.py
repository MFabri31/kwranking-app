
def nav():
    while True:
        print('-------------')
        print('Kwranking App')
        print('-------------')
        
        while True: 
            try:
                print('[1] - Importar palabras claves\n[2] - Mostrar palabras claves\n[0] - Salir')
                option = int(input('>'))
            except ValueError:
                print('Aviso! No se permite el ingreso de cadenas.')
            else:
                break;


        if option > 2:
            print('Opción no contemplada.')
        elif option == 1:
            print('Importando palabras claves.')
        elif option == 2:
            print('Mostrando palabras claves.')
        elif option == 0:
            print('Saliendo')
            break;

