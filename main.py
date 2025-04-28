import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

def load_ui(path):
    loader = QUiLoader()
    ui_file = QFile(path)
    if not ui_file.open(QFile.ReadOnly):
        print(f"Cannot open {path}: {ui_file.errorString()}")
        sys.exit(-1)
    window = loader.load(ui_file)
    ui_file.close()
    return window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = load_ui("ui/MainWindow.ui")  # <- updated filename!
    window.show()
    sys.exit(app.exec())
