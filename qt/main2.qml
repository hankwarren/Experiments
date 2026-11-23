import QtQuick

Rectangle {
    id: page
    width: 320; height: 480
    color: "lightgray"

    Text {
        id: helloText
        text: "Hello world!"
        x: 150
        y: 50
        //anchors.horizontalCenter: page.horizontalCenter
        font.pointSize: 24; font.bold: true
    states: [State {
        name: "down"
        when: mouseArea.pressed == true
        PropertyChanges {
            target: helloText
                y: 160
                rotation: 180
                color: "red"
        }
    }]
    
    transitions: [Transition {
        from: ""
        to: "down"
        reversible: true;

        NumberAnimation { properties: "y,rotation"; duration: 500; easing.type: Easing.InOutQuad }
        ColorAnimation { properties: "color"; duration: 500 }
    }]
    }

    MouseArea { id: mouseArea; anchors.fill: parent }
    

    Grid {
        id: colorPicker
        x: 4; anchors.bottom: page.bottom; anchors.bottomMargin: 4
        rows: 2; columns: 3; spacing: 3

        Cell { cellColor: "red"; onClicked: (cellColor) => { helloText.color = cellColor} }
        Cell { cellColor: "green"; onClicked: (cellColor) => { helloText.color = cellColor } }
        Cell { cellColor: "blue"; onClicked: (cellColor) => { helloText.color = cellColor } }
        Cell { cellColor: "yellow"; onClicked: (cellColor) => { helloText.color = cellColor } }
        Cell { cellColor: "steelblue"; onClicked: (cellColor) => { helloText.color = cellColor } }
        Cell { cellColor: "black"; onClicked: (cellColor) => { helloText.color = cellColor } }
    }
}