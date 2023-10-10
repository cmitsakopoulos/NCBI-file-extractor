import os

directory = r''
count = 0
for file in os.listdir(directory):
    count += 1
    new_name = "FOLDER%i" % count
    mouse = os.path.join(directory, file)
    os.rename(mouse, new_name)