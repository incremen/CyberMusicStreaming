import testing.drag_test_window 
from PyQt5.QtWidgets import QApplication
import sys


def main():
    app = QApplication(sys.argv)
    test_window = testing.drag_test_window.TestWindow()
    test_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()