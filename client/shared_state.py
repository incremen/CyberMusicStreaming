from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.client_socket import ClientSocketHandler
    from music_playing.audio_handler import AudioHandler
from client.music_playing_emitter import MusicPlayingEmitter
from database.login_manager import LoginManager

@dataclass
class SharedState:
  socket_handler: 'ClientSocketHandler'
  audio_handler: 'AudioHandler'
  login_manager: LoginManager
