import os

for root, dirs, files in os.walk('./input'):
    print(dirs, " " , files)
    # for name in files:
    #     print(os.path.join(root, name))
