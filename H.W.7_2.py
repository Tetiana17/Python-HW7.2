def correct_sentence(text):
    # перевіряємо чи починається речення з великої літери
    if text[0].islower():
        text = text[0].upper() + text[1:]
    # перевіряємо чи закінчується речення крапкою
    if text[-1] != '.':
        text += '.'
    return text


# перевірка роботи за допомогою функції
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
