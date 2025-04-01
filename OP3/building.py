import classroom
class AcademicBuilding:
    def __init__(self, adress, classrooms: list):
        '''
        The initializer
        Arrtibutes:
            adress(str), the adress
            classroom

        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.address
        'Kozelnytska st. 2a'
        >>> for room in building.classrooms:
        ...     print(room)
        Classroom 016 has a capacity of 80 persons and has the following \
equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        '''
        self.address = adress
        self.classrooms = classrooms
    def total_equipment(self):
        '''
        Counts the total_equipment
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
        '''
        equipment_count = {}
        for classroom in self.classrooms:
            for equipment in classroom.equipment:
                if equipment in equipment_count:
                    equipment_count[equipment] += 1
                else:
                    equipment_count[equipment] = 1
        # Sort equipment by name
        return sorted(equipment_count.items())
    def __str__(self):
        '''
        The __str__() method, returns a string
        >>> classroom_016 = classroom.Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = classroom.Classroom('007', 12, ['TV'])
        >>> classroom_008 = classroom.Classroom('008', 25, ['PC', 'projector'])
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> print(building)
        Kozelnytska st. 2a
        Classroom 016 has a capacity of 80 persons and has the following \
equipment: PC, projector, mic.
        Classroom 007 has a capacity of 12 persons and has the following equipment: TV.
        Classroom 008 has a capacity of 25 persons and has the following equipment: PC, projector.
        '''
        result = f"{self.address}\n"
        for classroom in self.classrooms:
            result += str(classroom) + "\n"
        return result.strip()

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
