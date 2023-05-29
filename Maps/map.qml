import QtQuick 2.15
import QtQuick.Controls 2.15
import QtPositioning 6.5
import QtLocation 6.5

Item {
    width: 800
    height: 600

    Plugin {
        id: osmPlugin
        name: "osm"

        PluginParameter {
            name: "osm.mapping.providersrepository.disabled"
            value: "true"
        }

        PluginParameter {
            name: "osm.mapping.providersrepository.address"
            value: "http://maps-redirect.qt.io/osm/5.8/"
        }
    }

    Map {
        id: map
        anchors.fill: parent
        plugin: osmPlugin
    }
}
