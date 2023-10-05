import os
import random
import string


def create_dummy_files(file_types, num_files, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i in range(num_files):
        file_type = random.choice(file_types)
        file_name = ''.join(random.choices(string.ascii_letters + string.digits, k=10)) + '.' + file_type
        file_path = os.path.join(output_dir, file_name)

        with open(file_path, 'w') as f:
            f.write('This is a dummy {} file.'.format(file_type))

    print(f'{num_files} dummy files created in {output_dir}.')


file_types = [
    'txt', 'pdf', 'csv', 'jpg', 'png', 'mp3', 'mp4',
    'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx',
    'odt', 'ods', 'odp', 'rtf', 'html', 'xml',
    'json', 'yaml', 'ini', 'md', 'log', 'zip',
    'tar', 'gz', 'bz2', '7z', 'rar', 'js', 'css',
    'py', 'c', 'cpp', 'java', 'rb', 'go', 'php',
    'swift', 'sql', 'sh', 'bat', 'pl', 'ts', 'kt',
    'rs', 'lua', 'r', 'ps', 'ai', 'psd', 'eps',
    'svg', 'tif', 'tiff', 'ico', 'bmp', 'webp',
    'wav', 'ogg', 'flac', 'm4a', 'webm', 'mkv',
    'avi', 'mov', 'wmv', 'flv', 'mobi', 'epub',
    'azw', 'azw3', 'lit', 'fb2', 'djvu', 'pdb'
]
num_files = 50
output_dir = "C:\\laragon\\www\\desktop-organizer\\training-ground"

create_dummy_files(file_types, num_files, output_dir)
