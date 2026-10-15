import os

# Это классическая рекурсивная функция, которая обходит дерево каталогов и собирает три числа: размер, количество папок, количество файлов

def scan(path):
    size = 0        
    dirs_count = 0    
    files_count = 0 

    for name in os.listdir(path):
        full_path = os.path.join(path, name)

        if os.path.isdir(full_path):
            dirs_count += 1
            s, d, f = scan(full_path)
            size += s
            dirs_count  += d
            files_count += f
        else:
            files_count += 1
            size += os.path.getsize(full_path)
    return size, dirs_count, files_count

path = '/Users/simba/Desktop/Python_Basic/Module22/'
print(path)

size, dirs_count, files_count = scan(path)

print('Размер каталога (в Кб): ', round(size / 1024, 2))
print('Количество подкаталогов: ', dirs_count)
print('Количество файлов: ', files_count)
      
