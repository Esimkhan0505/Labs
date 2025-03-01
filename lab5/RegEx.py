import re

# Проверяет, содержит ли строка 'a', за которой следует ноль или более 'b'
print(bool(re.fullmatch(r'a*b*', "abbb")))  # True

# Проверяет, содержит ли строка 'a', за которой следует две или три 'b'
print(bool(re.fullmatch(r'ab{2,3}', "abb")))  # True

# Находит последовательности строчных букв, соединённых символом подчеркивания
print(re.findall(r'\b[a-z]+_[a-z]+\b', "hello_world test_example"))  # ['hello_world', 'test_example']

# Находит последовательности, начинающиеся с одной заглавной буквы, за которой следуют строчные буквы
print(re.findall(r'[A-Z][a-z]+', "Hello World ThisIsA Test"))  # ['Hello', 'World', 'This', 'Test']

# Проверяет, содержит ли строка 'a', за которой следует любое количество символов, оканчиваясь на 'b'
print(bool(re.fullmatch(r'a.*b', "acb")))  # True

# Заменяет все пробелы, запятые и точки на двоеточия
print(re.sub(r'[ ,.]', ':', "Hello, world. How are you?"))  # 'Hello:world:How:are:you?'

# Преобразует строку в snake_case в camelCase
print(''.join(word.capitalize() for word in "hello_world_example".split('_')))  # 'HelloWorldExample'

# Разбивает строку в местах появления заглавных букв
print(re.split(r'(?=[A-Z])', "SplitAtUppercaseLetters"))  # ['Split', 'At', 'Uppercase', 'Letters']

# Вставляет пробелы между словами, начинающимися с заглавных букв
print(re.sub(r'(?<!^)(?=[A-Z])', ' ', "InsertSpacesBetweenWords"))  # 'Insert Spaces Between Words'

# Преобразует строку из camelCase в snake_case
print(re.sub(r'(?<!^)(?=[A-Z])', '_', "CamelCaseToSnake").lower())  # 'camel_case_to_snake'
