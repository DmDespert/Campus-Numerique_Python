import os
import shutil


def add_text(text):
    with open('readme.txt', 'w') as file:
        file.write(text)


def edit_file(file, filename):
    os.rename(file, filename)
    print("edited", filename)


def binary_file():
    with open('test.bin', 'w+b') as file:
        byte_array = [120, 3, 255, 0, 100]
        binary_format = bytearray(byte_array)
        file.write(binary_format)


def text_file():
    add_text("Hello world !!")
    edit_file("readme.txt", "readed.txt")


def create_folder(name, file):
    os.mkdir(name)
    with open(file, 'w') as f:
        f.write("Hello world! \n i'm \n a \n new \n peon")
    src_path = r"/Volumes/DATA/websites/Campus/Python/J1/" + file
    dst_path = r"/Volumes/DATA/websites/Campus/Python/J1/" + name + "/" + file
    shutil.copy(src_path, dst_path)
    os.remove("/Volumes/DATA/websites/Campus/Python/J1/" + file)

    return file in "/Volumes/DATA/websites/Campus/Python/J1/" + name + "/"


def read_file(folder, file):
    i = 1
    while True:
        with open(folder + "/" + file, 'r') as f:
            print(f.readline(i))
        choice = str(input("Next ? Type n / Previous ? Type p / Exit ? Type q : "))
        if choice == "n":
            i = i + 1
            with open(folder + "/" + file, 'r') as f:
                print(f.readline(i))
        if choice == "p":
            i = i - 1
            with open(folder + "/" + file, 'r') as f:
                print(f.readline(i))
        if choice == "q":
            return False


def manage_file():
    usr_choice = int(input("1) Create folder & copy / 2) Read file / 3) Rename file / 4) exit : "))
    if usr_choice == 1:
        folder_name = str(input("Folder name : "))
        file_name = str(input("File name & type : "))
        create_folder(folder_name, file_name)
    if usr_choice == 2:
        folder_name = str(input("Folder name : "))
        file_name = str(input("File name & type : "))
        read_file(folder_name, file_name)
    if usr_choice == 3:
        folder_name = str(input("Path : "))
        new_name = str(input("New name : "))
        edit_file(folder_name, new_name)
    if usr_choice == 4:
        exit()
    else:
        manage_file()




