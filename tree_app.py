import re

# The function with two async one step shift generatots
def binary_tree_maker(list):
    '''
    The function with two one step shift generators
    Takes argument list of things... Enjoy!
    '''
    def generator(list):
        for x in list:
            yield x
    for i in generator(list):
        result_conteiner = []
        last_box = i
        for j in generator(list):
            if j == None or last_box == None:
                print(j, "Root / Split tree :", last_box, 'The Root of the Tree')
                result = ({'Input': last_box}, {'Root': j})
                result_conteiner.append(result)
                last_box = j
            elif j > last_box:
                print(j, 'Bigger than', last_box, 'Go Right !')
                result = ({'Input': last_box}, {'Right OUT': j})
                result_conteiner.append(result)
                last_box = j
            elif j < last_box:
                print(j, 'less than', last_box, 'Go Left !')
                result = ({'Input': last_box}, {'Left OUT': j})
                result_conteiner.append(result)
                last_box = j
            elif j == last_box:
                print(j, "Root Side(or split) :", last_box, 'The Root of the Tree')
                result = ({'Input': last_box}, {'Root': j})
                result_conteiner.append(result)
                last_box = j

        print('The end is:', last_box, 'That\'s why this is a Leaf')
        result = ({'Input': last_box}, {'Leaf': None})
        result_conteiner.append(result)
        for item in result_conteiner:
            print(item)
        break
# - here is some data
source = [
    (None, 'a'),
    (None, 'b'),
    (None, 'c'),
    ('a', 'a1'),
    ('a', 'a2'),
    ('a2', 'a21'),
    ('a2', 'a22'),
    ('b', 'b1'),
    ('b1', 'b11'),
    ('b11', 'b111'),
    ('b', 'b2'),
    ('c', 'c1'),
]
# Here is SUPER list !
list1 = [1,4,6,8,45,45,34,None,2,76,34,7,4,789,765,123,87,4,3,67,None,43,87,23,75,]
# Here is cleaning data option
cleaned = re.findall("[\d{9}]", str(source))


# Usability - Put your argument in brackets(your_list_of_stuff) and run the function:

binary_tree_maker(list1)







