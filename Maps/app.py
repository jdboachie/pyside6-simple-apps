import sys

import folium
from folium.plugins import MiniMap

from geocoder import ip

from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QApplication, QMainWindow


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map Viewer")
        self.setWindowIcon(QIcon("Maps/images/location.png"))
        self.setMinimumSize(900, 700)

        file_menu = self.menuBar().addMenu("File")
        edit_menu = self.menuBar().addMenu("Edit")
        view_menu = self.menuBar().addMenu("View")

        location = ip("me")
        if location:
            m = folium.Map(location=(location.lat, location.lng), zoom_start=50)
            folium.CircleMarker(
                location=(location.lat, location.lng),
                radius=20,
                popup=m.location,
                color="blue",
                fill=True,
                fill_color="blue",
            ).add_to(m)
            
            folium.CircleMarker(
                location=(location.lat, location.lng),
                radius=1,
                popup=m.location,
                color="blue",
                fill=True,
                fill_color="blue",
            ).add_to(m)
        else:
            m = folium.Map(location=(0, 0), zoom_start=50)

        minimap = MiniMap()
        m.add_child(minimap)

        self.map_view = QWebEngineView(self)
        map_html = m._repr_html_()
        
        self.map_view.setHtml(map_html, QUrl("about:blank"))
        self.setCentralWidget(self.map_view)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())
