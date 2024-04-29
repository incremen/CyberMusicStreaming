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
 r'D:\vs_code_projects_good_place\cyber_music_streaming\ui\images', 
 r'D:\vs_code_projects_good_place\cyber_music_streaming\ui\album_pics',
]

generate_qrc(directories, r'D:\vs_code_projects_good_place\cyber_music_streaming\ui\resource_file.qrc')



"""
pyuic5 -x ui\main_page\main_page.ui -o ui\main_page\main_page_ui.py
pyuic5 -x ui\search_page\search_page.ui -o ui\search_page\search_page_ui.py
pyuic5 -x ui\login_page\login_page.ui -o ui\login_page\login_page_ui.py

pyrcc5 ui\resource_file.qrc -o ui\resource_file_rc.py\
    
"""