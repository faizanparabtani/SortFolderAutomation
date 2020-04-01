import os
import shutil
from os import path

# Put the path of the folder to be sorted below between ""
# Example C:/Users/Faizan/Downloads will sort the Downloads Folder
folder_to_sort = ""
os.chdir(folder_to_sort)

Images = 'Images'
PDF = "PDF's"
Audio = 'Audio'
Video = 'Video'
Text = 'Text'
Executables = 'Executables'
Docs = 'Docs'
Zip = 'Zipped'



def check_and_create():
    if path.isdir(Images) == False:
        Img = os.path.join(folder_to_sort, Images)
        os.mkdir(Img)
    if path.isdir(Audio) == False:
        Aud = os.path.join(folder_to_sort, Audio)
        os.mkdir(Aud)
    if path.isdir(Video) == False:
        Vid = os.path.join(folder_to_sort, Video)
        os.mkdir(Vid)
    if path.isdir(PDF) == False:
        PD = os.path.join(folder_to_sort, PDF)
        os.mkdir(PD)
    if path.isdir(Text) == False:
        Tex = os.path.join(folder_to_sort, Text)
        os.mkdir(Tex)
    if path.isdir(Executables) == False:
        Exe = os.path.join(folder_to_sort, Executables)
        os.mkdir(Exe)
    if path.isdir(Docs) == False:
        Doc = os.path.join(folder_to_sort, Docs)
        os.mkdir(Doc)
    if path.isdir(Zip) == False:
        zip = os.path.join(folder_to_sort, Zip)
        os.mkdir(zip)



def sort_files():
    for filename in os.listdir(folder_to_sort):
        try:
            if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg") or filename.endswith(".gif") or filename.endswith(".tiff"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Images + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".wav") or filename.endswith(".mp3"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Audio + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".mp4") or filename.endswith(".avi") or filename.endswith(".mov") or filename.endswith(".flv") or filename.endswith(".wmv"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Video + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".pdf"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + PDF + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".txt"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Text + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".exe"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Executables + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".xlsx") or filename.endswith(".docx") or filename.endswith(".csv"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Docs + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            elif filename.endswith(".zip"):
                move_from = folder_to_sort + "/" + filename
                move_to = folder_to_sort + "/" + Zip + "/" + filename
                os.rename(move_from, move_to)
                shutil.move(move_from, move_to)
                os.replace(move_from, move_to)
            else:
                continue
        except FileNotFoundError:
            continue


if __name__ == "__main__":
    check_and_create()
    sort_files()
