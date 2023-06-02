import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPlainTextEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    
    def __init__(self, ):
        super().__init__()
        
        self.setWindowTitle("QSS Tester")
        
        self.editor = QPlainTextEdit()
        self.editor.textChanged.connect(self.update_styles)
        
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
        
        # Define a set of simple widgets.
        checkbox = QCheckBox("Checkbox")
        layout.addWidget(checkbox)
        
        combo = QComboBox()
        combo.setObjectName("thecombo")
        combo.addItems(["first", "second", "third", "fourth"])
        layout.addWidget(combo)
        
        sb = QSpinBox()
        sb.setRange(0, 99999)
        layout.addWidget(sb)
        
        l = QLabel("This is a label")
        l.mousePressEvent = lambda event: print(f"Label clicked at: {event.localPos()}")
        layout.addWidget(l)
        
        line_edit = QLineEdit()
        line_edit.setObjectName("mylineedit")
        layout.addWidget(line_edit)
        
        push_button = QPushButton("Don't Push It!")
        layout.addWidget(push_button)
        
        self.container = QWidget()
        self.container.setLayout(layout)
        
        self.setCentralWidget(self.container)
    
    def update_styles(self):
        qss = self.editor.toPlainText()
        self.setStyleSheet(qss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyle("Fusion")
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())