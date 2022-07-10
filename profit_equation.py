def profit(Currency, buysell, sellbuy, border):
    if (buysell <= sellbuy <= border) or (buysell >= sellbuy >= border):
        exit('Недопустимые исходные данные!')
    s = round(Currency * (border - buysell) / (sellbuy - border), 2)
    if s > 0:
        exit(print('Надо купить:', s, 'ед. валюты'))
    if s < 0:
        exit(print('Надо продать:', abs(s), 'ед. валюты'))
    else:
        exit(print('Вам ничего делать не надо :)'))


profit(float(input('Сколько у вас валюты изначально? ')),
    float(input('По какому курсу к рублю вы купили эту валюту? ')),
    float(input('Какой биржевой курс ин. валюты по отношению к рублю сейчас? ')),
    float(input('Какой переходный курс между прибылью и убылью вы хотите? ')))
