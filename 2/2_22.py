f = open('file.txt', 'a', encoding='utf-8')
f.write('Меня зовут Олег\n')
for i in range(5):
    f.write('А как зовут тебя?\n')
f.close()
