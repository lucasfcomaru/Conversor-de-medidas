def conversor_temperatura():
    while True:
        print('Escolha uma unidade de medida.')
        print('c - Celsius')
        print('f - Fahrenheit')
        print('k - Kelvin')
        print('0 - Voltar')

        try:
            temperatura_unidade1 = input('Escolha a unidade de medida de entrada: ')
            
        except ValueError:
            print('Algo deu errado. tente novamente.')
        else:
            # Converter Celsius para outras unidades
            if (temperatura_unidade1.lower() == 'c'):
                try: 
                    temperatura_valor = float(input('Digite seu valor: '))
                    temperatura_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (temperatura_unidade2.lower() == 'f'):
                        calculo = temperatura_valor * 1.8 + 32
                        print(f'O resultado é: {calculo:.2f} °F.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (temperatura_unidade2.lower() == 'k'):
                        calculo = temperatura_valor + 273.15
                        print(f'O resultado é: {calculo:.2f} °K.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (temperatura_unidade2.lower() == 'c'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter Fahrenheit para outras unidades
            elif (temperatura_unidade1.lower() == 'f'):
                try: 
                    temperatura_valor = float(input('Digite seu valor: '))
                    temperatura_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (temperatura_unidade2.lower() == 'c'):
                        calculo = (temperatura_valor - 32) / 1.8
                        print(f'O resultado é: {calculo:.2f} °C.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (temperatura_unidade2.lower() == 'k'):
                        calculo = (temperatura_valor + 459.67) / 1.8
                        print(f'O resultado é: {calculo:.2f} °K.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (temperatura_unidade2.lower() == 'f'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Converter Kelvin para outras unidades
            elif (temperatura_unidade1.lower() == 'k'):
                try: 
                    temperatura_valor = float(input('Digite seu valor: '))
                    temperatura_unidade2 = input('Escolha a unidade de medida de saída: ')

                except ValueError:
                    print('Algo deu errado. tente novamente.')

                else: 
                    if (temperatura_valor < -273.15):
                        print('Digite um valor maior ou igual a 273.15 °K.')
                        continue
                    elif (temperatura_unidade2.lower() == 'c'):
                        calculo = temperatura_valor - 273.15
                        print(f'O resultado é: {calculo:.2f} °C.')
                        
                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (temperatura_unidade2.lower() == 'f'):
                        calculo = temperatura_valor * 1.8 - 459.67
                        print(f'O resultado é: {calculo:.2f} °F.')

                        operacao = input('Deseja realizar outra operação? [Y/N]')
                        if (operacao) in 'yY':
                            continue
                        if (operacao) in 'nN':
                            break
                        else:
                            print('De volta ao menu principal. Escolha uma opção.')
                            break
                    elif (temperatura_unidade2.lower() == 'k'):
                        print('As duas unidades de medidas não podem ser iguais. Tente de novo.')
                        continue
                    else:
                        print('Digite unidades de medidas válidas.')

            # Voltar para o menu principal
            elif (temperatura_unidade1 == '0'):
                print('Voltando para o menu principal')
                break

            else:
                print('Opção inválida. Digite uma opção do menu.')
        