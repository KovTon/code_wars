def remove(s):
    txt_split = s.split(' ')
    # for "!" in txt_split:
    #     if count('!') = 1:
            
    
    
    pass


s = "Hi!!!! !Hi! Hi! Hi Hi!! Hi! ! !! !"
txt_split = s.split(' ')
# print(txt_split)
# for i in txt_split:
#     if "!!" in txt_split:
#         txt_split.pop()
# print(txt_split)

# print(txt_split)
# for i in txt_split:
#     if "!" in txt_split:
#         print


print(txt_split)
print('Это число items в списке?:', txt_split.count('!!'))
print('Это число items в первом элементе?:', txt_split[0].count("!"))
number_of_exclam = []
for i in txt_split:
    number_of_exclam.append(txt_split.count('!!'))
# я понял что цикл перебирает элементы в txt_split, а не В элементах txt_split.
# https://www.codewars.com/kata/57fafb6d2b5314c839000195/train/python
print(number_of_exclam)
