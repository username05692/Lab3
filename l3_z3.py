sentence = str(input("Введіть речення: "))
words = sentence.split()

for word in words:
    if word.lower().startswith('к'):
        print("Знайдене слово:",word) 
        break 
else:
    print("Слів, що починаються на 'к', не знайдено.")
