import QtQuick
import QtQuick.Controls

ApplicationWindow {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World!")

    header: MenuBar {   // on MacOS the menubar is at the top of the screen
        Menu {
            title: qsTr("&File")
            Action {
                text: qsTr("&Open...")
                onTriggered: console.log("Open action triggered")
            }
            Action {
                text: qsTr("&Save As...")
                onTriggered: console.log("Save As action triggered")
            }
            Action {
                text: qsTr("&Save...")
                onTriggered: console.log("Save action triggered")
            }
            MenuSeparator { }
            Action {    // the exit option does not show up on MacOS.
                text: qsTr("&Exit")
                onTriggered: Qt.quit()
            }
        }
    }
    Button {
        text: qsTr("Hello World!")
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }
}