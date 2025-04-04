import os
import shutil
import string


def list_dir_files(path):
    dirs = [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]
    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    all_items = os.listdir(path)
    return dirs, files, all_items


def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)
    return exists, readable, writable, executable


def analyze_path(path):
    if os.path.exists(path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)
        return True, filename, directory
    return False, None, None


def count_lines(file_path):
    with open(file_path, "r") as file:
        return len(file.readlines())


def write_list_to_file(file_path, data_list):
    with open(file_path, "w") as file:
        file.writelines(f"{item}\n" for item in data_list)


def create_alphabet_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", "w") as file:
            file.write(f"This is file {letter}.txt")


def copy_file(src_path, dst_path):
    shutil.copyfile(src_path, dst_path)


def delete_file(path):
    if not os.path.exists(path):
        print(f"Ошибка: Путь {path} не существует")
        return
    if not os.access(path, os.W_OK):
        print(f"Ошибка: Нет прав на запись для {path}")
        return
    os.remove(path)
    print(f"Файл {path} удалён")
    
if __name__ == "__main__":
    path = "."
    dirs, files, all_items = list_dir_files(path)
    print(f"Директории: {dirs}")
    print(f"Файлы: {files}")
    print(f"Все элементы: {all_items}\n")


    test_path = "test.txt"
    with open(test_path, "w") as f:
        f.write("Тестовый файл")
    exists, readable, writable, executable = check_path_access(test_path)
    print(f"Путь: {test_path}")
    print(f"Существует: {exists}")
    print(f"Читаемый: {readable}")
    print(f"Записываемый: {writable}")
    print(f"Исполняемый: {executable}\n")


    sample_path = "folder/test.txt"
    exists, filename, directory = analyze_path(test_path)
    if exists:
        print(f"Путь существует")
        print(f"Имя файла: {filename}")
        print(f"Директория: {directory}")
    else:
        print(f"Путь {sample_path} не существует\n")


    with open(test_path, "w") as f:
        f.write("Line 1\nLine 2\nLine 3")
    lines = count_lines(test_path)
    print(f"Количество строк в {test_path}: {lines}\n")

    my_list = ["apple", "banana", "orange"]
    list_file = "list.txt"
    write_list_to_file(list_file, my_list)
    print(f"Список записан в {list_file}\n")


    create_alphabet_files()
    print("Создано 26 файлов от A.txt до Z.txt\n")


    src = "test.txt"
    dst = "test_copy.txt"
    copy_file(src, dst)
    print(f"Содержимое {src} скопировано в {dst}\n")


    delete_file(test_path)

