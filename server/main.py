import glob
from subprocess import call
from zipfile import ZipFile
import shutil
import os
while True:
    directory = '../source/*'
    all_source_path = glob.glob(directory)
    if len(all_source_path) > 0:
        item = all_source_path[0]
        obj = item.split('\\')
        main_obj = obj[-1].split('.')
        first_name = main_obj[0]
        last_name = main_obj[1]
        if last_name == 'py':
            call (['python' , item])
            os.remove(item)
        else :
            with open (item , 'r') as file:
                all_data = file.readlines()
            data1=''
            data2=''
            data3=''
            if all_data != []:
                for i in range (10):
                    data1+=all_data[i]
                for i in range (20):
                    data2+=all_data[i]
                for i in range (30):
                    data3+=all_data[i]
            all_file = []
            for i in range (3):
                file_name = first_name+'_'+str(i+1)+'.'+last_name
                all_file.append(file_name)
                with open (file_name , 'w') as file:
                    if i == 0:
                        file.write(data1)
                    elif i ==1:
                        file.write(data2)
                    else:
                        file.write(data3) 
            zip_name = 'my_python_files.zip'
            with ZipFile (zip_name , 'w') as zip:
                for file in all_file:
                    zip.write(file)
                all_file.append(zip_name)
                zip.close()
            destination_path = '../destination/'
            shutil.copy(zip_name , destination_path)
            with ZipFile (zip_name , 'r') as zip:
                zip.extractall(destination_path)
                zip.close()
            for file in all_file:
                os.remove(file)
            dest_directory = '../destination/*'
            all_dest_file = glob.glob(dest_directory)
            os.remove(all_dest_file[0])
            os.remove(item)
