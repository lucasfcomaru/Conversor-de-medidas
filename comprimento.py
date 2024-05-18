def conversor_comprimento():
    while True:
        print('Escolha a primeira unidade de medida.')
        print('km - Quilômetro')
        print('hm - Hectômetro')
        print('dam - Decâmetro')
        print('m - Metro')
        print('dm - Decímetro')
        print('cm - Centímetro')
        print('mm - Milímetro')
        print('0 - Voltar')

        try:
            comprimento_unidade1 = input('Escolha a unidade de medida de entrada: ')
            
        except ValueError:
            print('Algo deu errado. tente novamente.')
        else:
            # Converter km para outras unidades
            if (comprimento_unidade1.lower() == 'km'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'hm'):
                        calculo = comprimento_valor1 * 10
                        print(f'O resultado é: {calculo:.2f} hm.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        calculo = comprimento_valor1 * 100
                        print(f'O resultado é: {calculo:.2f} dam.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        calculo = comprimento_valor1 * 1000
                        print(f'O resultado é: {calculo:.2f} m.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        calculo = comprimento_valor1 * 10000
                        print(f'O resultado é: {calculo:.2f} dm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        calculo = comprimento_valor1 * 100000
                        print(f'O resultado é: {calculo:.2f} cm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        calculo = comprimento_valor1 * 1000000
                        print(f'O resultado é: {calculo:.2f} mm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'km'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')
            
            # converter hm para outras unidades de medidas
            elif (comprimento_unidade1.lower() == 'hm'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'km'):
                        calculo = comprimento_valor1 / 10
                        print(f'O resultado é: {calculo:.2f} km.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        calculo = comprimento_valor1 * 10
                        print(f'O resultado é: {calculo:.2f} dam.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        calculo = comprimento_valor1 * 100
                        print(f'O resultado é: {calculo:.2f} m.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        calculo = comprimento_valor1 * 1000
                        print(f'O resultado é: {calculo:.2f} dm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        calculo = comprimento_valor1 * 10000
                        print(f'O resultado é: {calculo:.2f} cm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        calculo = comprimento_valor1 * 100000
                        print(f'O resultado é: {calculo:.2f} mm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'hm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')
            
            # converter dam para outras unidades de medidas
            elif (comprimento_unidade1.lower() == 'dam'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'km'):
                        calculo = comprimento_valor1 / 100
                        print(f'O resultado é: {calculo:.2f} km.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'hm'):
                        calculo = comprimento_valor1 / 10
                        print(f'O resultado é: {calculo:.2f} hm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        calculo = comprimento_valor1 * 10
                        print(f'O resultado é: {calculo:.2f} m.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        calculo = comprimento_valor1 * 100
                        print(f'O resultado é: {calculo:.2f} dm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        calculo = comprimento_valor1 * 1000
                        print(f'O resultado é: {calculo:.2f} cm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        calculo = comprimento_valor1 * 10000
                        print(f'O resultado é: {calculo:.2f} mm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')
            
            # converter m para outras unidades de medidas
            elif (comprimento_unidade1.lower() == 'm'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'km'):
                        calculo = comprimento_valor1 / 1000
                        print(f'O resultado é: {calculo:.2f} km.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'hm'):
                        calculo = comprimento_valor1 / 100
                        print(f'O resultado é: {calculo:.2f} hm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        calculo = comprimento_valor1 / 10
                        print(f'O resultado é: {calculo:.2f} dam.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        calculo = comprimento_valor1 * 10
                        print(f'O resultado é: {calculo:.2f} dm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        calculo = comprimento_valor1 * 100
                        print(f'O resultado é: {calculo:.2f} cm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        calculo = comprimento_valor1 * 1000
                        print(f'O resultado é: {calculo:.2f} mm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')
                    
            # converter dm para outras unidades de medidas
            elif (comprimento_unidade1.lower() == 'dm'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'km'):
                        calculo = comprimento_valor1 / 10000
                        print(f'O resultado é: {calculo:.2f} km.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'hm'):
                        calculo = comprimento_valor1 / 1000
                        print(f'O resultado é: {calculo:.2f} hm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        calculo = comprimento_valor1 / 100
                        print(f'O resultado é: {calculo:.2f} dam.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        calculo = comprimento_valor1 / 10
                        print(f'O resultado é: {calculo:.2f} m.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        calculo = comprimento_valor1 * 10
                        print(f'O resultado é: {calculo:.2f} cm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        calculo = comprimento_valor1 * 100
                        print(f'O resultado é: {calculo:.2f} mm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')  
            
            # converter cm para outras unidades de medidas
            elif (comprimento_unidade1.lower() == 'cm'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'km'):
                        calculo = comprimento_valor1 / 100000
                        print(f'O resultado é: {calculo:.2f} km.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'hm'):
                        calculo = comprimento_valor1 / 10000
                        print(f'O resultado é: {calculo:.2f} hm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        calculo = comprimento_valor1 / 1000
                        print(f'O resultado é: {calculo:.2f} dam.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        calculo = comprimento_valor1 / 100
                        print(f'O resultado é: {calculo:.2f} m.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        calculo = comprimento_valor1 / 10
                        print(f'O resultado é: {calculo:.2f} dm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        calculo = comprimento_valor1 * 10
                        print(f'O resultado é: {calculo:.2f} mm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # converter mm para outras unidades de medidas
            elif (comprimento_unidade1.lower() == 'mm'):
                try: 
                    comprimento_valor1 = float(input('Digite seu valor: '))
                    comprimento_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (comprimento_unidade2.lower() == 'km'):
                        calculo = comprimento_valor1 / 1000000
                        print(f'O resultado é: {calculo:.2f} km.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'hm'):
                        calculo = comprimento_valor1 / 100000
                        print(f'O resultado é: {calculo:.2f} hm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dam'):
                        calculo = comprimento_valor1 / 10000
                        print(f'O resultado é: {calculo:.2f} dam.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'm'):
                        calculo = comprimento_valor1 / 1000
                        print(f'O resultado é: {calculo:.2f} m.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'dm'):
                        calculo = comprimento_valor1 / 100
                        print(f'O resultado é: {calculo:.2f} dm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'cm'):
                        calculo = comprimento_valor1 / 10
                        print(f'O resultado é: {calculo:.2f} cm.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (comprimento_unidade2.lower() == 'mm'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')
            
            # Voltar para o menu principal
            elif (comprimento_unidade1 == '0'):
                print('Voltando para o menu principal')
                break
            else:
                print('Opção inválida. Digite uma opção do menu.')