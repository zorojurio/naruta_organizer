import os
import logging
from constants import *

logging.info(f'Naruta Started to organize files')
path = os.getcwd()
logging.debug(f'Naruta Organizing in Path {path}')

path = '/home/luffy/Downloads'
os.chdir(path)
file_types = [
    AUDIO,
    IMAGE,
    VIDEO,
    DOC,
    ZIP,
    DATA,
    OTHER,
]

for file_type in file_types:
    try:
        os.mkdir(os.path.join(path, file_type))
        logging.debug(f'Folder {file_type} created')
    except FileExistsError:
        logging.error('Folder already Exists')
extension_mapper = {
    '.aif': AUDIO,
    '.cda': AUDIO,
    '.mid': AUDIO,
    '.mp3': AUDIO,
    '.mpa': AUDIO,
    '.ogg': AUDIO,
    '.wav': AUDIO,
    '.wma': AUDIO,
    '.wpl': AUDIO,
    '.7z': ZIP,
    '.arj': ZIP,
    '.deb': ZIP,
    '.pkg': ZIP,
    '.rar': ZIP,
    '.rpm': ZIP,
    '.tar.gz': ZIP,
    '.z': ZIP,
    '.zip': ZIP,
    '.bin': ZIP,
    '.dmg': ZIP,
    '.iso': ZIP,
    '.toast': ZIP,
    '.vcd': ZIP,
    '.csv': DOC,
    '.dat': DATA,
    '.db': DATA,
    '.dbf': DATA,
    '.log': DATA,
    '.mdb': DATA,
    '.sav': DATA,
    '.sql': DATA,
    '.tar': DATA,
    '.xml': DATA,
    '.ai': IMAGE,
    '.bmp': IMAGE,
    '.gif': IMAGE,
    '.ico': IMAGE,
    '.jpeg': IMAGE,
    '.jpg': IMAGE,
    '.png': IMAGE,
    '.ps': IMAGE,
    '.psd': IMAGE,
    '.svg': IMAGE,
    '.tif': IMAGE,
    '.tiff': IMAGE,
    '.webp': IMAGE,
    '.key': DOC,
    '.odp': DOC,
    '.pps': DOC,
    '.ppt': DOC,
    '.pptx': DOC,
    '.ods': DOC,
    '.xls': DOC,
    '.xlsm': DOC,
    '.xlsx': DOC,
    '.doc': DOC,
    '.docx': DOC,
    '.odt': DOC,
    '.pdf': DOC,
    '.rtf': DOC,
    '.tex': DOC,
    '.txt': DOC,
    '.wpd': DOC,
    '.3g2': VIDEO,
    '.3gp': VIDEO,
    '.avi': VIDEO,
    '.flv': VIDEO,
    '.h264': VIDEO,
    '.m4v': VIDEO,
    '.mkv': VIDEO,
    '.mov': VIDEO,
    '.mp4': VIDEO,
    '.mpg': VIDEO,
    '.mpeg': VIDEO,
    '.rm': VIDEO,
    '.swf': VIDEO,
    '.vob': VIDEO,
    '.webm': VIDEO,
    '.wmv': VIDEO,
}

for file in os.listdir():
    try:
        if os.path.isfile(file):
            ext = os.path.splitext(file)[1]
            if ext in extension_mapper:
                file_type = extension_mapper[ext]
                os.rename(os.path.join(path, file), os.path.join(path, file_type, file))
                print(f'File {file} is a {file_type}')
            else:
                os.rename(os.path.join(path, file), os.path.join(path, OTHER, file))
    except Exception as e:
        logging.error(f'{e}')

logging.info('Naruta Completed Organizing Files')