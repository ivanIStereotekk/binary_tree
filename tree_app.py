
list = [1,4,6,8,45,34,2,76,34,7,4]
#cleaned = re.findall("[\d{9}]", str(*args))


def generator(list):
    for i in list:
        yield i

for i in generator(list):
    result_conteiner = []
    last_box = i
    for j in generator(list):
        if j > last_box:
            print(j,'Bigger than',last_box,'Go Right !')
            result = ({'Input':last_box},{'right':j})
            result_conteiner.append(result)
            last_box = j
        elif j < last_box:
            print(j, 'less than', last_box,'Go Left !')
            result = ({'Input': last_box}, {'left':j})
            result_conteiner.append(result)
            last_box = j
        elif j == last_box:
            print(j,"Root Side :",last_box,'The Beggining of Tree')
            last_box = j
    print('The end is:',last_box,'That\'s why this is a Leaf')
    result = ({'Input': last_box}, {'Leaf': None})
    result_conteiner.append(result)
    for item in result_conteiner:
        print(item)
    break










