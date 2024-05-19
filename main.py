import cabecalho as cb
import comprimento as ct
import massa as ms
import temperatura as tp
import volume as vm

# Menu principal
while True:
    cb.cabecalho_menu_principal()
    print('-' * 10, 'MENU PRINCIPAL', '-' * 10)
    print('Tipos de medidas')
    print('1 - Comprimento')
    print('2 - Massa')
    print('3 - Temperatura')
    print('4 - Volume')
    print('0 - Sair')

    try:
        tipo_medida = int(input('Escolha o tipo de medida: '))
    except ValueError:
        print('Por favor, digite um número.')
    else:
        if (tipo_medida == 0):
            print('Encerrando o programa...')
            break
        elif (tipo_medida == 1):
            ct.conversor_comprimento()
            continue
        elif (tipo_medida == 2):
            ms.conversor_massa()
            continue
        elif (tipo_medida == 3):
            tp.conversor_temperatura()
            continue
        elif (tipo_medida == 4):
            vm.conversor_volume()
            continue
        else:
            print('Opção inválida. Digite uma opção do menu.')
            
    