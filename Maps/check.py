from PySide6.QtPositioning import QGeoPositionInfoSource

plugins = QGeoPositionInfoSource.availableSources()
print(plugins)
