import sys
import threading
import time
import psutil
import speedtest
from PyQt5 import QtWidgets, QtGui, QtCore

class WinSpeed(QtWidgets.QSystemTrayIcon):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setIcon(QtGui.QIcon("network_icon.png"))
        self.setToolTip("WinSpeed: Internet Speed Monitor")
        
        self.menu = QtWidgets.QMenu()
        self.quit_action = QtWidgets.QAction("Quit", self)
        self.quit_action.triggered.connect(self.quit)
        self.menu.addAction(self.quit_action)
        self.setContextMenu(self.menu)
        
        self.update_speed()
        self.show()

    def update_speed(self):
        threading.Thread(target=self.test_speed).start()
        QtCore.QTimer.singleShot(60000, self.update_speed)

    def test_speed(self):
        try:
            st = speedtest.Speedtest()
            st.get_best_server()
            download_speed = st.download() / 1e6  # convert to Mbps
            upload_speed = st.upload() / 1e6  # convert to Mbps
            self.setToolTip(f"Download: {download_speed:.2f} Mbps\nUpload: {upload_speed:.2f} Mbps")
        except Exception as e:
            self.setToolTip(f"Error: {str(e)}")
    
    def quit(self):
        self.hide()
        self.app.quit()

def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    tray_icon = WinSpeed(app)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()