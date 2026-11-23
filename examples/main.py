import sys
from datetime import datetime
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal

# 1. Define a backend communication class inheriting from QObject
class BackendBridge(QObject):
    # Define a custom signal to send data back to QML
    timeUpdated = Signal(str)

    def __init__(self):
        super().__init__()

    # Define a Slot to receive actions/calls from QML
    @Slot()
    def get_server_time(self):
        now = datetime.now().strftime("%H:%M:%S")
        print(f"Python received request! Sending time: {now}")
        # Emit the signal containing the string to update the UI
        self.timeUpdated.emit(f"Python Time: {now}")

if __name__ == "__main__":
    # 2. Initialize the Qt Application (use QGuiApplication for QML apps)
    app = QGuiApplication(sys.argv)

    # 3. Create the application engine and the backend instance
    engine = QQmlApplicationEngine()
    backend = BackendBridge()

    # 4. Expose the Python object to QML as a context property named 'backend'
    engine.rootContext().setContextProperty("backend", backend)

    # 5. Load the QML UI file
    engine.load("main.qml")

    # Exit cleanly if the engine fails to load the QML file
    if not engine.rootObjects():
        sys.exit(-1)

    # 6. Execute the main event loop
    sys.exit(app.exec())
