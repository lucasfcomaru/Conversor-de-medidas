def conversor_volume():
    while True:
        print('Escolha uma unidade de medida.')
        print('kg - Quilograma')
        print('hg - Hectograma')
        print('dag - Decagrama ')
        print('g - Grama')
        print('dg - Decigrama ')
        print('cg - Centigrama ')
        print('mg - miligrama ')
        print('0 - Voltar')

        try:
            massa_unidade1 = input('Escolha a unidade de medida de entrada: ')
            
        except ValueError:
            print('Algo deu errado. tente novamente.')
        else:
            # Converter kg para outras unidades
            if (massa_unidade1.lower() == 'kg'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'hg'):
                        calculo = massa_valor * 10
                        print(f'O resultado é: {calculo:.2f} hg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'dag'):
                        calculo = massa_valor * 100
                        print(f'O resultado é: {calculo:.2f} dag.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'g'):
                        calculo = massa_valor * 1000
                        print(f'O resultado é: {calculo:.2f} g.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'dg'):
                        calculo = massa_valor * 10000
                        print(f'O resultado é: {calculo:.2f} dg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'cg'):
                        calculo = massa_valor * 100000
                        print(f'O resultado é: {calculo:.2f} cg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'mg'):
                        calculo = massa_valor * 1000000
                        print(f'O resultado é: {calculo:.2f} mg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'kg'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')