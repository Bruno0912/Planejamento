prods = list(
    [
        [
            'Arroz 5Kg',
            float(19),
            0
        ],
        [
            'Feijão Carioca 1Kg',
            float(13),
            1
        ],
        [
            'Açúcar Cristal 5kg',
            float(25),
            2
        ],
        [
            'Café 1kg',
            float(23.59),
            3
        ],
        [
            'Extrato de Tomate 2 Kg',
            float(35),
            4
        ]
    ]
)

sl_prods = dict()
total = float(0)

def see_prods():
    print('|', ('-' * 50), '|')

    for x in prods:
        print('\t', x[0], ' |\033[92m R$ ', x[1], ' \033[00m|\033[93m C. do Produto: ', x[2], '\033[00m')

    print('|', ('-' * 50), '|')

def select_prods():
    global sl_prods
    print('Quais produtos deseja selecionar?')
    see_prods()

    selected = False
    while(selected == False):
        error_inp = False
        while(error_inp == False):
            try:
                select = int(input('Código do Produto: '))
                error_inp = True
            except:
                print('Insira um código válido')

        error_inp = False
        while(error_inp == False):
            try:
                units = int(input('Unidades: '))
                error_inp = True
            except:
                print('Insira um número válido')
        
        if(any(select == p[2] for p in prods)):
            product = prods[select]
            if(product[2] in sl_prods):
                osl_prods = sl_prods[product[2]]
                sl_prods.update({product[2]: [
                    product[0],
                    float((product[1] * units) + osl_prods[1]),
                    int(units + osl_prods[2])
                ]})
            else:
                sl_prods.update({product[2]: [
                    product[0],
                    float(product[1] * units),
                    units
                ]})
        else:
            print('\nProduto não encontrado!\n')

        if(bool(int(input('Deseja continuar? [0-1]: ')))):
            if(bool(int(input('Rever produtos? [0-1]: ')))):
                see_prods()
        else:
            selected = True

def remove_prod():
    global sl_prods
    if(len(sl_prods) > 0):
        print('\nQual(is) produto(s) deseja remover?')
        for x in sl_prods:
            prod = sl_prods[x]
            print(x, ' - ', prod[0], ' |\033[92m R$ ', prod[1], ' \033[00m|\033[93m Unidades: ', prod[2], '\033[00m')

        error_inp = False
        while(error_inp == False):
            try:
                select = int(input('Código: '))
                error_inp = True
            except:
                print('Insira um código válido')
        
        if(select in sl_prods):
            sl_prods.pop(select)
        else:
            print('\nProduto não encontrado!\n')

        if(len(sl_prods) > 0 and bool(int(input('Deseja remover outro produto? [0-1]: ')))):
            remove_prod()
    else:
        print('\nNão há produtos para serem removidos!')

def see_total():
    global total, sl_prods
    if(len(sl_prods) > 0):
        total = float(0)
        for x in sl_prods:
            prod = sl_prods[x]
            print(prod[0], ' |\033[92m R$ ', prod[1], ' \033[00m|\033[93m Unidades: ', prod[2], '\033[00m')
            total += prod[1]

        print('\nTotal: \033[92m R$ ', total, '\033[00m\n')
        if(bool(int(input('Deseja remover algum produto? [0-1]: ')))):
            remove_prod()
        elif(total > 0 and bool(int(input('Deseja realizar o pagamento? [0-1]: ')))):
            payment()

    else:
        print('\nVocê não selecionou nenhum produto!\n')

def payment():
    global total, sl_prods
    total = float(0)
    for x in sl_prods:
        prod = sl_prods[x]
        total += prod[1]
    if(total > 0): 
        print(f'''\nTotal: \033[92mR$ {total}\033[00m
    Formas de Pagamento:
    [1] - Débito ou Crédito
    [2] - Espécie
    [3] - Cancelar\n''')

        error_inp = False
        while(error_inp == False):
            try:
                select = int(input('Escolher: '))
                if(select < 1 or select > 3):
                    print('Insira um comando válido')
                else:
                    error_inp = True
            except:
                print('Insira um comando válido')
        
        match(select):
            case 1:
                print('Pago!')
                total = float(0)
                sl_prods = dict()
            case 2:
                error_inp = False
                while(error_inp == False):
                    try:
                        value = float(input('Valor: '))
                        if(value < total):
                            print(f'Para quitar sua divida insira um valor maior ou igual a \033[92mR$ {total}\033[00m')
                        else:
                            error_inp = True
                    except:
                        print('Insira um valor válido')
                    
                    print('Pago!')
                    total -= value
                    if(total < 0):
                        print('Troco: \033[92mR$ ', abs(total), '\033[00m')
                    else:
                        total = float(0)
                        sl_prods = dict()
    
    else:
        print('Não há valores a serem quitados!')


while(True):
    print('''\nComandos:
[1] - Selecionar Produtos
[2] - Ver Produtos
[3] - Ver Total
[4] - Remover Produto do carrinho
[5] - Pagar
[6] - Sair\n''')

    error_inp = False
    while(error_inp == False):
        try:
            select = int(input('Escolher: '))
            if(select < 1 or select > 6):
                print('Insira um comando válido')
            else:
                error_inp = True
        except:
            print('Insira um comando válido')

    match(select):
        case 1:
            select_prods()
        case 2:
            see_prods()
        case 3:
            see_total()
        case 4:
            remove_prod()
        case 5:
            payment()
        case _:
            exit()
    