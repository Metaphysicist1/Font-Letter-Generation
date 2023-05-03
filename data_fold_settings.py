import sys
import os
import shutil

# print(chr(67))
# for Big,Small in :
#     string = f'mv /home/metaphysicist/Coding/Research/Font_Generation/data/Images/Images_dir/{Big} /home/metaphysicist/Coding/Research/Font_Generation/data/Images/Images_dir/{Small}'
#     print(string)

# os.system('sudo bash')

images_dir = '/home/metaphysicist/Coding/Research/Font_Generation/data/Images/Images_dir'

# for i in range(69, 70):
#     Big = chr(i)
#     Small = chr(i+32)
#     # print(Big, Small)
#     src = images_dir+'/'+Small
#     dst = images_dir+'/'+Big
#     shutil.move(src, dst)
    
#     # os.chdir(
#     #     '/home/metaphysicist/Coding/Research/Font_Generation/data/Images/Images_dir')
#     # print(os.getcwd())
#     # os.system(f'mkdir -p {Small}/{Big}')


# for i in range(69,71):
#     Big = chr(i)
#     Small = chr(i+32)
#     print(Big, Small)
# os.system(f'mkdir -p p/P')


#############################################
for i in range(71, 91):
    Big = chr(i)
    Small = chr(i+32)
    # print(Big, Small)
    src = images_dir+'/'+Big
    dst = images_dir+'/'+Small+'/'+Big
    print(chr(i))
    os.system(f'mkdir -p {Small}/{Big}')
    shutil.move(src, dst)
###########################################

# os.chdir(images_dir)
# for i in range(73+10, 73+19):
    
#     letter = chr(i+32)
#     print(letter)
#     # os.system("sudo bash")
#     os.system('rm -rf {}'.format(letter))
    # print(Big, Small)
# for i in range(69, 70):
#     os.system(f'rm -rf {dst}')
#     # os.chdir(
#     #     '/home/metaphysicist/Coding/Research/Font_Generation/data/Images/Images_dir')
#     # print(os.getcwd())
#     # os.system(f'mkdir -p {Small}/{Big}')
