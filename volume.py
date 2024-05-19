def conversor_volume():
    while True:
        print('Escolha uma unidade de medida.')
        print('km - Quilômetro cúbico')
        print('hm - Hectômetro cúbico')
        print('dam - Decâmetro cúbico ')
        print('m - Metro cúbico')
        print('dm - Decímetro cúbico ')
        print('cm - Centímetro cúbico ')
        print('mm - milímetro cúbico ')
        print('0 - Voltar')

        try:
            volume_unidade1 = input('Escolha a unidade de medida de entrada: ')
            
        except ValueError:
            print('Algo deu errado. tente novamente.')
        else:
            # Converter km³ para outras unidades
            if (volume_unidade1.lower() == 'km'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'hm'):
                        calculo = volume_valor * 1000
                        print(f'O resultado é: {calculo} hm³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        calculo = volume_valor * 1000 ** 2
                        print(f'O resultado é: {calculo} dam³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        calculo = volume_valor * 1000 ** 3
                        print(f'O resultado é: {calculo} m³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        calculo = volume_valor * 1000 ** 4
                        print(f'O resultado é: {calculo} dm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        calculo = volume_valor * 1000 ** 5
                        print(f'O resultado é: {calculo} cm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        calculo = volume_valor * 1000 ** 6
                        print(f'O resultado é: {calculo} mm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'km'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter hm³ para outras unidades
            elif (volume_unidade1.lower() == 'hm'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'km'):
                        calculo = volume_valor / 1000
                        print(f'O resultado é: {calculo} km³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        calculo = volume_valor * 1000
                        print(f'O resultado é: {calculo} dam³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        calculo = volume_valor * 1000 ** 2
                        print(f'O resultado é: {calculo} m³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        calculo = volume_valor * 1000 ** 3
                        print(f'O resultado é: {calculo} dm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        calculo = volume_valor * 1000 ** 4
                        print(f'O resultado é: {calculo} cm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        calculo = volume_valor * 1000 ** 5
                        print(f'O resultado é: {calculo} mm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'hm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter dam³ para outras unidades
            elif (volume_unidade1.lower() == 'dam'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'km'):
                        calculo = volume_valor / 1000 ** 2
                        print(f'O resultado é: {calculo} km³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'hm'):
                        calculo = volume_valor / 1000
                        print(f'O resultado é: {calculo} hm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        calculo = volume_valor * 1000
                        print(f'O resultado é: {calculo} m³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        calculo = volume_valor * 1000 ** 2
                        print(f'O resultado é: {calculo} dm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        calculo = volume_valor * 1000 ** 3
                        print(f'O resultado é: {calculo} cm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        calculo = volume_valor * 1000 ** 4
                        print(f'O resultado é: {calculo} mm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter m³ para outras unidades
            elif (volume_unidade1.lower() == 'm'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'km'):
                        calculo = volume_valor / 1000 ** 3
                        print(f'O resultado é: {calculo} km³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'hm'):
                        calculo = volume_valor / 1000 ** 2
                        print(f'O resultado é: {calculo} hm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        calculo = volume_valor / 1000
                        print(f'O resultado é: {calculo} dam³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        calculo = volume_valor * 1000
                        print(f'O resultado é: {calculo} dm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        calculo = volume_valor * 1000 ** 2
                        print(f'O resultado é: {calculo} cm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        calculo = volume_valor * 1000 ** 3
                        print(f'O resultado é: {calculo} mm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter dm³ para outras unidades
            elif (volume_unidade1.lower() == 'dm'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'km'):
                        calculo = volume_valor / 1000 ** 4
                        print(f'O resultado é: {calculo} km³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'hm'):
                        calculo = volume_valor / 1000 ** 3
                        print(f'O resultado é: {calculo} hm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        calculo = volume_valor / 1000 ** 2
                        print(f'O resultado é: {calculo} dam³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        calculo = volume_valor / 1000
                        print(f'O resultado é: {calculo} m³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        calculo = volume_valor * 1000 
                        print(f'O resultado é: {calculo} cm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        calculo = volume_valor * 1000 ** 2
                        print(f'O resultado é: {calculo} mm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter cm³ para outras unidades
            elif (volume_unidade1.lower() == 'cm'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'km'):
                        calculo = volume_valor / 1000 ** 5
                        print(f'O resultado é: {calculo} km³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'hm'):
                        calculo = volume_valor / 1000 ** 4
                        print(f'O resultado é: {calculo} hm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        calculo = volume_valor / 1000 ** 3
                        print(f'O resultado é: {calculo} dam³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        calculo = volume_valor / 1000 ** 2
                        print(f'O resultado é: {calculo} m³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        calculo = volume_valor / 1000 
                        print(f'O resultado é: {calculo} dm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        calculo = volume_valor * 1000
                        print(f'O resultado é: {calculo} mm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter mm³ para outras unidades
            elif (volume_unidade1.lower() == 'mm'):
                try: 
                    volume_valor = float(input('Digite seu valor: '))
                    volume_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (volume_unidade2.lower() == 'km'):
                        calculo = volume_valor / 1000 ** 6
                        print(f'O resultado é: {calculo} km³.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'hm'):
                        calculo = volume_valor / 1000 ** 5
                        print(f'O resultado é: {calculo} hm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dam'):
                        calculo = volume_valor / 1000 ** 4
                        print(f'O resultado é: {calculo} dam³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'm'):
                        calculo = volume_valor / 1000 ** 3
                        print(f'O resultado é: {calculo} m³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'dm'):
                        calculo = volume_valor / 1000 ** 2
                        print(f'O resultado é: {calculo} dm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'cm'):
                        calculo = volume_valor / 1000
                        print(f'O resultado é: {calculo} cm³.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (volume_unidade2.lower() == 'mm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Voltar para o menu principal
            elif (volume_unidade1 == '0'):
                print('Voltando para o menu principal')
                break
            
            else:
                print('Opção inválida. Digite uma opção do menu.')

