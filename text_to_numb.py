NUMBS = {
    'один': 1, 'одна': 1, 'одно': 1, 'два': 2, 'две': 2, 'три': 3, 'четыре': 4, 'пять': 5,
    'шесть': 6, 'семь': 7, 'восемь': 8, 'девять': 9, 'десять': 10,
    'одинадцать': 11, 'двенадцать': 12, 'тринадцать': 13, 'четырнадцать': 14, 'пятнадцать': 15,
    'шестнадцать': 16, 'семнадцать': 17, 'восемнадцать': 18, 'девятнадцать': 19, 'двадцать': 20,
    'тридцать': 30, 'сорок': 40, 'пятьдесят': 50, 'шестьдесят': 60, 'семьдесят': 70, 'восемьдесят': 80, 'девяносто': 90
}

H_M_S = {'час': 'h', 'часа': 'h', 'часов': 'h',
         'минута': 'm', 'минуты': 'm', 'минут': 'm', 'минуту': 'm',
         'секунда': 's', 'секунды': 's', 'секунд': 's', 'секунду': 's'}

t = 'секунда'


def tex_to_num(text):
    phrase = text.split(' ')
    print(phrase)
    time_dic = {}
    num = 0
    for word in phrase:
        if word in NUMBS:
            if num == 0 or ((num % 10) == 0 and NUMBS[word] < 10):
                num += NUMBS[word]
        elif word in H_M_S:
            if num == 0:
                num = 1
            time_dic[H_M_S[word]] = num
            num = 0
    if time_dic:
        return time_dic
    else:
        return None

