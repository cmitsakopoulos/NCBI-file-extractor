import os
#Below one would insert the directory at which the massive folder is located.
#Keep in mind, for reasons beyond my understanding at the moment, the program renames the folders containing our FASTA files, and then moves them to the directory in which the program is stored.
#Take that into account when you insert the desired directory for the "movefiles.py" program
directory = r''
count = 0
for file in os.listdir(directory):
    count += 1
    new_name = "FOLDER%i" % count
    mouse = os.path.join(directory, file)
    os.rename(mouse, new_name)
