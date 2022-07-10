def crlib(txt):
    lib = ''
    Ord = 0
    while Ord < 1424:
        lib = lib + chr(Ord)
        Ord = Ord + 1
    with open('d:\GitHubRepository\WorkSpace\Practice at the SBpAU\TextCoding\library.txt', 'w+', encoding='utf-8') as txt:
        txt.write(lib)
    print('Обновление завершено.')


def check(txt):
    cnt = 0
    idx = ''
    print('Всего символов в библиотеке:', len(txt))
    for Ord in range(0, len(txt)):
        if (txt[Ord] != chr(Ord)) and (Ord != 13):
            idx = idx + str(Ord) + ' '
            cnt = cnt + 1
    print('Из них ', cnt,' несовпадений с порядковыми номерами:', idx)

txtfile = open('d:\GitHubRepository\WorkSpace\Practice at the SBpAU\TextCoding\library.txt', 'r', encoding='utf-8')
A = int(input('Обновить библиотеку (кн. 1) или проверить её (кн. 2): '))
if A == 1:
    Q = input('Нажмите enter, чтобы продолжить...')
    crlib(txtfile.read())
    txtfile.close()
if A == 2:
    Q = input('Нажмите enter, чтобы продолжить...')
    check(txtfile.read())
    txtfile.close()
