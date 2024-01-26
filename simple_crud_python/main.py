import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QPushButton, QLineEdit, QLabel


class TodoApp(QWidget):
    def __init__(self):
        self.init_ui()

    def init_ui(self):
        self.todo_list = QListWidget()

        self.input_text = QLineEdit()
        self.add_button = QPushButton('Add')
        self.add_button.clicked.connect(self.add_todo)

        self.delete_button = QPushButton('Delete')
        self.delete_button.clicked.connect(self.delete_todo)

        self.status_label = QLabel()

        hbox = QHBoxLayout()
        hbox.addWidget(self.input_text)
        hbox.addWidget(self.add_button)
        hbox.addWidget(self.delete_button)

        vbox = QVBoxLayout()
        vbox.addWidget(self.todo_list)
        vbox.addLayout(hbox)
        vbox.addWidget(self.status_label)

        self.setLayout(vbox)

        self.setWindowTitle('To-Do List')
        self.show()

    def add_todo(self):
        todo_text = self.input_text.text().strip()
        if todo_text:
            self.todo_list.addItem(todo_text)
            self.input_text.clear()
            self.status_label.setText('Task added successfully.')
        else:
            self.status_label.setText('Please enter a task.')

    def delete_todo(self):
        selected_item = self.todo_list.currentItem()
        if selected_item:
            self.todo_list.takeItem(self.todo_list.row(selected_item))
            self.status_label.setText('Task deleted successfully.')
        else:
            self.status_label.setText('Select a task to delete.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    todo_app = TodoApp()
    sys.exit(app.exec_())
