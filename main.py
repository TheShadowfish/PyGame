import string



numbers = ''.join([str(num) for num in range(10)])



#  создаем строку `letters`, содержащую маленькие буквы от a до #  z, используя метод `string.ascii_lowercase` из модуля `string`.

# numbers = ' '.join([string.digits, string.ascii_lowercase])
letters = ''

let2 = string.ascii_letters
let3 = string.digits

numbers = string.digits + ' ' + string.ascii_lowercase

# Не удаляйте код ниже: он нужен для проверки.



print(numbers, letters)