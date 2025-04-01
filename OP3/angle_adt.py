import math

class AngleADT:
    HEX_DIGITS = "0123456789ABCDEF"
    STEP_ANGLE = 360 / 16  # Кожна цифра має рівний кутовий крок
    
    def __init__(self):
        """Ініціалізація AngleADT"""
        self.angles = []
        
    def _char_to_hex(self, char):
        """Конвертує символ у дві шістнадцяткові цифри"""
        hex_repr = f"{ord(char):02X}"
        return hex_repr
    
    def _hex_to_angle(self, hex_digit):
        """Конвертує шістнадцяткову цифру у відповідний кут"""
        return self.HEX_DIGITS.index(hex_digit) * self.STEP_ANGLE
    
    def encode_message(self, message):
        """Кодує повідомлення у список відносних кутів"""
        angles = []
        current_angle = 0  # Початкове положення
        
        for char in message:
            hex_digits = self._char_to_hex(char)  # Отримуємо дві шістнадцяткові цифри
            
            for hex_digit in hex_digits:
                target_angle = self._hex_to_angle(hex_digit)
                relative_angle = target_angle - current_angle
                
                # Якщо два однакових кути підряд - робимо повний оберт
                if relative_angle == 0:
                    angles.append(360.0)
                else:
                    angles.append(relative_angle)
                
                current_angle = target_angle
        
        return angles

# Приклад використання
encoder = AngleADT()
message1 = "hello"
message2 = "1 січня"

angles1 = encoder.encode_message(message1)
angles2 = encoder.encode_message(message2)

print(angles1)
print(angles2)