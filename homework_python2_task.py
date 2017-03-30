def case_hundreds_to_string(hundreds):
    h = hundreds
    out_str = ''
    if h == 1:
        out_str = 'one hundred '
    elif h == 2:
        out_str = 'two hundred '
    elif h == 3:
        out_str = 'three hundred '
    elif h == 4:
        out_str = 'four hundred '
    elif h == 5:
        out_str = 'five hundred '
    elif h == 6:
        out_str = 'six hundred '
    elif h == 7:
        out_str = 'seven hundred '
    elif h == 8:
        out_str = 'eight hundred '
    elif h == 9:
        out_str = 'nine hundred '
    return out_str


def case_dozens(dozens):
    d = dozens
    out_str = ''
    if d == 2:
        out_str = 'twenty'
    elif d == 3:
        out_str = 'thirty'
    elif d == 4:
        out_str = 'forty'
    elif d == 5:
        out_str = 'fifty'
    elif d == 6:
        out_str = 'sixty'
    elif d == 7:
        out_str = 'seventy'
    elif d == 8:
        out_str = 'eighty'
    elif d == 9:
        out_str = 'ninety'
    return out_str


def case_custom_to_string(dozens, unit):
    d = dozens
    u = unit
    out_str = ''
    if d == 1 and u == 0:
        out_str = 'ten '
    elif d == 1 and u == 1:
        out_str = 'eleven '
    elif d == 1 and u == 2:
        out_str = 'twelve '
    elif d == 1 and u == 3:
        out_str = 'thirteen '
    return out_str


def unit_to_string(unit):
    u = unit
    out_str = ''
    if u == 1:
        out_str = 'one'
    elif u == 2:
        out_str = 'two'
    elif u == 3:
        out_str = 'three'
    elif u == 4:
        out_str = 'four'
    elif u == 5:
        out_str = 'five'
    elif u == 6:
        out_str = 'six'
    elif u == 7:
        out_str = 'seven'
    elif u == 8:
        out_str = 'eight'
    elif u == 9:
        out_str = 'nine'
    return out_str


def converter(number):
    num = number
    category_list = []
    million = 0
    h_thousands = 0
    d_thousands = 0
    thousands = 0
    hundreds = 0
    dozens = 0
    unit = 0
    out_string = ''

    if num == 0:
        category_list.append('zero')

    if num >= 1000000:
        million = 1
        num -= million * 1000000
        million = 'one million'
        category_list.append(million)
    else:
        category_list.append('zero')

    if num / 100000 == 0:
        num %= 100000
        category_list.append('zero')
    else:
        h_thousands = num / 100000
        num -= h_thousands * 100000
        category_list.append(case_hundreds_to_string(h_thousands))

    if num / 10000 == 0:
        num %= 10000
        category_list.append('zero')
        d_thousands = 0
    else:
        d_thousands = num / 10000
        num -= d_thousands * 10000

    if num / 1000 == 0:
        num %= 1000
        thousands = 0
        category_list.append('zero')
    else:
        thousands = num / 1000
        num -= thousands * 1000

    if 99 >= d_thousands * 10 + thousands >= 20 and thousands != 0:
        category_list.append(case_dozens(d_thousands) + '-' + unit_to_string(thousands) + 'thousands ')
    elif 99 >= d_thousands * 10 + thousands >= 20 and thousands == 0:
        category_list.append(case_dozens(d_thousands) + 'thousands ')
    elif 20 > d_thousands * 10 + thousands > 13:
        category_list.append(unit_to_string(thousands) + 'teen thousands ')
    elif 13 >= d_thousands * 10 + thousands >= 10:
        category_list.append(case_custom_to_string(d_thousands, thousands) + 'thousands ')
    elif 13 >= d_thousands * 10 + thousands >= 10 and million != 1:
        category_list.append(unit_to_string(thousands) + 'thousands ')

    if num / 100 == 0:
        num %= 100
        category_list.append('zero')
    else:
        hundreds = num / 100
        num -= hundreds * 100
        category_list.append(case_hundreds_to_string(hundreds))

    if num / 10 == 0:
        num %= 10
        category_list.append('zero')
        dozens = 0
    else:
        dozens = num / 10
        num -= dozens * 10

    if num / 1 == 0:
        num %= 1
        unit = 0
    else:
        unit = num / 1
        num -= unit * 1

    if 99 >= dozens * 10 + unit >= 20 and unit != 0:
        category_list.append('and ' + case_dozens(dozens) + '-' + unit_to_string(unit))
    elif 99 >= dozens * 10 + unit >= 20 and unit == 0:
        category_list.append('and ' + case_dozens(dozens) + ' ')
    elif 20 > dozens * 10 + unit > 13:
        category_list.append('and ' + unit_to_string(unit) + 'teen ')
    elif 13 >= dozens * 10 + unit >= 10:
        category_list.append('and ' + case_custom_to_string(dozens, unit) + ' ')
    elif 13 >= dozens * 10 + unit >= 10 and million != 1:
        category_list.append('and ' + unit_to_string(unit) + ' ')

    for i in category_list:
        if i != 'zero':
            out_string += i

    print(out_string)


converter(10)
