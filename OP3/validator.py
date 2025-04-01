import re
class Validator:
    def validate_name_surname(self, name_surname: str):
        correct = r"^[A-Z][a-z]{1,29} [A-Z][a-z]{1,29}+$"
        return bool(re.fullmatch(correct, name_surname))
    def validate_age(self, age: str):
        correct = r"^(1[6-9]|[2-9][0-9])$"
        return bool(re.fullmatch(correct, age))
    def validate_country(self, country: str):
        correct = r"^[A-Z][a-zA-Z]{1,9}$"
        return bool(re.fullmatch(correct, country))
    def validate_region(self, region: str):
        correct = r"^[A-Z][a-z0-9]{1,9}$"
        return bool(re.fullmatch(correct, region))
    def validate_living_place(self, living_place: str):
        correct = r"^[A-Z][a-zA-Z]{2,19} (st\.|av\.|prosp\.|rd\.) \d[a-z0-9]$"
        return bool(re.fullmatch(correct, living_place))
    def validate_index(self, index: str):
        correct = r"[0-9]{5}"
        return bool(re.fullmatch(correct, index))
    def validate_phone(self, phone: str):
        correct = r"^\+(\d{9,12}|\d{2} \(\d{3}\) \d{3}-\d{2}-\d{2})$"
        return bool(re.fullmatch(correct, phone))

    def validate_email(self, email: str):
        correct = (
            r"^[a-zA-Z0-9!#$%&'*+/=?^_`{|}~]"  # first character must be valid
            r"(?:[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]{0,62}"  # allowed characters
            r"[a-zA-Z0-9!#$%&'*+/=?^_`{|}~])?"  # Cannot end with a dot
            r"@"  # @ symbol
            r"[a-z0-9]+"  # Domain name
            r"(?:\.[a-z0-9]+)*"  # ucu.edu.ua
            r"\.(com|org|edu|gov|net|ua)$"  # Allowed TLDs
        )
        return bool(re.fullmatch(correct, email))

    def validate_id(self, id: str):
        correct = r"^\d{6}$"
        if not re.fullmatch(correct, id):
            return False
        return id.count('0') == 1

    
    def validate(self, data: str):
        # pattern = r'[A-Z][a-z]+(,|, |;|; )\d(,|, |;|; )[A-Z][a-z]+(,|, |;|; )'
        # return bool(re.fullmatch(pattern, data))
        parts = re.split(r'\s*(?:,|;)\s*', data)
        if len(parts) == 9:
            name_surname = parts[0]
            age = parts[1]
            country = parts[2]
            region = parts[3]
            living_place = parts[4]
            index = parts[5]
            phone = parts[6]
            email = parts[7]
            id = parts[8]
            return (
                self.validate_name_surname(name_surname)
                and self.validate_age(age)
                and self.validate_country(country)
                and self.validate_region(region)
                and self.validate_living_place(living_place)
                and self.validate_index(index)
                and self.validate_phone(phone)
                and self.validate_email(email)
                and self.validate_id(id)
            )
        return False



