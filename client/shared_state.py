from dataclasses import dataclass
from client.client_socket import ClientSocketHandler
from music_playing.audio_handler import AudioHandler
from client.main_page_emitter import WindowEmitter

@dataclass
class SharedState:
  socket_handler: ClientSocketHandler
  audio_handler: AudioHandler
