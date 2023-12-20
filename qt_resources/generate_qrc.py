import os

def generate_qrc(directory, qrc_file):
  with open(qrc_file, 'w') as f:
      f.write('<RCC>\n')
      f.write(' <qresource prefix="/">\n')
      for filename in os.listdir(directory):
          f.write(f' <file>images\{filename}</file>\n')
      f.write(' </qresource>\n')
      f.write('</RCC>\n')

generate_qrc(r'D:\VS Code Projects (good place)\Cyber Music Streaming\qt_resources\images', 
             r'D:\VS Code Projects (good place)\Cyber Music Streaming\qt_resources\resource_file.qrc')
