# Write your code here.

# Task 1
def hello():
    return "Hello!"

# Task 2

def greet(name):
    return f"Hello, {name}!"

#Task 3

def calc(num1, num2, operation="multiply"):
    try:
        match operation:
            case 'add':
                return num1 + num2
            case 'subtract':
                return num1 - num2
            case 'multiply':
                return num1 * num2
            case 'divide':
                try:
                    return num1 / num2
                except ZeroDivisionError:
                    return "You can't divide by 0!"
            case 'modulo':
                return num1 % num2
            case 'int_divide':
                try:
                    return num1 // num2
                except ZeroDivisionError:
                    return "You can't divide by 0!"
            case 'power':
                return num1 ** num2
            case _:
                return f"Error: '{operation}' is an invalid operator!"
    except TypeError:
        return "You can't multiply those values!"
    
# Task 4

def data_type_conversion(value, data_requested):
    match data_requested:
        case "float":
            try:
                return float(value)
            except ValueError:
                return f"You can't convert {value} into a {data_requested}."
        case "str":
            return str(value)
        case "int":
            try:
                return int(value)
            except ValueError:
                return f"You can't convert {value} into a {data_requested}."

#Task 5

def grade(*args):
    try:
        average = sum(args) / len(args)

        if(average >= 90):
            return "A"
        elif(average >= 80):
            return "B"
        elif(average >= 70):
            return "C"
        elif(average >= 60):
            return "D"
        else:
            return "F"
    except TypeError:
        return "Invalid data was provided."

# Task 6

def repeat(string, count):
    result = ""
    for i in range(count):
        result += string
    return result

# Task 7 

def student_scores(score, **kwargs):
    match score:
        case "best":
            return max(kwargs, key=kwargs.get)
        case "mean":
            return sum(kwargs.values()) / len(kwargs)

# Task 8

def titleize(uncapitalized):
    words = uncapitalized.split()
    first_word = words[0].capitalize()
    last_word = words[len(words)-1].capitalize()

    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]

    result = first_word + " "

    for i, word in enumerate(words):
        if(i == 0):
            continue
        if(i == len(words)-1):
            break
        if(word.lower() in little_words):
            result += word.lower() + " "
        else:
            result += word.capitalize() + " "

    return result + last_word

# Task 9

def hangman(secret, guess):
    word = ""

    for letter in secret:
        if(letter in guess):
            word += letter
        else:
            word += "_"
    return word

# Task 10

def pig_latin(text):
    vowels = ['a', 'e', 'i', 'o', 'u']

    words = text.split()
    text = []

    for word in words:
        if(word[0] in vowels):
            text.append(word + "ay")
        elif(word.startswith("qu")):
            text.append(word[2:] + "quay")
        else:
            consonants = ""
            for i, letter in enumerate(word):
                if (not letter in vowels)or(word[i-1] == "q" and word[i] == "u"):
                    consonants += letter
                elif(letter in vowels):
                    break
            text.append(word[len(consonants):] + consonants + "ay")

    return " ".join(text)