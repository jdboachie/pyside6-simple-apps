import QtQuick 2.15
import QtLocation 5.15

Item {
    width: 800
    height: 600

    Plugin {
        id: mapPlugin
        name: "nmea"
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: mapPlugin
    }
}