from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel


class Sidebar(QWidget):
    page_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.setFixedWidth(220)
        self.build_ui()

    def build_ui(self):
        layout = QVBoxLayout(self)

        title = QLabel("🍽 Restaurant\nAsset Manager")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            QLabel{
                font-size:20px;
                font-weight:bold;
                padding:15px;
            }
        """)

        layout.addWidget(title)

        pages = [
            ("🏠 Dashboard", "dashboard"),
            ("📁 Projects", "projects"),
            ("🍽 Categories", "categories"),
            ("🍕 Menu", "menu"),
            ("🖼 Images", "images"),
            ("☁ Cloudinary", "cloudinary"),
            ("🔥 Firebase", "firebase"),
            ("⚙ Settings", "settings"),
            ("📊 Logs", "logs"),
        ]

        for text, page in pages:
            btn = QPushButton(text)
            btn.setMinimumHeight(45)
            btn.clicked.connect(
                lambda checked=False, p=page: self.page_changed.emit(p)
            )

            btn.setStyleSheet("""
                QPushButton{
                    text-align:left;
                    padding-left:15px;
                    font-size:15px;
                    border:none;
                }

                QPushButton:hover{
                    background:#E6E6E6;
                }
            """)

            layout.addWidget(btn)

        layout.addStretch()