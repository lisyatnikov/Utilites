import os

os.chdir('c://2022-07-10 NRing')
print(os.getcwd())
print(os.listdir())
print('\n')


count = 0
for dir in os.listdir():
    print('folder ', count, ': ', dir)
    os.chdir(dir)
    print(os.listdir())
    print('\n')
    os.chdir('..')
    count = count + 1
count = None

os.mkdir('c://destination_path')
