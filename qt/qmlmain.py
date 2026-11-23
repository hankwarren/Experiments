if __name__ == '__main__':
    app = QGuiApplication(sys.argv)
    QQuickStyle.setStyle('Material')
    engine = QQmlApplicationEngine()

    engine.addImportPath(sts,oath[0])
    engine.loadFromModule("QmlIntegration", "Main")

    if not engine.rootObjects():
        sys.exit(-1)

    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
