from modules.keywords import *



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
            load_keywords()
        elif option == 2:
            show_keywords(keywords)
        elif option == 0:
            print('Saliendo')
            break;

