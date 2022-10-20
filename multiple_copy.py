import os

os.chdir('c://2022-07-10 NRing')
print(os.getcwd())
print(os.listdir())
print('\n')


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

os.mkdir('c://destination_path')
