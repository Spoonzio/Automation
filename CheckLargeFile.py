import shutil, os

# Check all folder's subfolder/ files for big files (100mb)
def checkfolder(fdirect, freport):
   
    for root, subfolders, files in os.walk(fdirect):

        if files:
             for file in files:
                currfile = os.path.getsize(os.path.join(root, file))
                if currfile > 100000000:
                    freport[0] += currfile
                    temp = str(file) + " ----------- @ " + str(root) + "------------ " + str(currfile/1000000) +"Mb"
                    if temp not in freport:
                        freport.append(temp)
                        print(temp)

        if subfolders:
            for subfolder in subfolders:
                checkfolder(os.path.join(root, subfolder), freport)
            
        else:
            pass
        
        if not files and  not subfolders:
            pass


if __name__ == '__main__':
    checkdir = str(input("Enter full directory to check for large files:\n"))

    if os.path.exists(checkdir) != True:
        # If given invalid directory / path
        print("Directory does not exist")
        exit()

    else:
        os.chdir(checkdir) # User input location here
        report = [0]
        checkfolder(checkdir, report)


