import os
import shutil
import unrar

os.chdir('c://2022-07-10 NRing')
print(os.getcwd())
print(os.listdir())
print('\n')

#FIXME: Think about function interface!!!
def get_tree():
    count = 0
    for dir in os.listdir():
        # Checking that directory is a folder (not a hidden file .something)
        if os.path.isdir(dir):
            print('folder ', count, ': ', dir)
            os.chdir(dir)
            print(os.listdir())
            print('\n')
            os.chdir('..')
            count = count + 1
    count = None


def copying_from_multiple_folders():
    for dir in os.listdir():
        # Checking that directory is a folder (not a hidden file .something)
        if os.path.isdir(dir):

            os.chdir(dir)
            print(os.getcwd())

            for file in os.listdir():

                if file.endswith('12.JPG'):
                    print('copying file ', file)
                    shutil.copy2(file, 'c://destination_path')



            os.chdir('..')




if not os.path.exists('c://destination_path'):
    os.mkdir('c://destination_path')

copying_from_multiple_folders()
