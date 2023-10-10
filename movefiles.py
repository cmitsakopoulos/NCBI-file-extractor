import shutil
import os

#The following is an example directory
output = r'C:\Users\x\Desktop\Python\'

for count in range(1, 149):
    #In order for the program to be able to sort through each consecutive folder, one will have to make use of the "%i" % function; 
    #Our count variable will update with each iteration, allowing the code to sort
    for filetype in os.listdir(r"C:\Users\mitsa\Desktop\Python\FOLDER%i" % count):
        if filetype.endswith(".fna") and count <= 149:
            filepath = os.path.join(r"C:\Users\mitsa\Desktop\Python\FOLDER%i" % count, filetype)
            shutil.move(filepath, output)
            print("file %i moved" % count)
            count +=1



 



