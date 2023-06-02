import QtQuick 2.15
import QtLocation 5.15

Item {
    width: 1000
    height: 700

    Plugin {
        id: mapPlugin
        name: "osm"
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: mapPlugin

        center {
            latitude: 7.652
            longitude: -1.419
        }
    }
    
    MouseArea {
        anchors.fill: parent
        onClicked: {
            console.log("Mouse clicked at:", mouseX, mouseY)
            // Perform actions based on the mouse click event
        }
    }
}