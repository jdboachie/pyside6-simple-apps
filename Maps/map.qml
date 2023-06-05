import QtQuick 2.15
import QtLocation 5.15

Item {
    width: 1100
    height: 650

    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: mapPlugin

        center {
            latitude: 6.67574
            longitude: -1.55681
        }

        zoomLevel: 14
    }
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            console.log("Mouse clicked at:", mouseX, mouseY)
            // Perform actions based on the mouse click event
        }
    }
}