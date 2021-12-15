import os
path = r"C:\Users\Юрий\pythonProject15"
name_dir = 'my_project'
folders = ['settings', 'mainapp', 'adminapp', 'authapp']

full_path = os.path.join(path, name_dir)


def create_folder(path):
    if not os.path.exists(path):
        os.mkdir(path)


create_folder(full_path)


for f in folders:
    folder = os.path.join(full_path, f)
    create_folder(folder)