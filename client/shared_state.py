from dataclasses import dataclass
from client.client_socket import ClientSocketHandler
from music_playing.audio_handler import AudioHandler
from client.window_emitter import WindowEmitter
from database.login_manager import LoginManager


@dataclass
class SharedState:
  socket_handler: ClientSocketHandler
  audio_handler: AudioHandler
  login_manager: LoginManager
