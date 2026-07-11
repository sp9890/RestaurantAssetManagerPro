import sys
from PySide6.QtWidgets import QApplication

from app.ui.styles.theme import APP_STYLE

from app.ui.windows.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(APP_STYLE)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()