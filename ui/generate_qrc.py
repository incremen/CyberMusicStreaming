import os

def generate_qrc(directory, qrc_file):
  with open(qrc_file, 'w') as f:
      f.write('<RCC>\n')
      f.write(' <qresource prefix="/">\n')
      for filename in os.listdir(directory):
          f.write(f' <file>images\{filename}</file>\n')
      f.write(' </qresource>\n')
      f.write('</RCC>\n')

generate_qrc(
    r'D:\VS Code Projects (good place)\Cyber Music Streaming\ui\images', 
    
    r'D:\VS Code Projects (good place)\Cyber Music Streaming\ui\resource_file.qrc'
    )

"""
pyuic5 -x ui\main_page\main_page.ui -o ui\main_page\main_page_ui.py
pyrcc5 ui\resource_file.qrc -o resource_file_rc.py\
    
pyuic5 -x ui\albums_page\albums_page.ui -o ui\albums_page\albums_page_ui.py
"""