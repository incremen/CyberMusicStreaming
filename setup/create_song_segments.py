import os
import subprocess
from pathlib import Path
def create_song_segment(audio_file : Path, output_dir : Path):
   if output_dir.exists():
       return
   output_dir.mkdir()

   ffmpeg_cmd = [
       r'd:\Downloads2\ffmpeg-6.1-essentials_build\ffmpeg-6.1-essentials_build\bin\ffmpeg.exe', '-i', audio_file.absolute(), '-c:a', 'aac',
       '-hls_time', '10', '-hls_list_size', '0',
       '-hls_segment_filename', f'{str(output_dir)}/segment%03d.ts', f'{str(output_dir)}/index.m3u8'
   ]

   subprocess.Popen(ffmpeg_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def process_all_songs(directory: Path, output_dir: Path):
  if not output_dir.exists():
      output_dir.mkdir()
  for file in directory.iterdir():
        create_song_segment(file, output_dir / file.stem)
              
              

directory = Path("songs")
output_dir = Path("song_segments")
process_all_songs(directory, output_dir)    