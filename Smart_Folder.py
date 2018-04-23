import os
import shutil

current_path = '/Users/jante/Documents/'
os.chdir(current_path)
try:
    smart_folder_path = '/Users/jante/Documents/Smart Folder/'
    os.chdir(smart_folder_path)
except FileNotFoundError:
    os.mkdir('Smart Folder')
    os.chdir(current_path + '/Smart Folder')

image_formats = ['.jpg', '.jfif', '.exif', '.png', 'tiff', '.gif', '.bmp', '.ppm', '.pgm', '.pbm', '.pnm', '.svg']
videos_formats = ['.avi', '.mp4', '.flv', '.wmv', '.mov', '.webm', '.mkv', '.f4v', '.vob', '.ogg', '.ogv', '.m4a', '.m4v',
          '.mpg', '.mp2', '.mpeg', '.mpv', '.m2v', '.3gp', '.3g2', '.mxf']
audio_formats = ['.aac', '.aax', '.act', '.aiff', '.amr', '.ape', '.au', '.awb', '.dct', '.flac',
                 '.gsm', '.mp3', '.sln', '.wav', '.wv']
document_formats = ['.txt', '.doc', '.pptx', '.ppt', '.pages', '.keynote', '.numbers', '.pdf', '.epub', '.xls']

for file in os.listdir():
    filename, ext = os.path.splitext(file)
    if os.path.isfile(file) and ext in image_formats:
        try:
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Images/'
            shutil.move(smart_src, smart_dst)
        except FileNotFoundError:
            os.mkdir('Images')
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Images/'
            shutil.move(smart_src, smart_dst)
    elif os.path.isfile(file) and ext in videos_formats:
        try:
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Videos/'
            shutil.move(smart_src, smart_dst)
        except FileNotFoundError:
            os.mkdir('Videos')
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Videos/'
            shutil.move(smart_src, smart_dst)
    elif os.path.isfile(file) and ext in audio_formats:
        try:
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Audios/'
            shutil.move(smart_src, smart_dst)
        except FileNotFoundError:
            os.mkdir('Audios')
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Audios/'
            shutil.move(smart_src, smart_dst)
    elif os.path.isfile(file) and ext in document_formats:
        try:
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Documents/'
            shutil.move(smart_src, smart_dst)
        except FileNotFoundError:
            os.mkdir('Documents')
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Documents/'
            shutil.move(smart_src, smart_dst)
    elif os.path.isfile(file) and (ext not in image_formats or ext not in videos_formats or
                                           ext not in audio_formats or ext not in document_formats):
        try:
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Other/'
            shutil.move(smart_src, smart_dst)
        except FileNotFoundError:
            os.mkdir('Other')
            smart_src = smart_folder_path + file
            smart_dst = smart_folder_path + 'Other/'
            shutil.move(smart_src, smart_dst)