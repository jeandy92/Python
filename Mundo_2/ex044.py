valorproduto = float(input('Valor pago no produto: '))
formadepagamento = int(input('Escolha a forma de pagamento:\n 1 - CHEQUE\n 2 - DINHEIRO \n 3 - CARTÃO\n'))

if formadepagamento > 3 or formadepagamento <= 0:
    print("Opção inválida \n")
else:
    if formadepagamento == 1 or formadepagamento == 2:
        desconto = valorproduto * 0.10
        print('Valor do desconto R${:.2f}'.format(desconto))
        print('Valor final do produto R${:.2f}'.format(valorproduto - desconto))
    elif formadepagamento == 3:
        opcao = int(input('1 - A vista \n 2 - Parcelado\n '))
        if opcao > 2 or opcao <= 0:
           print("Opção inválida\n")
        else:
            if opcao == 1:
                desconto = valorproduto * 0.05
                print('Valor do desconto  R${:.2f}'.format(desconto))
                print('valor final do produto  R${:.2f}'.format(valorproduto - desconto))
            elif opcao == 2:
                qtdparcelas = int(input('Quantidade de Parcelas: \n'))
                if qtdparcelas <= 0:
                    print('Quantidade de parcelas não pode ser zero ou menor')
                else:
                     if qtdparcelas == 2:
                        print('2x')
                        print('Valor das Parcelas: R${:.2f}'.format(valorproduto / qtdparcelas))
                        print('Valor total do Produto R${:.2f}'.format(valorproduto))
                     elif qtdparcelas >= 3:
                        print(qtdparcelas, "x")
                        print('Valor das Parcelas: R${:.2f}'.format(int(((valorproduto + (valorproduto * 0.20)) / qtdparcelas))))
                        print('Valor total do Produto: R${:.2f}'.format(valorproduto + (valorproduto * 0.20)))
