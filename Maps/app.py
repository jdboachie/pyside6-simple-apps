import sys

import folium
from folium.plugins import MiniMap

from geocoder import ip

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QLabel,
    QWidget,
)


class MapWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Map Viewer")
        self.setWindowIcon(QIcon("Maps/img/location.png"))
        self.setMinimumSize(900, 700)

        file_menu = self.menuBar().addMenu("File")
        edit_menu = self.menuBar().addMenu("Edit")
        view_menu = self.menuBar().addMenu("View")
        
        self.statusBar().showMessage("Loading...")
        
        layout = QHBoxLayout()

        self.map_view = QWebEngineView(self)
        
        location = ip("me")
        if location:
            m = folium.Map(location=(location.lat, location.lng), zoom_start=30)
            folium.CircleMarker(
                location=(location.lat, location.lng),
                radius=10,
                popup=m.location,
                color="red",
                fill=True,
                fill_color="red",
            ).add_to(m)
            
            folium.ClickForMarker(
                "<b>Lat:</b> ${lat}<br /><b>Lon:</b> ${lng}",
            ).add_to(m)
        else:
            m = folium.Map(location=(0, 0), zoom_start=50)

        minimap = MiniMap()
        m.add_child(minimap)
        map_html = m._repr_html_()
        self.map_view.setHtml(map_html, QUrl("about:blank"))

        self.label = QLabel()
        self.label.setPixmap(QPixmap("Maps/img/location.png"))
        
        # Mouse click events
        self.map_view.mousePressEvent = lambda event: print(f"[Map] Mouse click event at {event.localPos()}")
        self.label.mousePressEvent = lambda event: print(f"[Label] Mouse click event at {event.localPos()}")

        layout.addWidget(self.map_view)
        # layout.addWidget(self.label)

        self.container = QWidget()
        self.container.setLayout(layout)
        self.container.setCursor(Qt.PointingHandCursor)
        self.setCentralWidget(self.container)
        self.statusBar().showMessage("Ready")
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapWindow()
    window.show()
    sys.exit(app.exec())


# from PySide6.QtCore import Qt, QUrl
# from PySide6.QtGui import QGuiApplication
# from PySide6.QtQuick import QQuickView

# # Create the PySide6 application
# app = QGuiApplication([])

# # Create a QQuickView for displaying the map
# view = QQuickView()

# # Set the window properties
# view.setTitle("Map Application")
# view.setResizeMode(QQuickView.SizeRootObjectToView)

# # Load the QML file with the map component
# view.setSource(QUrl.fromLocalFile("Maps/map.qml"))

# # Show the window
# view.show()

# # Run the application event loop
# app.exec()