from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQuick import QQuickView

# Create the PySide6 application
app = QGuiApplication([])

# Create a QQuickView for displaying the map
view = QQuickView()

# Set the window properties
view.setTitle("Map Application")
view.setResizeMode(QQuickView.SizeRootObjectToView)

# Load the QML file with the map component
view.setSource(QUrl.fromLocalFile("Maps/map.qml"))  # Replace "map.qml" with your QML file name

# Show the window
view.show()

# Run the application event loop
app.exec()
