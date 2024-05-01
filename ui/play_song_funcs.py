def skip_btn_click(self):
    self.skip_btn.setEnabled(False)
    self.audio_handler.stop_playing_song() 
    self.skip_btn.setEnabled(True)
    
def back_btn_click(self):
    self.audio_handler.play_last_song()
    
def pause_btn_click(self):
    self.audio_handler.pause_or_resume_song()
    
def update_song_progress(self, progress):
    self.progress_slider.setValue(progress)