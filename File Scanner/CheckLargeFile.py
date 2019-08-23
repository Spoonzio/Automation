import shutil, os

# Check all folder's subfolder/ files for big files (100mb)
def checkfolder(fdirect, freport, flimit):
   
    for root, subfolders, files in os.walk(fdirect):
        if files:
             for file in files:
                currfile = os.path.getsize(os.path.join(root, file))
                if currfile > int(flimit)*(1024*1024):
                    freport[0] += currfile

                    if currfile > 1073741824:
                        currfile =str(round(currfile/1073741824 ,2)) + "Gb"
                    else:
                        currfile =str(round(currfile/1048576, 2)) + "Mb"
                        
                    temp ="# "+ str(file) + " ----------- @ " + str(root) + "------------ " + currfile
                    if temp not in freport:
                        freport.append(temp)
                        print(temp)

        if subfolders:
            for subfolder in subfolders:
                checkfolder(os.path.join(root, subfolder), freport, flimit)
            
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
        limit = str(input("What is the minimum MB size to look for?(Too low will cause in a large list of result): \n"))
        os.chdir(checkdir) # User input location here
        report = [0]
        checkfolder(checkdir, report, limit)


