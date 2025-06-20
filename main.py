"""
Задание №1

Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
Условия:

    Программа должна быть нечувствительна к регистру.
    Игнорировать пробелы и знаки пунктуации.
Пример использования:
    isPalindrom("level") # True
    isPalindrom("hello") # False

Задание №2

Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
Условия:

    Слова передаются в виде списка через ввод пользователя.
    Программа должна вывести все палиндромы из списка.

Пример использования:
    isPalindromList(["hello", "list", "level"]) # ["level"]

Задание №3

Задание: Написать программу, которая ищет все палиндромы в строке текста.
Условия:

    Программа должна игнорировать регистр и знаки пунктуации.
    Если палиндромы повторяются, выводить их только один раз.

Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]
"""

""""
def isPalindrom(word):
    cleaner_word = word.replace(" ", "").lower()
    reversed_word = cleaner_word[::-1]
    return reversed_word == cleaner_word
a = input("Попробуй угадать слово...")
if isPalindrom(a):
    print("Палиндром")
else:
    print("не Палиндром") """



"""def isPalindrom(word):
    cleaner_word =  word.replace(" ", " ").lower()
    reversed_word = cleaner_word[::-1]
    return reversed_word == cleaner_word

a = list(["level", "word", "table", "music", "madam"])

def isPalindromList(words):
    Palindroms = []
    for word in words:
        if isPalindrom(word):
            Palindroms.append(word)
    return Palindroms
    
print(a)    
print(isPalindromList(a))"""


"""def punctuation(string):
    punctuation = "!\"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"
    result = ""

    for char in string:
        if char not in punctuation:
            result += char

    return result

def isPalindrom(words):
    cleaner_word = words.replace(" ", "").lower()
    reversed_word = cleaner_word[::-1]
    return reversed_word == cleaner_word

def isPalindromList(words):
    palindroms = []
    for word in words:
        if isPalindrom(word):
            palindroms.append(word)
    return palindroms

def isPalindromString(string):
    clean_string = punctuation(string)
    words = clean_string.split()
    print(words)
    palindromes = isPalindromList(words)
    return palindromes

print(isPalindromString("Madam, Anna went to the civic center"))"""



