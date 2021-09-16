import os

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

i = 1

while True:
    new_folder = 'Virus'+str(i)
    folder_path = os.path.join(desktop, new_folder)
    os.mkdir(folder_path)
    i += 1