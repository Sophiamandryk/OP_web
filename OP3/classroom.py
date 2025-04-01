'''
The class holds informations about the particular classroom
'''
class Classroom:
    """
    Classroom class, responsible for holding info about the classroom
    Attributes: 
    number(str), the class sumber
    capacity(int), the max people the classroom contains
    equipment(list), the equipment in the classroom
    other_classroom(Classroom), the classroom for comparison
    Methods:
    __str__():
        returns a string
    __repr__():
        returns info for the developer to easier debug
    is_larger():
        determines whether the first classroom is bigger
    equipment_differences():
        determines the differences in equipment in two places
    """

    def __init__(self, number, capacity, equipment:list):
        '''
        The initializer

        Attributes: 
        number(str), the class sumber
        capacity(int), the max people the classroom contains
        equipment(list), the equipment in the classroom
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016.number
        '016'
        >>> classroom_016.capacity
        80
        >>> classroom_016.equipment
        ['PC', 'projector', 'mic']
        '''
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        '''
        The __str__ method

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> print(classroom_016)
        Classroom 016 has a capacity of 80 persons and has the following equipment: PC, \
projector, mic.
        '''
        capacity_str = ', '.join(self.equipment)
        return f'Classroom {self.number} has a capacity of {self.capacity} persons and \
has the following equipment: {capacity_str}.'
    def is_larger(self, other_classroom):
        '''
        Determines whether the first classroom is bigger
        Attributes:
        other_classroom(Classroom), the classroom for comparison
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        '''
        assert isinstance(other_classroom, Classroom)
        return self.capacity > other_classroom.capacity
    def equipment_differences(self,other_classroom):
        '''
        Determines the differences in equipment in two places
        Attributes:
        other_classroom(Classroom), the classroom for comparison
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'mic', 'projector']
        '''
        lst = self.equipment.copy()
        for i in self.equipment:
            if i in other_classroom.equipment:
                lst.remove(i)
        return sorted(lst)
    def __repr__(self):
        """
        Returns a string representation of the object for a developer.

        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_016
        Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> [classroom_016]
        [Classroom('016', 80, ['PC', 'projector', 'mic'])]
        """
        return f"Classroom('{self.number}', {self.capacity}, {self.equipment})"
if __name__ == '__main__':
    import doctest
    print(doctest.testmod())


# class AcademicBuilding:
#     def __init__(self, adress, classrooms: list):
#         '''
#         The initializer
#         Arrtibutes:
#             adress(str), the adress
#             classroom

#         >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
#         >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
#         >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
#         >>> classrooms = [classroom_016, classroom_007, classroom_008]
#         >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
#         >>> building.address
#         'Kozelnytska st. 2a'
#         >>> for room in building.classrooms:
#         ...     print(room)
#         Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
#         Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
#         Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
#         '''
#         self.address = adress
#         self.classrooms = classrooms
#     def total_equipment(self):
#         '''
#         Counts the total_equipment
        
#         >>> classrooms = [classroom_016, classroom_007, classroom_008]
#         >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
#         >>> building.total_equipment()
#         [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
#         '''
#         equipment_count = {}
#         for classroom in self.classrooms:
#             for equipment in classroom.equipment:
#                 if equipment in equipment_count:
#                     equipment_count[equipment] += 1
#                 else:
#                     equipment_count[equipment] = 1
#         # Sort equipment by name
#         return sorted(equipment_count.items())
#     def __str__(self):
#         '''
#         The __str__() method, returns a string
#         >>> classrooms = [classroom_016, classroom_007, classroom_008]
#         >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
#         >>> print(building)
#         Kozelnytska st. 2a
#         Classroom 016 has a capacity of 80 persons and has the following equipment: PC, projector, mic.
#         Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
#         Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
#         '''
#         result = f"{self.address}\n"
#         for classroom in self.classrooms:
#             result += str(classroom) + "\n"
#         return result.strip()

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())

# classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
# classroom_007 = Classroom('007', 12, ['TV'])
# classroom_008 = Classroom('008', 25, ['PC', 'projector'])
# classrooms = [classroom_016, classroom_007, classroom_008]
# building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
# print(building)
# print(building)
# print(building.adress)
# for  room in building.classrooms:
#     print(room)
# print(classrooms)

# lst  = [('LA', 2), ('PP', 4), ('OP', 2)]
# print(lst[0][0])
# classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
# classroom_07 = Classroom('62', 12,['PC', 'lala', 'mlalaic'])
# print(classroom_016)
# як вивести __repr__?