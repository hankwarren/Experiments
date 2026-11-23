
import QtQuick

// qml ai2main.qml

Rectangle {
    id: page
    width: 320; height: 480
    color: "lightgray"

    Text {
        id: helloText
        text: "Hello world!"
        y: 30
        x: 100
        font.pointSize: 24; font.bold: true
    }

    MouseArea {
        id: mouseArea
        anchors.fill: parent
    }

    states: [
        State {
            name: "down"
            when: mouseArea.pressed == true
            
            // Fixed: The official Qt 6 syntax uses a target name wrapper inside PropertyChanges
            PropertyChanges {
                helloText {
                    y: 160
                    rotation: 180
                    color: "red"
                }
            }
        }
    ]

    transitions: [
        Transition {
            from: ""
            to: "down"
            reversible: true
            
            ParallelAnimation {
                NumberAnimation {
                    properties: "y,rotation"
                    duration: 500
                    easing.type: Easing.InOutQuad
                }
                ColorAnimation {
                    duration: 500
                }
            }
        }
    ]

    // Custom Cell component implementation from the tutorial is required for the bottom grid
    Grid {
        id: colorPicker
        x: 4; anchors.bottom: page.bottom; anchors.bottomMargin: 4
        rows: 2; columns: 3; spacing: 3

        Rectangle { width: 50; height: 50; color: "red"; MouseArea { anchors.fill: parent; onClicked: helloText.color = "red" } }
        Rectangle { width: 50; height: 50; color: "green"; MouseArea { anchors.fill: parent; onClicked: helloText.color = "green" } }
        Rectangle { width: 50; height: 50; color: "blue"; MouseArea { anchors.fill: parent; onClicked: helloText.color = "blue" } }
        Rectangle { width: 50; height: 50; color: "yellow"; MouseArea { anchors.fill: parent; onClicked: helloText.color = "yellow" } }
        Rectangle { width: 50; height: 50; color: "steelblue"; MouseArea { anchors.fill: parent; onClicked: helloText.color = "steelblue" } }
        Rectangle { width: 50; height: 50; color: "black"; MouseArea { anchors.fill: parent; onClicked: helloText.color = "black" } }
    }
}
