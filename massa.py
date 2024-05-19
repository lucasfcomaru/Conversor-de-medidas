def conversor_massa():
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
            
            # converter hg para outras unidades
            elif (massa_unidade1.lower() == 'hg'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'kg'):
                        calculo = massa_valor / 10
                        print(f'O resultado é: {calculo:.2f} kg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'dag'):
                        calculo = massa_valor * 10
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
                        calculo = massa_valor * 100
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
                        calculo = massa_valor * 1000
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
                        calculo = massa_valor * 10000
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
                        calculo = massa_valor * 100000
                        print(f'O resultado é: {calculo:.2f} mg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'hg'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # converter dag para outras unidades
            elif (massa_unidade1.lower() == 'dag'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'kg'):
                        calculo = massa_valor / 100
                        print(f'O resultado é: {calculo:.2f} kg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'hg'):
                        calculo = massa_valor / 10
                        print(f'O resultado é: {calculo:.2f} hg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'g'):
                        calculo = massa_valor * 10
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
                        calculo = massa_valor * 100
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
                        calculo = massa_valor * 1000
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
                        calculo = massa_valor * 10000
                        print(f'O resultado é: {calculo:.2f} mg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'dag'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # converter g para outras unidades
            elif (massa_unidade1.lower() == 'g'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'kg'):
                        calculo = massa_valor / 1000
                        print(f'O resultado é: {calculo:.2f} kg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'hg'):
                        calculo = massa_valor / 100
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
                        calculo = massa_valor / 10
                        print(f'O resultado é: {calculo:.2f} dag.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'dg'):
                        calculo = massa_valor * 10
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
                        calculo = massa_valor * 100
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
                        calculo = massa_valor * 1000
                        print(f'O resultado é: {calculo:.2f} mg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'g'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # converter dg para outras unidades
            elif (massa_unidade1.lower() == 'dg'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'kg'):
                        calculo = massa_valor / 10000
                        print(f'O resultado é: {calculo:.2f} kg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'hg'):
                        calculo = massa_valor / 1000
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
                        calculo = massa_valor / 100
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
                        calculo = massa_valor / 10
                        print(f'O resultado é: {calculo:.2f} g.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'cg'):
                        calculo = massa_valor * 10
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
                        calculo = massa_valor * 100
                        print(f'O resultado é: {calculo:.2f} mg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'dg'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # converter cg para outras unidades
            elif (massa_unidade1.lower() == 'cg'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'kg'):
                        calculo = massa_valor / 100000
                        print(f'O resultado é: {calculo:.2f} kg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'hg'):
                        calculo = massa_valor / 10000
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
                        calculo = massa_valor / 1000
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
                        calculo = massa_valor / 100
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
                        calculo = massa_valor / 10
                        print(f'O resultado é: {calculo:.2f} dg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'mg'):
                        calculo = massa_valor * 10
                        print(f'O resultado é: {calculo:.2f} mg.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'cg'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # converter mg para outras unidades
            elif (massa_unidade1.lower() == 'mg'):
                try: 
                    massa_valor = float(input('Digite seu valor: '))
                    massa_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (massa_unidade2.lower() == 'kg'):
                        calculo = massa_valor / 1000000
                        print(f'O resultado é: {calculo:.2f} kg.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (massa_unidade2.lower() == 'hg'):
                        calculo = massa_valor / 100000
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
                        calculo = massa_valor / 10000
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
                        calculo = massa_valor / 1000
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
                        calculo = massa_valor / 100
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
                        calculo = massa_valor / 10
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
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Voltar para o menu principal
            elif (massa_unidade1 == '0'):
                print('Voltando para o menu principal')
                break
            else:
                print('Opção inválida. Digite uma opção do menu.')