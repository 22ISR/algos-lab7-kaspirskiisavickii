# Задание №1

# Задание: Написать программу, которая принимает на вход слово и проверяет, является ли оно палиндромом.
# Условия:

#     Программа должна быть нечувствительна к регистру.
#     Игнорировать пробелы и знаки пунктуации.
# Пример использования:
#     isPalindrom("level") # True
#     isPalindrom("hello") # False

def isPalindrom(word):
    word_lower = word.lower()
    
    cl_word = ""
    for a in word_lower:
        if a.isalnum():
            cl_word += a
    
    return cl_word == cl_word[::-1]
print(isPalindrom("level"))
print(isPalindrom("hello"))


# Задание №2

# Задание: Написать программу, которая принимает список слов и проверяет, какие из них являются палиндромами.
# Условия:

#     Слова передаются в виде списка через ввод пользователя.
#     Программа должна вывести все палиндромы из списка.

# Пример использования:
#     isPalindromList(["hello", "list", "level"]) # ["level"]

def is_palindromchik(word):
    word = word.lower()
    word = word.replace(" ", "")
    return word == word[::-1]

def palindrom_list(word_list):
    palindromes = []
    for word in word_list:
        if is_palindromchik(word):
            palindromes.append(word)
    return palindromes

my_words = ["hello", "list", "level"]
print(palindrom_list(my_words))

# Задание №3

# Задание: Написать программу, которая ищет все палиндромы в строке текста.
# Условия:

#     Программа должна игнорировать регистр и знаки пунктуации.
#     Если палиндромы повторяются, выводить их только один раз.

# Пример использования isPalindromString("Madam, Anna went to the civic center") # ["madam", "anna", "civic"]

def isPalindromString(text):
    text = text.lower()
    words = text.split()
    
    resul = []
    for word in words:
        clean_words= word.strip(",.!?;:-'\"")
        if len(clean_words) > 1 and clean_words == clean_words[::-1]:
            if clean_words not in resul:
                resul.append(clean_words)
    
    return resul

print(isPalindromString("Madam, Anna went to the civic center"))  
