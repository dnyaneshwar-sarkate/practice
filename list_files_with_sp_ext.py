## Python programme to list down the files wiyh specific extensions

import os 

root_dir = r'D:\Dnyaneshwar\data-engg\python-practice'

lst = []

for root, dirs, files in os.walk(root_dir):

    for file in files:

        if file.endswith('.py'):
            print(root)
            print(dirs)
            print(file)
            # print(os.path.join(root, file))
