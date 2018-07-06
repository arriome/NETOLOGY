import os
import subprocess
import errno
import uuid
count = 0
source_dir = os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"\\Source")
result_dir = os.path.normpath(os.path.dirname(os.path.abspath(__file__))+"\\Result")
if not os.path.exists(result_dir):# проверяем наличие папки result
    print("Создаем отсутствующую директорию Result")
    try:
        os.makedirs(result_dir)   # и создаем, если ее нет
    except OSerr:
        pass
print("Папка исходников",source_dir)
print("Папка назначения",result_dir)
files_list = os.listdir(source_dir)
print(files_list)
def resize_jpg(files_list):
    for file in files_list:
        print("Обработка файла:",file)
        command = os.path.join(source_dir,file)
        command_out = os.path.join(result_dir,file)
        if os.path.isfile(command_out): 
            command_out =command_out+str(uuid.uuid4())+".jpg"
            print("Такой файл уже существует в папке Result. Файл переименован в ", command_out)       
        print(command)
        print(command_out)
        subprocess.call(["convert.exe",command,"-resize", "200",  command_out])
map(resize_jpg(files_list),files_list)

