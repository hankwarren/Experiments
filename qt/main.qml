import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 400
    height: 300
    visible: true
    title: "Python + QML Integration"

    Column {
        anchors.centerIn: parent
        spacing: 0
        Text {
            id: statusText
            text: "Click the button to fetch data from Python"
            font.pointSize: 18
            anchors.horizontalCenter: parent.horizontalCenter
        }

        Button {
            text: "Trigger Backend"
            anchors.horizontalCenter: parent.horizontalCenter
            onClicked: backend.get_server_time()
        }
    }
    Connections {
        target: backend
        function onTimeUpdated(currentTime) {
            statusText.text = currentTime
        }
    }
}