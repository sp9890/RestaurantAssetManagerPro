from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QStackedWidget,
    QLabel,
    QStatusBar,
)

from app.ui.widgets.sidebar import Sidebar

from app.ui.pages.dashboard_page import DashboardPage
from app.ui.pages.projects_page import ProjectsPage
from app.ui.pages.settings_page import SettingsPage
from app.ui.pages.images_page import ImagesPage
from app.ui.pages.menu_page import MenuPage
from app.ui.pages.categories_page import CategoriesPage
from app.ui.pages.cloudinary_page import CloudinaryPage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Restaurant Asset Manager Pro")
        self.resize(1400, 850)

        self.build_ui()

    def build_ui(self):

        central = QWidget()
        self.setCentralWidget(central)

        main_layout = QHBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        self.sidebar = Sidebar()
        self.sidebar.page_changed.connect(self.change_page)

        main_layout.addWidget(self.sidebar)

        # Right Side
        right_layout = QVBoxLayout()

        toolbar = QLabel("Restaurant Asset Manager Pro")

        toolbar.setStyleSheet("""
            background:#2c3e50;
            color:white;
            font-size:20px;
            font-weight:bold;
            padding:15px;
        """)

        right_layout.addWidget(toolbar)

        self.pages = QStackedWidget()

        # ------------------------
        # Page Registry
        # ------------------------

        self.page_registry = {

            "dashboard": DashboardPage(),

            "projects": ProjectsPage(),

            "menu": MenuPage(),

            "images": ImagesPage(),

            "settings": SettingsPage(),

            "categories": CategoriesPage(),

            "cloudinary": CloudinaryPage(),

        }

        for page in self.page_registry.values():

            self.pages.addWidget(page)

        right_layout.addWidget(self.pages)

        main_layout.addLayout(right_layout)

        status = QStatusBar()

        status.showMessage("Ready")

        self.setStatusBar(status)

        self.pages.setCurrentWidget(
            self.page_registry["dashboard"]
        )

    # def change_page(self, page):

    #     if page in self.page_registry:

    #         self.pages.setCurrentWidget(
    #             self.page_registry[page]
    #         )

    #     else:

    #         print(f"{page} page not created yet.")
    def change_page(self, page):

     print("Clicked:", page)
     print("Registry:", list(self.page_registry.keys()))

     if page in self.page_registry:

        print("Opening:", page)

        self.pages.setCurrentWidget(
            self.page_registry[page]
        )

     else:

        print(f"{page} page not created yet.")