import sys

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map Viewer")
        self.setWindowIcon(QIcon("Maps/images/location.png"))
        self.setMinimumSize(900, 650)

        file_menu = self.menuBar().addMenu("File")
        edit_menu = self.menuBar().addMenu("Edit")
        view_menu = self.menuBar().addMenu("View")

        self.map_view = QWebEngineView(self)
        self.setCentralWidget(self.map_view)

        self.load_map()

    def load_map(self):
        map_url = QUrl("https://www.openstreetmap.org/#map=19/6.67626/-1.55634")
        self.map_view.load(map_url)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())
