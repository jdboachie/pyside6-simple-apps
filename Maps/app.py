import os
import sys
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication, QIcon
from PySide6.QtQuick import QQuickView


class View(QQuickView):

    def __init__(self, ):
        super().__init__()

        self.setTitle("Map Viewer")
        self.setIcon(QIcon(os.path.join("Maps", "img", "location.png")))
        self.setResizeMode(QQuickView.SizeRootObjectToView)

        # Load the QML file with the map component
        self.setSource(QUrl.fromLocalFile(os.path.join("Maps", "map.qml")))


if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    view = View()
    view.show()
    app.exec()
