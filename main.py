import os
import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QListWidget,
    QPushButton,
    QListWidgetItem,
    QLabel,
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import Qt
from send2trash import send2trash
import mimetypes


class FileScanner(QWidget):
    def __init__(self):
        super().__init__()

        self.status_label = QLabel()
        self.file_list = QListWidget()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Scanner')
        self.setGeometry(100, 100, 800, 600)

        self.scan_files()

        self.delete_button = QPushButton('Delete Selected Files')
        self.delete_button.clicked.connect(self.delete_files)

        self.refresh_button = QPushButton('Refresh List')
        self.refresh_button.clicked.connect(self.scan_files)

        self.browse_button = QPushButton('Browse for Folder')
        self.browse_button.clicked.connect(self.browse_folder)

        layout = QVBoxLayout(self)
        layout.addWidget(self.file_list)
        layout.addWidget(self.delete_button)
        layout.addWidget(self.refresh_button)
        layout.addWidget(self.browse_button)
        layout.addWidget(self.status_label)

    def scan_files(self):
        desktop_path = os.path.expanduser("~/Desktop")
        try:
            files = [f for f in os.listdir(desktop_path) if os.path.isfile(
                os.path.join(desktop_path, f))]
            self.populate_file_list(files)
            self.status_label.setText("File list refreshed.")
        except Exception as e:
            self.show_error(f"Error scanning files: {e}")

    def populate_file_list(self, files):
        self.file_list.clear()
        for file_name in files:
            file_path = os.path.join(
                os.path.expanduser("~/Desktop"), file_name)
            mime_type, _ = mimetypes.guess_type(file_path)
            icon_path = os.path.join(os.path.dirname(
                __file__), "icons", f"{mime_type}.png")

            if not os.path.exists(icon_path):
                self.download_icon_async(mime_type)

            icon = QIcon(icon_path) if os.path.exists(icon_path) else QIcon()
            item = QListWidgetItem(icon, file_name)
            self.set_item_color(item, mime_type)
            self.file_list.addItem(item)

            # Display additional file information
            item.setToolTip(f"File Name: {file_name}\nMime Type: {mime_type}")

    def download_icon_async(self, mime_type):
        # Simulating icon download for demonstration
        pass

    def delete_files(self):
        selected_items = self.file_list.selectedItems()
        if not selected_items:
            self.status_label.setText("No files selected for deletion.")
            return

        desktop_path = os.path.expanduser("~/Desktop")

        try:
            for item in selected_items:
                file_name = item.text()
                file_path = os.path.join(desktop_path, file_name)
                normalized_path = os.path.normpath(file_path)
                send2trash(normalized_path)
                item.setForeground(QColor('red'))

            self.status_label.setText("Selected files deleted successfully.")

            for item in selected_items:
                self.file_list.takeItem(self.file_list.row(item))

        except Exception as e:
            self.show_error(f"Error deleting files: {e}")

    def browse_folder(self):
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.status_label.setText(f"Selected Folder: {folder}")
            self.populate_file_list(os.listdir(folder))

    def show_error(self, message):
        self.status_label.setText(f"Error: {message}")

    def set_item_color(self, item, mime_type):
        # Assign colors based on mime types (customize as needed)
        color_mapping = {
            'text/plain': 'blue',
            'application/pdf': 'green',
            'image/jpeg': 'orange',
            'image/png': 'purple',
            'application/zip': 'brown',
            # Add more mime types and colors as needed
        }
        default_color = 'black'
        color = color_mapping.get(mime_type, default_color)
        item.setForeground(QColor(color))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scanner = FileScanner()
    scanner.show()
    sys.exit(app.exec_())
