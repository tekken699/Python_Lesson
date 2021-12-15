from os import walk, path, listdir
import shutil

name_proj = "my_project"
nana = input('Введите название папки')

try:
    for root, dirs, files in walk(name_proj):
        if 'templates' in dirs:
            for entry in listdir(path.join(root, "templates")):
                shutil.copytree(path.join(root, "templates", entry),
                                path.join(name_proj, nana, entry))
except FileExistsError:
    print("Невозможно создать файл, так как он уже существует")