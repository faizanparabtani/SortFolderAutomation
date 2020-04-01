# Sort any folder by running this simple Python script
This is a quick and simple to use tool to clear up cluttered folders.  
It is very common to have a cluttered Desktop or Downloads Folder.  
By running this script the files are arranged according to their File Types hence giving you a cleaner working environment.  

## How Does it Work?
The script first checks if the File Type Folders exist or not.  
If not they are created.  
Then an iteration passes over every file in that folder and moves them accordingly to
their File Type Folder.  
Once all the files are iterated over you are left with a sorted and clean folder.  

## Dependencies
Python (Libraries os, pycopy-shutil)

## Setup
In sort_files.py make the following change:  
```
# Put the path of the folder to be sorted below between ""
# Example C:/Users/Faizan/Downloads will sort the Downloads Folder
folder_to_sort = ""
```
That is it.  
Once done run the script.  

### Note
Common File Type Extensions are included.  
Feel free to add any extensions if needed.  
Happy Coding!
