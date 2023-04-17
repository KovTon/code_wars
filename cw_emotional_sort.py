# - 1 Добавили type hinting для параметра raw_emotion_list
# - 2 Изменили raw_string_of_elements на [str] * 3 (Изменили метод создания
# одинаковых эмодзи. Теперь это [':D'] * raw_emotion_list.count(':D').
# - 3 Изменили вид основного условного выражения с if order == True на if order

def sort_emotions(raw_emotion_list: list[str], order: bool):
    sorted_emotion_list = []
    if order:
        if (emoji := ':D') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':)') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':|') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':(') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := 'T_T') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
    else:
        if (emoji := 'T_T') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':(') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':|') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':)') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
        if (emoji := ':D') in raw_emotion_list:
            sorted_emotion_list.extend([emoji] * raw_emotion_list.count(emoji))
    return sorted_emotion_list


raw_emotion_list = [
    'T_T', ':)', ':D', ':)', ':|', ':)', ':(', ':D', ':D', ':)'
    ]
print(sort_emotions(raw_emotion_list, True))
print(sort_emotions(raw_emotion_list, False))
