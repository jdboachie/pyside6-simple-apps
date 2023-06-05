import os
import sys
import time

from custom_logger import CustomLogger

from PySide6.QtCore import (
    QDate,
    QDir,
    QStandardPaths,
    Qt,
    QUrl,
    Slot,
)
from PySide6.QtGui import (
    QDesktopServices,
    QGuiApplication,
    QIcon,
    QImage,
    QPixmap,
)
from PySide6.QtMultimedia import (
    QCamera,
    QImageCapture,
    QMediaCaptureSession,
    QMediaDevices,
)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


logger = CustomLogger()


class ImageView(QWidget):
    
    def __init__(self, preview_image, file_name):
        super().__init__()
        
        self.file_name = file_name
        
        main_layout = QVBoxLayout(self)
        self.image_label = QLabel()
        self.image_label.setPixmap(QPixmap.fromImage(preview_image))
        main_layout.addWidget(self.image_label)
        
        top_layout = QHBoxLayout()
        
        self.file_name_label = QLabel(QDir.toNativeSeparators(file_name))
        self.file_name_label.setTextInteractionFlags(Qt.TextInteractionFlag)
        top_layout.addWidget(self.file_name_label)
        
        top_layout.addStretch()
        copy_button = QPushButton("Copy")
        copy_button.setToolTip("Copy file name to clipboard")
        top_layout.addWidget(copy_button)
        copy_button.clicked.connect(self.copy)
        launch_button = QPushButton("Launch")
        launch_button.setToolTip("Launch image viewer")
        top_layout.addWidget(launch_button)
        launch_button.clicked.connect(self.launch)
        main_layout.addLayout(top_layout)
    
    @Slot()
    def copy(self):
        QGuiApplication.clipboard().setText(self._file_name_label.text())

    @Slot()
    def launch(self):
        QDesktopServices.openUrl(QUrl.fromLocalFile(self._file_name))


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Camera")
        self.setWindowIcon(QIcon(os.path.join("Camera", "img", "camera-black.png")))
        self.setMinimumSize(900, 700)
        
        self.layout = QGridLayout()
        
        self.camera_picker = QComboBox()
        
        available_cameras = QMediaDevices.videoInputs()
        if available_cameras:
            for cam in available_cameras:
                self.camera_picker.addItems([cam.description()])
                logger.log_info(f"Found {cam.description()}")
            else:
                self.camera_viewfinder = QVideoWidget()
                self.layout.addWidget(self.camera_viewfinder)
                self.layout.addWidget(self.camera_picker)
            
            self.camera_info = available_cameras[0]
            self.camera = QCamera(self.camera_info)
            # self.camera.errorOccurred.connect(self._camera_error)
            self.image_capture = QImageCapture(self.camera)
            # self.image_capture.imageCaptured.connect(self.image_captured)
            # self.image_capture.imageSaved.connect(self.image_saved)
            # self.image_capture.errorOccurred.connect(self._capture_error)
            self.capture_session = QMediaCaptureSession()
            self.capture_session.setCamera(self.camera)
            self.capture_session.setImageCapture(self.image_capture)
        else:
            logger.log_error("No cameras found")

        if self.camera:
            self.setWindowTitle(f"Camera - {self.camera_info.description()}")
            self.capture_session.setVideoOutput(self.camera_viewfinder)
            self.camera.start()
        
        self.container = QWidget()
        self.container.setLayout(self.layout)
        self.setCentralWidget(self.container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
