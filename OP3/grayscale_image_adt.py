# def compress(aaisc_string:str):
#     lst = []
#     dicti = {}
#     letter_list = list(aaisc_string)
#     for letter in aaisc_string:
#         lst.append(ord(letter))
    
#     for code, letter in list(zip(lst, letter_list)):
#         if letter not in dicti:
            
#     return dicti
# print(compress('geekific'))


# def compress(aaisc_string: str):
#     lst = []
#     dicti = {}
#     output = []
#     letter_list = list(aaisc_string)

#     for letter in aaisc_string:
#         lst.append(ord(letter))


#     for key, index in dicti.keys():
#         for value in dicti.values():
#             if ord(key[index] + key[index+1]) not in output:
#                 output.append(ord(key[index] + key[index+1]))
#             else:
#                 output.append(ord(key))
    

#     # for code, letter in list(zip(lst, letter_list)):
#     #     if letter not in dicti:
#     #         dicti[letter] = code

#     return output

# print(compress('geekific'))




def lzw_compression(dlist):
    # Стиснення за допомогою алгоритму LZW
    # Ініціалізація словника: мапуємо символи на їх ASCII-коди
    dictionary = {chr(i): i for i in range(256)}  # ASCII символи 0-255
    dict_size = 256  # Початковий розмір словника
    result = []
    w = ""

    # Пройдемо через кожен символ (число) в дводименшому масиві dlist
    for row in range(len(dlist)):
        for col in range(len(dlist[0])):
            symbol = chr(dlist[row][col])  # Використовуємо символ, що відповідає числу
            
            # Перевіряємо, чи є комбінація в словнику
            if w + symbol in dictionary:
                w = w + symbol  # Якщо є, продовжуємо з цим символом
            else:
                result.append(dictionary[w])  # Додаємо код попереднього слова
                dictionary[w + symbol] = dict_size  # Додаємо нову комбінацію в словник
                dict_size += 1
                w = symbol  # Починаємо новий символ

    # Додаємо залишок
    if w:
        result.append(dictionary[w])

    return result

# Тестування функції
dlist = [
    [65, 66, 67],  # 'A', 'B', 'C'
    [65, 68, 69],  # 'A', 'D', 'E'
    [70, 71, 72]   # 'F', 'G', 'H'
]

compressed = lzw_compression(dlist)
print("Compressed data:", compressed)
