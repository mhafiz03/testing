import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.todo_list = QListWidget()

        self.input_text = QLineEdit()

        self.tombol_tambah = QPushButton('Tambah')
        self.tombol_tambah.clicked.connect(self.tambah_list)

        self.tombol_hapus = QPushButton('Hapus')
        self.tombol_hapus.clicked.connect(self.hapus_list)

        self.label_status = QLabel()

        hbox = QHBoxLayout()
        hbox.addWidget(self.input_text)
        hbox.addWidget(self.tombol_tambah)
        hbox.addWidget(self.tombol_hapus)

        vbox = QVBoxLayout()
        vbox.addWidget(self.todo_list)
        vbox.addLayout(hbox)
        vbox.addWidget(self.label_status)

        self.setLayout(vbox)
        self.setWindowTitle('Program Python CRUD')
        self.setMinimumSize(800, 600)

    def tambah_list(self):
        todo_text = self.input_text.text().strip()
        if todo_text:
            self.todo_list.addItem(todo_text)
            self.input_text.clear()
            self.label_status.setText('Berhasil ditambah.')
        else:
            self.label_status.setText('Tolong tulis sesuatu.')

    def hapus_list(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            self.todo_list.takeItem(self.todo_list.row(selected_item))
            self.label_status.setText('Berhasil dihapus.')
        else:
            self.label_status.setText('Tolong milih yang ingin dihapus.')


app = QApplication(sys.argv)
todo_app = App()
todo_app.show()
sys.exit(app.exec_())
