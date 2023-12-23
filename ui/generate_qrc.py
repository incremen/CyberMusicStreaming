import os

import os

import os

def generate_qrc(directories, qrc_file):
    with open(qrc_file, 'w') as f:
        f.write('<RCC>\n')
        f.write(' <qresource prefix="/">\n')
        for directory in directories:
            for filename in os.listdir(directory):
                f.write(f' <file>{os.path.basename(directory)}/{filename}</file>\n')
        f.write(' </qresource>\n')
        f.write('</RCC>\n')

directories = [
 r'D:\VS Code Projects (good place)\Cyber Music Streaming\ui\images', 
 r'D:\VS Code Projects (good place)\Cyber Music Streaming\ui\album_pics',
]

generate_qrc(directories, 'resource_file.qrc')



"""
pyuic5 -x ui\main_page\main_page.ui -o ui\main_page\main_page_ui.py
pyrcc5 ui\resource_file.qrc -o resource_file_rc.py\
    
pyuic5 -x ui\search_page\search_page.ui -o ui\search_page\search_page_ui.py
"""