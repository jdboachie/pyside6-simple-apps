#!/usr/bin/python3
"""
A Simple Notepad clone

"""
import os
import sys


from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QPlainTextEdit,
    QStatusBar,
)

from PySide6.QtGui import (
    QAction,
    QFontDatabase,
    QIcon,
)

from PySide6.QtPrintSupport import QPrintDialog


class MainWindow(QMainWindow):
    """
    Subclasses QMainWindow to create the Notepad window

    Args:
        QMainWindow
    """
    
    def __init__(self, ):
        """
        Defines the Window Initialization
        """
        super(MainWindow, self).__init__()
        
        # Window Setup
        self.setWindowTitle("Notepad")
        self.setMinimumSize(700, 500)
        
        layout = QVBoxLayout()
        
        self.editor = QPlainTextEdit()
        layout.addWidget(self.editor)
        self.setCentralWidget(self.editor)
        
        # QTextEdit editor configuration
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(11)
        self.editor.setFont(fixedfont)
        
        # path of the currently opened file
        self.path = ""
        
        self.status = QStatusBar()
        self.setStatusBar(self.status)
        
        file_menu = self.menuBar().addMenu("File")
        
        open_file_action = QAction(QIcon(os.path.join("Notepad/images", "open.png")), "Open", self)
        open_file_action.setStatusTip("Open")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)

        save_file_action = QAction(QIcon(os.path.join("Notepad/images", "disk.png")), "Save", self)
        save_file_action.setStatusTip("Save")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)

        saveas_file_action = QAction(QIcon(os.path.join("Notepad/images", "disk--pencil.png")), "Save As", self)
        saveas_file_action.setStatusTip("Save As")
        saveas_file_action.triggered.connect(self.file_save_as)
        file_menu.addAction(saveas_file_action)

        print_action = QAction(QIcon(os.path.join('Notepad/images', 'printer.png')), "Print", self)
        print_action.setStatusTip("Print current page")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)

        edit_menu = self.menuBar().addMenu("Edit")

        undo_action = QAction(QIcon(os.path.join('Notepad/images', 'arrow-curve-180-left.png')), "Undo", self)
        undo_action.setStatusTip("Undo last change")
        undo_action.triggered.connect(self.editor.undo)
        edit_menu.addAction(undo_action)

        redo_action = QAction(QIcon(os.path.join('Notepad/images', 'arrow-curve.png')), "Redo", self)
        redo_action.setStatusTip("Redo last change")
        redo_action.triggered.connect(self.editor.redo)
        edit_menu.addAction(redo_action)

        edit_menu.addSeparator()

        cut_action = QAction(QIcon(os.path.join('Notepad/images', 'scissors.png')), "Cut", self)
        cut_action.setStatusTip("Cut selected text")
        cut_action.triggered.connect(self.editor.cut)
        edit_menu.addAction(cut_action)

        copy_action = QAction(QIcon(os.path.join('Notepad/images', 'document-copy.png')), "Copy", self)
        copy_action.setStatusTip("Copy selected text")
        copy_action.triggered.connect(self.editor.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction(QIcon(os.path.join('Notepad/images', 'clipboard-paste-document-text.png')), "Paste", self)
        paste_action.setStatusTip("Paste from clipboard")
        paste_action.triggered.connect(self.editor.paste)
        edit_menu.addAction(paste_action)

        select_action = QAction(QIcon(os.path.join('Notepad/images', 'selection-input.png')), "Select all", self)
        select_action.setStatusTip("Select all text")
        select_action.triggered.connect(self.editor.selectAll)
        edit_menu.addAction(select_action)

        edit_menu.addSeparator()

        wrap_action = QAction(QIcon(os.path.join('Notepad/images', 'arrow-continue.png')), "Wrap text to window", self)
        wrap_action.setStatusTip("Toggle wrap text to window")
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)

        self.update_title()
        self.show()
    
    def dialog_critical(self, msg):
        """Generates a Critical Dialog Box

        Args:
            msg (string): Message to be displayed
        """
        dialog = QMessageBox(self)
        dialog.setText(msg)
        dialog.setIcon(QMessageBox.Critical)
        dialog.show()
    
    def edit_toggle_wrap(self, ):
        """Toggles the Wrap Text to Window Option"""
        self.editor.setLineWrapMode(QPlainTextEdit.WidgetWidth if self.editor.lineWrapMode() == QPlainTextEdit.NoWrap else QPlainTextEdit.NoWrap)
    
    def file_open(self, ):
        """Opens a File Dialog Box to Open a File"""
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Open",
            "*.txt"
        )
        
        if path:
            
            try:
                with open(path, 'r') as f:
                    text = f.read()
            
            except Exception as e:
                self.dialog_critical(str(e))
            
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()
    
    def file_print(self, ):
        """Opens a Print Dialog Box to Print the Current Document"""
        dialog = QPrintDialog()
        
        if dialog.exec_():
            self.editor.print_(dialog.printer())
    
    def file_save(self, ):
        """Saves the Current Document"""
        if self.path == "" or None:
            self.file_save_as()
        
        self.save_to_path(self.path)
    
    def file_save_as(self, ):
        """Opens a File Dialog Box to Save the Current Document"""
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save As",
            "*.txt"
        )
        
        if path:
            self.save_to_path(path)
    
    def save_to_path(self, path):
        """Saves the Current Document to the Specified Path

        Args:
            path (string): Path to Save the Document
        """
        text = self.editor.toPlainText()
        
        try:
            with open(path, 'w') as f:
                f.write(text)
        
        except Exception as e:
            self.dialog_critical(str(e))
        
        else:
            self.path = path
            self.update_title()
    
    def update_title(self):
        """Updates the Title of the Window"""
        self.setWindowTitle("{} - Notepad".format(os.path.basename(self.path) if self.path else "Untitled"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
