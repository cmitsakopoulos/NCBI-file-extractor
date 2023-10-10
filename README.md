# NCBI-file-extractor
A method of separating FASTA files (.fna) from their identically named subfolders, using python automation. This would be used to port all FASTA files into a specific directory(folder), in order to concatenate them for a blastn database.


As a beginner in bioinformatics, I came across the inconvinience of mass downloading hundreds of assemblies from NCBI; that is, the website will generate a large folder which for some reason contains all of your desired .fna files in identically named subfolders. This essentially means that a simple program that scans with ".endswith" will move the subfolders to your desired location and not the FASTA files which you actually need. Not to mention, whenever I tried to use the "makeblastdb" command (needed to generate a databse for blastn) it would fail to extract my FASTA files from the hundreds of uneccesary subfolders.


In order to make effective use of the programs appended to my repository, one would first have to use the Renamefiles.py(to rename the subfolders that contain our FASTA files) and then run the movefiles.py(move the .fna files from our VSCODE Python folder, into a new folder). 

Keep in mind, this is a simple and beginner's solution to my problem. I have very little experience with coding and as such, any shortcomings(it could have been made better blah blah) with my code are a result of that. 
