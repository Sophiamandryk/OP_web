# class Question:
#     '''Questions Class'''
#     def __init__(self, text, answer):
#         '''The initializer'''
#         self.text = text
#         self.answer = answer
#     def __str__(self):
#         '''Returns a visual representation'''
#         return f'{self.__class__.__name__}: {self.text}'
#     def check_answer(self, user_answer):
#         '''Checks whether the answers are correct'''
#         return self.answer == user_answer
    


# from collections.abc import Iterable, Hashable

# class Test(Iterable, Hashable):
#     def __iter__(self):
#         return iter([])  # Порожній ітератор

#     def __hash__(self):
#         return hash(id(self))  # Унікальний хеш для кожного об'єкта

# # Перевірка
# test = Test()
# print(isinstance(test, Iterable))  # True
# print(isinstance(test, Hashable))  # True

# class Appliance:
#     def operate(self):
#         pass
# class WashingMachine(Appliance):
#     def operate(self):
#         print("Washing clothes")
# class Refrigerator(Appliance):
#     def operate(self):
#         print("Cooling food")
# class Oven(Appliance):
#     def operate(self):
#         print("Baking food")
# washing_machine = WashingMachine()
# refrigerator = Refrigerator()
# oven = Oven()

# # Виклик методу operate() для кожного об'єкта
# washing_machine.operate()
# refrigerator.operate()
# oven.operate()

# # Перевірка наслідування
# print(isinstance(washing_machine, Appliance))
# print(isinstance(refrigerator, Appliance))
# print(isinstance(oven, Appliance))


# from collections.abc import Container, Sized
# class Test(Container, Sized):
#     def __contains__(self, item):
#         return False
    
#     def __len__(self):
#         return 0
# test = Test()
# print(isinstance(test, Container))
# print(isinstance(test, Sized))


import re
string = 'abcabcabc'
pattern = r'...'
matches = re.findall(pattern, string)
print(matches)