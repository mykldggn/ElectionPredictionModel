# main_app.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# needs relative import
from .map_visualization import MapVisualization
class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Election Prediction App'
        self.setWindowTitle(self.title)
        self.setGeometry(100, 100, 1200, 800)

        # Initialize the map visualization
        self.map_vis = MapVisualization(self)
        self.setCentralWidget(self.map_vis)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())
