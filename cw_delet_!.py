# https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python
# Пример с сайта. Внутри join генератор. Это не list comprehension

s = "Hi!!!! !Hi! Hi! Hi Hi!! Hi! ! !! !"


def remove_best(s):
    return ' '.join(w for w in s.split(' ') if w.count('!') != 1)


def remove(text):
    txt_split = text.split(' ')
    result = []
    for word in txt_split:
        amount_of_exclamation = word.count('!')
        if amount_of_exclamation != 1:
            result.append(word)
    return ' '.join(result)


print(remove(s))
