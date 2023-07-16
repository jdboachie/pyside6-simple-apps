// import QtQuick 2.15
// import QtLocation 5.15

// Item {
//     width: 1100
//     height: 650

//     Plugin {
//         id: mapPlugin
//         name: "osm"
//     }

//     Map {
//         id: map
//         anchors.fill: parent
//         plugin: mapPlugin

//         center {
//             latitude: 6.67574
//             longitude: -1.55681
//         }

//         zoomLevel: 14
//     }
    
//     MouseArea {
//         anchors.fill: parent
//         onClicked: {
//             console.log("Mouse clicked at:", mouseX, mouseY)
//             // Perform actions based on the mouse click event
//         }
//     }
// }

import QtQuick 2.15
import QtQuick.Controls 2.15
import QtPositioning 5.15
import QtLocation 5.15

Rectangle {
    id: rectangle
    Plugin {
        id: osmPlugin
        name: "osm"
        // name: "esri"
        // preferred: ["esri", "osm"]
        // PluginParameter {
        //     name: "osm.mapping.providersrepository.disabled"
        //     value: "false"
        // }
        // PluginParameter {
        //     name: "osm.mapping.providersrepository.address"
        //     // value: "http://maps-redirect.qt.io/osm/5.8/"
        //     // value: "https://tile.thunderforest.com/cycle/"
        //     // value: "https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/8/136/74" 
        // }
        // PluginParameter { name: "osm.useragent"; value: "My great Qt OSM application" }
        // PluginParameter { name: "osm.mapping.host"; value: "http://osm.tile.server.address/" }
        // PluginParameter { name: "osm.mapping.copyright"; value: "Soko Aerial Robotics" }
        // PluginParameter { name: "osm.routing.host"; value: "http://osrm.server.address/viaroute" }
        // PluginParameter { name: "osm.geocoding.host"; value: "http://geocoding.server.address" }
        // PluginParameter { name: "osm.places.host"; value: "http://geocoding.server.address" }
       
        PluginParameter {
            name: "osm.mapping.providersrepository.disabled"
            value: "true"
        }
        PluginParameter {
            name: "osm.mapping.providersrepository.address"
            value: "http://maps-redirect.qt.io/osm/5.8/"
        }
    }
    property variant locationTC: QtPositioning.coordinate(7.9465, 1.0232)
    property int zoomLevel: 6
        Map {
            id: map
            anchors.fill: parent
            plugin: osmPlugin
            center: locationTC
            zoomLevel: 6
            // zoom in and out buttons
            Column {
                anchors.right: parent.right
                rightPadding: 5
                topPadding: 5
                spacing: 5
                Button {
                    contentItem: Text {
                        text: "+"
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 24
                        color: "white"
                    }
                    onClicked: {
                        map.zoomLevel += 1
                    }
                    width: 50
                    height: 30
                    background: Rectangle {
                        color: "#8572a8"
                    }
                }
                Button {
                    contentItem: Text {
                        text: "-"
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                        font.pointSize: 24
                        color: "white"
                    }
                    onClicked: {
                        map.zoomLevel -= 1
                    }
                    width: 50
                    height: 30
                    background: Rectangle {
                        color: "#8572a8"
                    }
                }
            }
            // group of items that will show on the map
            MapItemGroup {
                // marker added to the map
                MapItemView {
                    model: markermodel
                    delegate: MapQuickItem {
                        coordinate: model.position_marker
                        anchorPoint.x: image.width/2
                        anchorPoint.y: image.height
                        sourceItem: Image {
                            id: image
                            source: model.source_marker
                        }
                        MouseArea {
                            id: markerMouseArea
                            objectName: "buttonMouseArea"
                            anchors.fill: parent
                            hoverEnabled: true
                            onClicked: {
                                App.showImage(model.imgPath)
                            }
                        }

                        ToolTip {
                            parent: image
                            visible: markerMouseArea.containsMouse
                            text: qsTr(model.tooltip)
                            width: contentWidth + 16
                            height: contentHeight + 16

                        }
                    }
                }
//                 MapItemView {
//     model: markermodel
//     delegate: MapQuickItem {
//         coordinate: model.position_marker
//         anchorPoint.x: image.width/2
//         anchorPoint.y: image.height

//         sourceItem: Item {
//             id: tooltipContainer

//             // Tooltip MouseArea
//             MouseArea {
//                 id: markerMouseArea
//                 objectName: "buttonMouseArea"
//                 anchors.fill: parent
//                 hoverEnabled: true
//                 onClicked: {
//                     App.showImage(model.imgPath)
//                 }
//             }

//             // Tooltip Rectangle
//             Rectangle {
//                 id: tooltip
//                 width: Math.min(contentWidth + 16, image.width * 0.5) // Limit width to 50% of the image width
//                 height: Math.min(contentHeight + 16, image.height * 0.5) // Limit height to 50% of the image height
//                 color: "lightyellow"
//                 border.color: "black"
//                 border.width: 1
//                 radius: 4

//                 // Tooltip Text
//                 Text {
//                     anchors.centerIn: parent
//                     text: qsTr(model.tooltip)
//                     font.pixelSize: 14
//                     wrapMode: Text.Wrap
//                 }

//                 // Position the tooltip within the parent image
//                 x: markerMouseArea.containsMouse ? -width - 8 : image.width + 8
//                 y: markerMouseArea.containsMouse ? -height - 8 : image.height + 8

//                 // Hide the tooltip when not hovered
//                 visible: markerMouseArea.containsMouse
//             }
//         }
//     }
// }

                // path traversed by the drone
                MapItemView {
                    model: dronemodel
                    delegate: MapPolyline {
                        line.width: 3
                        line.color: "blue"
                        path: model.dronePath
                    }
                }

                // polygon that shows where the drone is viewing
                MapItemView {
                    model: fmvmodel
                    delegate: MapPolygon {
                        color: "#4c98e073"
                        border.color: "blue"
                        border.width: 2
                        path: model.polygonPoints
                    }
                }
                // next four lines for the drone"s view
                MapItemView {
                    model: fmvmodel
                    delegate: MapPolyline {
                        line.width: 1
                        line.color: "blue"
                        path: model.linePoints[0]
                    }
                }

                MapItemView {
                    model: fmvmodel
                    delegate: MapPolyline {
                        line.width: 2
                        line.color: "blue"
                        path: model.linePoints[1]
                    }
                }

                MapItemView {
                    model: fmvmodel
                    delegate: MapPolyline {
                        line.width: 2
                        line.color: "blue"
                        path: model.linePoints[2]
                    }
                }

                MapItemView {
                    model: fmvmodel
                    delegate: MapPolyline {
                        line.width: 2
                        line.color: "blue"
                        path: model.linePoints[3]
                    }
                }
                // frame center line
                MapItemView {
                    model: fmvmodel
                    delegate: MapPolyline {
                        id: framecenterline
                        line.width: 3
                        // line.color: "blue"
                        line.color: "red"
                        path: model.linePoints[4]
                        MouseArea {
                            id: frame_center_line_mousearea
                            objectName: "buttonMouseArea"
                            anchors.fill: parent
                            hoverEnabled: true
                        }

                        ToolTip {
                            parent: framecenterline
                            visible: frame_center_line_mousearea.containsMouse
                            text: qsTr("Frame Center")
                        }
                    }
                }

                // drone marker
                MapItemView {
                    model: dronemodel
                    anchors.fill: parent
                    delegate: MapQuickItem {
                        coordinate: model.dronePosition
                        anchorPoint.x: droneImg.width/2
                        anchorPoint.y: droneImg.height/2
                        sourceItem: Image {
                            id: droneImg
                            width: 70
                            height: 70                    
                            transform: Rotation {
                                origin.x: droneImg.width/2
                                origin.y: droneImg.height/2
                                angle: model.heading
                            }
                            source: model.droneIcon
                        }
                    }
                }
            }
        }

        ComboBox {
            id: mapTypeComboBox
            function setMapType(index)
            {
                map.activeMapType = map.supportedMapTypes[index]
                }
            model: [
                "Street Map"
                , "Cycle Map"
                , "Transit Map"
                , "Night Transit Map"
                , "Terrain Map"
                , "Hiking Map"
            ]
            currentIndex: 0
            onCurrentIndexChanged: setMapType(currentIndex)
        }
    }
