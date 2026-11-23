import QtQuick 

Rectangle { 
    id: page 
    width: 320; height: 480 
    color: "lightgray" 

    // Create a property to hold the user's chosen text color safely
    property color chosenColor: "black"

    Text { 
        id: helloText 
        text: "Hello world!" 
        x: 150 
        y: 50 
        font.pointSize: 24; font.bold: true 
        
        // Bind the default color to our custom property
        color: page.chosenColor

        // MOVED HERE: States must live inside the component changing properties
        states: [
            State { 
                name: "down" 
                when: mouseArea.pressed == true 
                PropertyChanges { 
                    target: helloText 
                    y: 160 
                    rotation: 180 
                    color: "red" 
                } 
            }
        ] 

        // MOVED HERE: Transitions must live next to the states
        transitions: [
            Transition { 
                from: "" 
                to: "down" 
                reversible: true
                
                NumberAnimation { 
                    properties: "y,rotation" 
                    duration: 500 
                    easing.type: Easing.InOutQuad 
                } 
                ColorAnimation { 
                    properties: "color" 
                    duration: 500 
                } 
            }
        ]
    } 

    MouseArea { 
        id: mouseArea
        anchors.fill: parent 
    } 

    Grid { 
        id: colorPicker 
        x: 4; anchors.bottom: page.bottom; anchors.bottomMargin: 4 
        rows: 2; columns: 3; spacing: 3 

        // Changed from helloText.color to page.chosenColor to keep bindings safe
        Cell { cellColor: "red"; onClicked: (cellColor) => { page.chosenColor = cellColor } } 
        Cell { cellColor: "green"; onClicked: (cellColor) => { page.chosenColor = cellColor } } 
        Cell { cellColor: "blue"; onClicked: (cellColor) => { page.chosenColor = cellColor } } 
        Cell { cellColor: "yellow"; onClicked: (cellColor) => { page.chosenColor = cellColor } } 
        Cell { cellColor: "steelblue"; onClicked: (cellColor) => { page.chosenColor = cellColor } } 
        Cell { cellColor: "black"; onClicked: (cellColor) => { page.chosenColor = cellColor } } 
    } 
}
