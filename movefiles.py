import shutil
import os

output = r'C:\Users\mitsa\Desktop\Dissertation\T3SS sequences and database\DATABASE'

for count in range(4, 149):
    for filetype in os.listdir(r"C:\Users\mitsa\Desktop\Python\FOLDER%i" % count):
        if filetype.endswith(".fna") and count <= 149:
            filepath = os.path.join(r"C:\Users\mitsa\Desktop\Python\FOLDER%i" % count, filetype)
            shutil.move(filepath, output)
            print("file %i moved" % count)
            count +=1



 



