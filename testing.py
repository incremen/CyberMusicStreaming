from PyQt5.QtWidgets import QApplication
from ui.playlist_page.playlist_window import PlaylistWindow
import sys

def main():
    app = QApplication(sys.argv)
    test_window = PlaylistWindow()
    test_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()