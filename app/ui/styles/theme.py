from app.ui.styles.colors import Colors


APP_STYLE = f"""

QMainWindow {{
    background:{Colors.BACKGROUND};
}}

QWidget {{
    background:{Colors.BACKGROUND};
    color:{Colors.TEXT};
    font-family:'Segoe UI';
    font-size:14px;
}}

QPushButton {{

    border:none;

    border-radius:10px;

    padding:10px;

}}

QPushButton:hover {{

    background:{Colors.HOVER};

    color:white;

}}

QStatusBar {{

    background:white;

}}

"""