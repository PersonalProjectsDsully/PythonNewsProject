import sys
from PyQt6 import *
from PyQt6.QtSql import QSqlDatabase, QSqlQuery
from PyQt6.QtWidgets import (

    QApplication,

    QMainWindow,

    QMessageBox,

    QTableWidget,

    QTableWidgetItem,

)


def createConnection():
    con = QSqlDatabase.addDatabase("QSQLITE")
    con.setDatabaseName("news.db")
    con.open()


class Contacts(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("QTableView Example")
        self.resize(450, 250)
        # Set up the view and load the data
        self.view = QTableWidget()
        self.view.setColumnCount(4)
        self.view.setHorizontalHeaderLabels(["title", "description", "link", "date"])
        query = QSqlQuery("SELECT title, description, link, date FROM news")
        while query.next():
            rows = self.view.rowCount()
            self.view.setRowCount(rows + 1)
            self.view.setItem(rows, 0, QTableWidgetItem(str(query.value(0))))
            self.view.setItem(rows, 1, QTableWidgetItem(query.value(1)))
            self.view.setItem(rows, 2, QTableWidgetItem(query.value(2)))
            self.view.setItem(rows, 3, QTableWidgetItem(query.value(3)))
        self.view.resizeColumnsToContents()
        self.setCentralWidget(self.view)


createConnection()
app = QApplication(sys.argv)
win = Contacts()
win.show()
sys.exit(app.exec())
