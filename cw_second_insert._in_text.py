txt = 'Helo wlord!'
symbol = 'l'


def second_symbol(txt, symbol):
    first_ind_symbol_in_txt = txt.find(symbol)
    answer = txt.find(symbol, first_ind_symbol_in_txt, len(txt + 1))
    return answer


# # print(second_symbol(txt, symbol))
# first_ind_symbol_in_txt = txt.find(symbol)
# answer = txt.find(symbol, first_ind_symbol_in_txt + 1, len(txt) + 1)
# print(answer)

# print(second_symbol(txt, symbol))
first_ind_symbol_in_txt = txt.find(symbol)
answer = txt.find(symbol, txt.find(symbol) + 1, len(txt) + 1)
print(answer)
