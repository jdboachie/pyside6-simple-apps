import sys
from PySide6.QtCore import QSize, QUrl
from PySide6.QtGui import QIcon
from PySide6.QtQuick import QQuickView
from PySide6.QtWidgets import QApplication
from PySide6.QtLocation import QGeoServiceProvider


class QuickView(QQuickView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setResizeMode(QQuickView.SizeRootObjectToView)
        self.setSource(QUrl.fromLocalFile("Maps/map.qml"))

        print(f"Available service providers: {QGeoServiceProvider.availableServiceProviders()}")
        
        self.setTitle("Map")
        self.setMinimumSize(QSize(700, 500))
        self.setIcon(QIcon("Maps/images/location.png"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = QuickView()
    view.show()
    sys.exit(app.exec())
