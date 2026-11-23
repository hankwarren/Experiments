import QtQuick

Window {
    width: 320
    height: 240
    visible: true
    color: "salmon"

    Text {
        anchors.centerIn: parent
        text: "Hello World!"
        font.pointSize: 25
        font.bold: true
    }
}