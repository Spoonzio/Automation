import shutil, os

# Check all folder's subfolder/ files for big files (100mb)
def checkfolder(fdirect):
    for root, subfolders, files in os.walk(fdirect):
        if files:
            for file in files:
                if os.path.getsize(os.path.join(root, file)) > 100000000:
                    temp = str(file) + " @ " + str(root)
                    print(temp)
        
        if subfolders:
            for subfolder in subfolders:
                if os.path.getsize(os.path.join(root, subfolder)) > 100000000:
                    checkfolder(os.path.join(root, subfolder))

#check sum of files size
def checktotal(start_path = '.'):
    total = 0
    for root, _, files in os.walk(start_path):
        for f in files:
            fp = os.path.join(root, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total += os.path.getsize(fp)

    return total


if __name__ == '__main__':
    checkdir = str(input("Enter full directory to check for large files:\n"))

    if os.path.exists(checkdir) != True:
        print("Directory does not exist")
        exit()

    else:
        os.chdir(checkdir) # Put location here
        dirsize =  os.path.getsize(checkdir)
        if dirsize < 100000000:
            # Check if whole directory is less than 100mb
            print("The directory is less than 100MB (%d)" % dirsize)
            exit()
        else:
            checkfolder(checkdir)