if __name__ == '__main__':
    valid = Validator()

    # name and surname
    assert valid.validate_name_surname("Elvis Presley") is True

    # should be only 2 words
    assert valid.validate_name_surname("ElvisPresley") is False
    assert valid.validate_name_surname("Elvis Presley forever") is False

    # should be only first uppercase letter in name and surname
    assert valid.validate_name_surname("elvis Presley") is False
    assert valid.validate_name_surname("Elvis presley") is False
    assert valid.validate_name_surname("Elvis PResley") is False

    # size of both name and surname should be between 2 and 30
    assert valid.validate_name_surname("Elvis Presleyqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq") is False
    assert valid.validate_name_surname("Elvis P") is False

    #no digits or punctuation in name or surname
    assert valid.validate_name_surname("Elvis P,resley") is False
    assert valid.validate_name_surname("El1vis Presley") is False

    # valid age is a number between 16 and 99
    assert valid.validate_age("20") is True
    assert valid.validate_age("7") is False
    assert valid.validate_age("100") is False
    assert valid.validate_age("20.") is False
    assert valid.validate_age("20a") is False

    # valid country name - between 2 and 10 chars,
    # first letter should be uppercase, can`t contain digits
    assert valid.validate_country("Ukraine") is True
    assert valid.validate_country("U") is False
    assert valid.validate_country("UUUUUUUUUUUUUUUUUUUUUUU") is False
    assert valid.validate_country("Ukraine1") is False
    assert valid.validate_country("ukraine") is False
    assert valid.validate_country("USA") is True

    # valid region name - the same as country,
    # but can contain numbers
    assert valid.validate_region("Lviv") is True
    assert valid.validate_region("Lviv1") is True
    assert valid.validate_region("L") is False
    assert valid.validate_region("lviv") is False

    # living place name - should be in format:
    # "Koselnytska st. 2a"
    # name of street - between 3 and 20 chars,
    # first character uppercase, no digits in it
    # type of street - should be "st.", "av.", "prosp." or "rd."
    # number of building - exactly 2 symbols,
    # the first should be a digit,
    # the second can be a digit or small letter
    assert valid.validate_living_place("Koselnytska st. 2a") is True
    assert valid.validate_living_place("koselnytska st. 2a") is False
    assert valid.validate_living_place("Koselnytska provulok 2a") is False
    assert valid.validate_living_place("Koselnytska st. 2") is False
    assert valid.validate_living_place("Koselnytska st. a2") is False
    assert valid.validate_living_place("Koselnytska st. 22") is True

    # valid index - exactly 5 digits
    assert valid.validate_index("79000") is True
    assert valid.validate_index("7900") is False
    assert valid.validate_index("790000") is False
    assert valid.validate_index("7900q") is False
    assert valid.validate_index("790 00") is False

    # valid phone number - in format "+380951234567" 
    # or "+38 (095) 123-45-67"
    # starts wit "+" and has from 9 to 12 numbers
    assert valid.validate_phone("+380951234567") is True
    assert valid.validate_phone("+38 (095) 123-45-67") is True
    assert valid.validate_phone("38 (095) 123-45-67") is False
    assert valid.validate_phone("380951234567") is False
    assert valid.validate_phone("-380951234567") is False
    assert valid.validate_phone("+3810951234567") is False
    assert valid.validate_phone("+20951234567") is True

    # valid email should be in format "username@domain.type"
    # username - any letters, digits, any of "!#$%&'*+-/=?^_`{|}~", 
    # dots (provided that it is not the first or last
    # character and provided also that it does not appear consecutively), 
    # at least 1, at most 64
    # domain - only lowercase letters, at least 1, at most 255, but
    # be careful - can be also "." - for example @ucu.edu.ua
    # type : "com", "org", "edu", "gov", "net", "ua"
    assert valid.validate_email("username@domain.com") is True
    assert valid.validate_email("username+usersurname@domain.com") is True
    assert valid.validate_email("username@ucu.edu.ua") is True
    assert valid.validate_email("usernamedomain.com") is False
    assert valid.validate_email("username@domaincom") is False
    assert valid.validate_email("username@domain.aaa") is False
    assert valid.validate_email("username@aaa") is False
    assert valid.validate_email("@domain.com") is False

    # valid id - exactly 6 digits, but should contain exactly one zero - at any position
    assert valid.validate_id("123450") is True
    assert valid.validate_id("011111") is True
    assert valid.validate_id("123456") is False
    assert valid.validate_id("123006") is False
    assert valid.validate_id("1230916") is False
    assert valid.validate_id("12306") is False

    # data - string in format "name_surname,age,country,region,living_place,index,phone,email,id"
    # can also be whitespaces between sections and allowed separator as ";"
    # all previous criteria are valid
    assert valid.validate("Elvis Presley,20,Ukraine,Lviv,Koselnytska st. 2a,79000,+380951234567,username@domain.com,123450") is True
    assert valid.validate("Elvis Presley;20;Ukraine;Lviv;Koselnytska st. 2a;79000;+380951234567;username@domain.com;123450") is True
    assert valid.validate("Elvis Presley; 20; Ukraine; Lviv; Koselnytska st. 2a; 79000; +380951234567; username@domain.com; 123450") is True
    assert valid.validate("Elvis Presley, 20, Ukraine, Lviv, Koselnytska st. 2a, 79000, +380951234567, username@domain.com, 123450") is True
# pattern = r'[050]{3}[-.]\d{3}[-.]\d{2}[-/]\d{2}'
# inp = input()
# print(bool(re.fullmatch(pattern, inp)))