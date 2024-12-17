from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout, QDialog, QApplication, QPushButton,\
    QMenu, QAction
from PyQt5.QtCore import Qt
import pymysql
from datetime import datetime
import sys
from functools import partial
from design_files.main_window import Ui_MainWindow
from design_files.table_info import Ui_Form
from design_files import add_order, d_first_window, admin_window, change_order, d_registration

name_database = 'bd'


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="root",
    charset="utf8mb4"
)

cursor = connection.cursor()
cursor.execute(f"USE {name_database}")
cursor.execute("SELECT * FROM orders;")
result = cursor.fetchall()


class FirstWindow(QtWidgets.QMainWindow, d_first_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.registration_window = RegistrationWindow(self)
        self.admin_window = None
        self.pushButton.clicked.connect(self.open_main_window)
        self.pushButton_2.clicked.connect(self.open_register_window)

    def open_main_window(self):
        dialog = QDialog(self)
        dialog.resize(200, 100)
        dialog.setWindowTitle("Ошибка")
        label = QLabel("", dialog)
        label.setStyleSheet("font-size: 20px;")
        label.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        dialog.setLayout(layout)

        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '':
            try:
                print(self.lineEdit.text())
                cursor.execute(f"SELECT * FROM users WHERE email = %s;", (self.lineEdit.text(),))
                user = cursor.fetchone()
                print(user)
            except:
                label.setText("Пользователь не найден")
                dialog.exec_()
                return
            if user:
                if user[2] == self.lineEdit_2.text():
                    if user[3] == 1:
                        self.admin_window = AdminWindow()
                        self.admin_window.show()
                        self.close()
                    else:
                        window = Ui()
                        self.close()
                        window.showMaximized()
                else:
                    label.setText("Неверный пароль")
                    dialog.exec_()
            else:
                label.setText("Пользователь не найден")
                dialog.exec_()
        else:
            label.setText("Вы не заполнили поля")
            dialog.exec_()

    def open_register_window(self):
        self.registration_window.show()
        self.close()


class RegistrationWindow(QtWidgets.QMainWindow, d_registration.Ui_MainWindow):
    def __init__(self, first_window):
        super().__init__()
        self.setupUi(self)
        self.firstWindow = first_window
        self.pushButton.clicked.connect(self.go_back)
        self.pushButton_2.clicked.connect(self.registration)

    def registration(self):
        dialog = QDialog(self)
        dialog.resize(200, 100)
        dialog.setWindowTitle("Ошибка")
        label = QLabel("", dialog)
        label.setStyleSheet("font-size: 20px;")
        label.setWordWrap(True)
        layout = QVBoxLayout()
        layout.addWidget(label)
        dialog.setLayout(layout)
        if self.lineEdit.text() != '' and self.lineEdit_2.text() != '' and self.lineEdit_3.text() != '':
            if self.lineEdit_2.text() == self.lineEdit_3.text():
                self.add_user(self.lineEdit.text(), self.lineEdit_2.text())
                window = Ui()
                self.close()
                window.showMaximized()
            else:
                label.setText("Пароли не совпадают")
                dialog.exec_()

        else:
            label.setText("Вы не заполнили поля")
            dialog.exec_()

    def go_back(self):
        self.firstWindow.show()
        self.close()

    def add_user(self, email, password):
        cursor.execute("""
                    INSERT INTO users (email, password, is_admin)
                    VALUES (%s, %s, %s)
                    """, (email, password, False))
        connection.commit()
        return cursor.lastrowid


class TableInfo(QDialog):
    """информация по столу"""
    def __init__(self, table_name, res):
        super(TableInfo, self).__init__()
        
        # uic.loadUi('table_info.ui', self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.resize(int(screen_width * 0.3), int(screen_height * 0.3))
        self.ui.label.resize(int(screen_width * 0.3), int(screen_height * 0.035))
        self.ui.scrollArea.resize(int(screen_width * 0.3), int(screen_height * 0.25))
        self.ui.label.setText(table_name)
        self.ui.label.setAlignment(Qt.AlignCenter)
        text = self.set_text(res)
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        label = QLabel(text)
        font = QFont("Arial", 14)
        label.setFont(font)
        label.setWordWrap(True)
        layout.addWidget(label)
        content_widget.setLayout(layout)
        self.ui.scrollArea.setWidget(content_widget)

    def set_text(self, res):
        print(res)
        data = []
        for j in res:
            cursor.execute("SELECT * FROM waiters WHERE id = %s;", (j[8],))
            waiter = cursor.fetchone()[1]
            cursor.execute("SELECT * FROM customers WHERE id = %s;", (j[3],))
            customer = cursor.fetchone()[1]
            order = []
            for e in j[4].split(';'):
                cursor.execute("SELECT * FROM menu WHERE id = %s;", (e,))
                order.append(cursor.fetchone()[1])
            text_order = ';'.join(order)
            data.append(f'{j[2]}  {customer} - {text_order}. Стол №{j[7]}. Стоимость заказа: {int(j[5])} руб. Официант - {waiter}')
        t = '\n\n'.join(data)
        return t


class AdminWindow(QtWidgets.QMainWindow, admin_window.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.change_order_window = None
        self.content_widget = QWidget()
        self.vertical_layout = QVBoxLayout(self.content_widget)
        for i in [21, 22, 23, 24, 25, 26, 27]:
            self.add_order(f"2024-11-{i}")
        self.scrollArea.setWidget(self.content_widget)
        self.resize_window()

    def add_order(self, date):
        cursor.execute("SELECT * FROM orders;")
        result = cursor.fetchall()
        data = []
        for j in result:
            if j[1].strftime("%Y-%m-%d") == date:
                cursor.execute("SELECT * FROM waiters WHERE id = %s;", (j[8],))
                waiter = cursor.fetchone()[1]
                cursor.execute("SELECT * FROM customers WHERE id = %s;", (j[3],))
                customer = cursor.fetchone()[1]
                order = []
                for e in j[4].split(';'):
                    cursor.execute("SELECT * FROM menu WHERE id = %s;", (e,))
                    order.append(cursor.fetchone()[1])
                text_order = ';'.join(order)
                data.append(
                    f'{j[0]} {j[2]}  {customer} - {text_order}. Стол №{j[7]}. Стоимость заказа: {int(j[5])} руб. Официант - {waiter}')
        data = sorted(data, key=lambda x: datetime.strptime(x.split()[1], "%H:%M:%S"))
        for i in data:
            layout = QHBoxLayout()
            label = QLabel(" ".join(i.split()[1:]))
            layout.addWidget(label)
            btn = QPushButton()
            btn.setText("Удалить")
            btn.clicked.connect(partial(self.delete_order, i.split()[0]))
            btn_2 = QPushButton()
            btn_2.setText("Изменить")
            btn_2.clicked.connect(partial(self.change_order, i.split()[0]))
            layout.addWidget(btn_2)
            layout.addWidget(btn)
            self.vertical_layout.addLayout(layout)

    def delete_order(self, id_order):
        try:
            with connection.cursor() as cursor:
                # Проверяем, существует ли заказ с таким ID
                cursor.execute("SELECT * FROM orders WHERE id = %s;", (id_order,))
                order = cursor.fetchone()
                if not order:
                    print(f"Заказ с ID {id_order} не найден.")
                    return

                # Удаляем заказ
                cursor.execute("DELETE FROM orders WHERE id = %s;", (id_order,))
                connection.commit()
                print(f"Заказ с ID {id_order} успешно удалён.")
                self.update_orders()
        except Exception as e:
            print(f"Ошибка при удалении заказа: {e}")

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

    def update_orders(self):
        self.clear_layout(self.vertical_layout)
        print("Все удалено")
        for i in [21, 22, 23, 24, 25, 26, 27]:
            self.add_order(f"2024-11-{i}")

    def change_order(self, id_order):
        self.change_order_window = ChangeOrder(id_order)
        self.change_order_window.show()
        self.close()
        
    def resize_window(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.resize(int(screen_width), int(screen_height))
        self.label.setGeometry(0, 0, int(screen_width), int(screen_height * 0.05))
        self.scrollArea.setGeometry(0, int(screen_height * 0.06), int(screen_width), int(screen_height * 0.96))


class ChangeOrder(QtWidgets.QMainWindow, change_order.Ui_MainWindow):
    def __init__(self, id_order):
        super().__init__()
        self.setupUi(self)
        self.order_id = id_order
        self.waiter_id = None
        self.table = None
        self.last_window = None
        cursor.execute("SELECT * FROM orders WHERE id = %s;", (id_order,))
        order = cursor.fetchone()
        cursor.execute("SELECT * FROM waiters;")
        waiters = list(cursor.fetchall())
        self.lineEdit.setText(str(order[1]))

        self.menu = QMenu(self)
        for waiter in waiters:
            action1 = QAction(f"{waiter[1]}", self)
            action1.triggered.connect(partial(self.choose_waiter, waiter[0], waiter[1]))
            self.menu.addAction(action1)
        self.pushButton.setMenu(self.menu)

        self.menu = QMenu(self)
        for i in range(1, 7):
            action1 = QAction(f"Столик №{i}", self)
            action1.triggered.connect(partial(self.choose_table, i, f"Столик №{i}"))
            self.menu.addAction(action1)
        self.pushButton_2.setMenu(self.menu)

        self.pushButton_3.clicked.connect(self.save)
        self.resize_window()

    def choose_waiter(self, id_waiter, name):
        self.waiter_id = id_waiter
        self.pushButton.setText(str(name))

    def choose_table(self, table, text):
        self.table = table
        self.pushButton_2.setText(str(text))

    def save(self):
        if self.lineEdit.text() != "" and self.waiter_id and self.table:
            update_query = """
                            UPDATE orders
                            SET date = %s, waiter_id = %s, table_name = %s
                            WHERE id = %s;
                        """
            cursor.execute(update_query, (self.lineEdit.text(), self.waiter_id, self.table, self.order_id))
            connection.commit()
            print("Обновлено")
            self.last_window = AdminWindow()
            self.last_window.show()
            self.close()
        else:
            dialog = QDialog(self)
            dialog.resize(200, 100)
            dialog.setWindowTitle("Ошибка")
            label = QLabel("", dialog)
            label.setStyleSheet("font-size: 20px;")
            label.setWordWrap(True)
            layout = QVBoxLayout()
            layout.addWidget(label)
            dialog.setLayout(layout)
            label.setText("Некоторые варианты не выбраны")
            dialog.exec_()
            
    def resize_window(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.resize(int(screen_width * 0.15), int(screen_height * 0.25))
        self.label.setGeometry(0, 0, int(screen_width * 0.15), int(screen_height * 0.05))
        self.label_2.setGeometry(0, int(screen_height * 0.05), int(screen_width * 0.04), int(screen_height * 0.04))
        self.lineEdit.setGeometry(int(screen_width * 0.042), int(screen_height * 0.05), int(screen_width * 0.1), int(screen_height * 0.03))
        self.label_3.setGeometry(0, int(screen_height * 0.09), int(screen_width * 0.04), int(screen_height * 0.04))
        self.pushButton.setGeometry(int(screen_width * 0.042), int(screen_height * 0.09), int(screen_width * 0.1), int(screen_height * 0.03))
        self.label_4.setGeometry(0, int(screen_height * 0.13), int(screen_width * 0.04), int(screen_height * 0.04))
        self.pushButton_2.setGeometry(int(screen_width * 0.042), int(screen_height * 0.13), int(screen_width * 0.1), int(screen_height * 0.03))
        self.pushButton_3.setGeometry(int(screen_width * 0.025), int(screen_height * 0.18), int(screen_width * 0.1), int(screen_height * 0.03))

        

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_order_window = None
        self.btn_add_order = QPushButton(self.ui.centralwidget)
        self.btn_add_order.setText("Добавить заказ")
        self.btn_add_order.clicked.connect(self.add_order)
        self.ui.label.setPixmap(QPixmap('cafe.jpg'))
        self.show()
        self.set_text()
        self.changing_the_size()
        self.add_functionality()

    def set_text(self):
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        data = []
        for i in result:
            if i[6] == 'Оформлен' or i[6] == 'Готовится':
                status = i[6]
                cursor.execute("SELECT * FROM waiters WHERE id = %s;", (i[8],))
                waiter = cursor.fetchone()[1]
                cursor.execute("SELECT * FROM customers WHERE id = %s;", (i[3],))
                customer = cursor.fetchone()[1]
                order = []
                for j in i[4].split(';'):
                    cursor.execute("SELECT * FROM menu WHERE id = %s;", (j,))
                    order.append(cursor.fetchone()[1])
                text_order = ';'.join(order)
                data.append(f'{status}: {customer} - {text_order}. Стол №{i[7]}. Стоимость заказа: {int(i[5])} руб. Официант - {waiter}')
        text = '\n\n'.join(data)
        label = QLabel(text)
        font = QFont("Arial", 14)
        label.setFont(font)
        label.setWordWrap(True)
        layout.addWidget(label)
        content_widget.setLayout(layout)
        self.ui.scrollArea.setWidget(content_widget)

        for i in [21, 22, 23, 24, 25, 26, 27]:
            data = []
            for j in result:
                if j[1].strftime("%Y-%m-%d") == f'2024-11-{i}':
                    cursor.execute("SELECT * FROM waiters WHERE id = %s;", (j[8],))
                    waiter = cursor.fetchone()[1]
                    cursor.execute("SELECT * FROM customers WHERE id = %s;", (j[3],))
                    customer = cursor.fetchone()[1]
                    order = []
                    for e in j[4].split(';'):
                        cursor.execute("SELECT * FROM menu WHERE id = %s;", (e,))
                        order.append(cursor.fetchone()[1])
                    text_order = ';'.join(order)
                    data.append(f'{j[2]}  {customer} - {text_order}. Стол №{j[7]}. Стоимость заказа: {int(j[5])} руб. Официант - {waiter}')
            data = sorted(data, key=lambda x: datetime.strptime(x.split()[0], "%H:%M:%S"))
            t = '\n\n'.join(data)
            text_main_info = self.calculate_main_info([j for j in result if j[1].strftime("%Y-%m-%d") == f'2024-11-{i}'])
            self.add_tab(t, f'2024-11-{i}', text_main_info)

    def changing_the_size(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        self.btn_add_order.resize(int(screen_width * 0.5), int(screen_height * 0.04))
        self.btn_add_order.move(int(screen_width * 0.5), 0)
        self.ui.scrollArea.resize(int(screen_width * 0.5), int(screen_height * 0.34))
        self.ui.scrollArea.move(int(screen_width * 0.5), int(screen_height * 0.1))
        self.ui.label_2.move(int(screen_width * 0.51), int(screen_height * 0.02))
        self.ui.label.resize(int(screen_width * 0.5), int(screen_height * 0.442))
        self.ui.label_2.resize(int(screen_width * 0.5), int(screen_height * 0.1))

        self.ui.text.resize(int(screen_width), int(screen_height * 0.07))
        self.ui.text.move(0, int(screen_height * 0.425))

        self.ui.tabWidget.move(0, int(screen_height * 0.5))
        self.ui.tabWidget.resize(int(screen_width), int(screen_height * 0.5))

        self.ui.table_1.resize(int(screen_width * 0.07), int(screen_height * 0.171))
        self.ui.table_2.resize(int(screen_width * 0.07), int(screen_height * 0.171))
        self.ui.table_3.resize(int(screen_width * 0.07), int(screen_height * 0.171))
        self.ui.table_4.resize(int(screen_width * 0.07), int(screen_height * 0.171))
        self.ui.table_5.resize(int(screen_width * 0.07), int(screen_height * 0.171))
        self.ui.table_6.resize(int(screen_width * 0.07), int(screen_height * 0.171))

        self.ui.table_1.move(int(screen_width * 0.038), int(screen_height * 0.035))
        self.ui.table_2.move(int(screen_width * 0.22), int(screen_height * 0.035))
        self.ui.table_3.move(int(screen_width * 0.402), int(screen_height * 0.035))
        self.ui.table_4.move(int(screen_width * 0.038), int(screen_height * 0.221))
        self.ui.table_5.move(int(screen_width * 0.22), int(screen_height * 0.221))
        self.ui.table_6.move(int(screen_width * 0.402), int(screen_height * 0.221))

    def add_tab(self, text, date, text_main_info):
        long_text = QLabel(text)
        long_text.setWordWrap(True)
        font = QFont("Arial", 14)
        long_text.setFont(font)

        scroll_area = QScrollArea()
        scroll_area.setWidget(long_text)
        scroll_area.setWidgetResizable(True)
        main_info = QLabel(text_main_info)
        main_info.setWordWrap(True)
        main_info.setFont(font)
        main_info.setFixedWidth(350)

        tab3_layout = QHBoxLayout()
        tab3_layout.addWidget(scroll_area)
        tab3_layout.addWidget(main_info)

        tab3 = QWidget()
        tab3.setLayout(tab3_layout)

        self.ui.tabWidget.addTab(tab3, date)

    def calculate_main_info(self, res):
        text = ''
        summ, cnt = 0, 0
        for i in res:
            summ += float(i[5])
            cnt += 1
        if cnt != 0:
            text += f'Средний чек - {int(summ/cnt)} руб.\n'
            text += f'Наибольшая сумма заказа - {int(max([float(i[5]) for i in res]))} руб.\n'
            text += f'Наименьшая сумма заказа - {int(min([float(i[5]) for i in res]))} руб.\n'
        return text

    def open_table_info(self, table_name, data):
        self.table_window = TableInfo(table_name, data)
        self.table_window.exec_()

    def add_functionality(self):
        self.ui.table_1.setStyleSheet("""
            QPushButton:hover {
                border: 2px solid red;   /* Подсветка границы при наведении */
            }
        """)
        self.ui.table_1.clicked.connect(lambda: self.open_table_info('Стол №1', sorted([i for i in result if i[7] == 1], key=lambda x: x[2])))
        self.ui.table_2.setStyleSheet("""
            QPushButton:hover {
                border: 2px solid red;   /* Подсветка границы при наведении */
            }
        """)
        self.ui.table_2.clicked.connect(lambda: self.open_table_info('Стол №2', sorted([i for i in result if i[7] == 2], key=lambda x: x[2])))
        self.ui.table_3.setStyleSheet("""
            QPushButton:hover {
                border: 2px solid red;   /* Подсветка границы при наведении */
            }
        """)
        self.ui.table_3.clicked.connect(lambda: self.open_table_info('Стол №3', sorted([i for i in result if i[7] == 3], key=lambda x: x[2])))
        self.ui.table_4.setStyleSheet("""
            QPushButton:hover {
                border: 2px solid red;   /* Подсветка границы при наведении */
            }
        """)
        self.ui.table_4.clicked.connect(lambda: self.open_table_info('Стол №4', sorted([i for i in result if i[7] == 4], key=lambda x: x[2])))
        self.ui.table_5.setStyleSheet("""
            QPushButton:hover {
                border: 2px solid red;   /* Подсветка границы при наведении */
            }
        """)
        self.ui.table_5.clicked.connect(lambda: self.open_table_info('Стол №5', sorted([i for i in result if i[7] == 5], key=lambda x: x[2])))
        self.ui.table_6.setStyleSheet("""
            QPushButton:hover {
                border: 2px solid red;   /* Подсветка границы при наведении */
            }
        """)
        self.ui.table_6.clicked.connect(lambda: self.open_table_info('Стол №6', sorted([i for i in result if i[7] == 6], key=lambda x: x[2])))

    def add_order(self):
        self.add_order_window = AddOrder()
        self.add_order_window.show()
        self.close()


class AddOrder(QtWidgets.QMainWindow, add_order.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.waiter_id = None
        self.table = None
        self.last_window = None
        self.text_order = ""
        self.id_orders = []
        self.price = 0
        cursor.execute("SELECT * FROM waiters;")
        waiters = list(cursor.fetchall())
        cursor.execute("SELECT * FROM menu;")
        orders = list(cursor.fetchall())
        self.menu = QMenu(self)
        for waiter in waiters:
            action1 = QAction(f"{waiter[1]}", self)
            action1.triggered.connect(partial(self.choose_waiter, waiter[0], waiter[1]))
            self.menu.addAction(action1)
        self.pushButton.setMenu(self.menu)

        self.menu = QMenu(self)
        for i in range(1, 7):
            action1 = QAction(f"Столик №{i}", self)
            action1.triggered.connect(partial(self.choose_table, i, f"Столик №{i}"))
            self.menu.addAction(action1)
        self.pushButton_2.setMenu(self.menu)

        self.menu = QMenu(self)
        for i in orders:
            action1 = QAction(f"{i[1]}", self)
            action1.triggered.connect(partial(self.choose_menu, i[0]))
            self.menu.addAction(action1)
        self.pushButton_4.setMenu(self.menu)

        self.pushButton_3.clicked.connect(self.add_order)
        self.resize_window()

    def add_order(self):
        if self.lineEdit.text() != "" and self.lineEdit_2.text() != "" and self.waiter_id and self.table and self.price > 0:
            insert_query = """
                            INSERT INTO customers (full_name)
                            VALUES (%s);
                        """
            cursor.execute(insert_query, (self.lineEdit_2.text(),))
            connection.commit()
            print("Новый заказчик добавлен")
            try:
                customer_id = cursor.lastrowid
                insert_query = """
                                INSERT INTO orders (date, time, name_id, order_description_id, 
                                price, status, table_name, waiter_id)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
                            """
                cursor.execute(insert_query, ("2024-11-27", self.lineEdit.text(), customer_id,
                                              ";".join([str(i) for i in self.id_orders]),
                                              int(self.price),
                                              "Оформлен", self.table, self.waiter_id))
                connection.commit()
                print("Новый заказ сделан")
            except Exception as e:
                print(e)
            self.last_window = Ui()
            self.last_window.showMaximized()
            self.close()
        else:
            dialog = QDialog(self)
            dialog.resize(200, 100)
            dialog.setWindowTitle("Ошибка")
            label = QLabel("", dialog)
            label.setStyleSheet("font-size: 20px;")
            label.setWordWrap(True)
            layout = QVBoxLayout()
            layout.addWidget(label)
            dialog.setLayout(layout)
            label.setText("Некоторые варианты не выбраны")
            dialog.exec_()

    def choose_menu(self, id_dish):
        self.id_orders.append(id_dish)
        cursor.execute("SELECT * FROM menu WHERE id = %s;", (id_dish,))
        order = cursor.fetchone()
        print(order)
        self.text_order += f"{order[1]}\n"
        self.price += int(order[2])
        label = QLabel()
        label.setText(self.text_order)
        font = QFont("Arial", 12)
        label.setFont(font)
        self.scrollArea.setWidget(label)
        self.label_8.setText(f"Цена: {self.price}руб.")

    def choose_waiter(self, id_waiter, name):
        self.waiter_id = id_waiter
        self.pushButton.setText(str(name))

    def choose_table(self, table, text):
        self.table = table
        self.pushButton_2.setText(str(text))
        
    def resize_window(self):
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()
        self.resize(int(screen_width * 0.15), int(screen_height * 0.45))
        self.label.setGeometry(0, 0, int(screen_width), int(screen_height * 0.05))
        self.label_2.setGeometry(0, int(screen_height * 0.05), int(screen_width * 0.04), int(screen_height * 0.04))
        self.lineEdit.setGeometry(int(screen_width * 0.04), int(screen_height * 0.05), int(screen_width * 0.1), int(screen_height * 0.03))
        self.label_5.setGeometry(0, int(screen_height * 0.09), int(screen_width * 0.04), int(screen_height * 0.04))
        self.lineEdit_2.setGeometry(int(screen_width * 0.04), int(screen_height * 0.09), int(screen_width * 0.1), int(screen_height * 0.03))

        self.label_6.setGeometry(0, int(screen_height * 0.13), int(screen_width * 0.04), int(screen_height * 0.04))
        self.pushButton_4.setGeometry(int(screen_width * 0.04), int(screen_height * 0.13), int(screen_width * 0.1), int(screen_height * 0.03))
        self.label_7.setGeometry(int(screen_width * 0.05), int(screen_height * 0.16), int(screen_width * 0.06), int(screen_height * 0.04))
        self.scrollArea.setGeometry(0, int(screen_height * 0.19), int(screen_width * 0.15), int(screen_height * 0.08))
        self.label_8.setGeometry(0, int(screen_height * 0.27), int(screen_width * 0.35), int(screen_height * 0.04))
        self.label_3.setGeometry(0, int(screen_height * 0.31), int(screen_width * 0.04), int(screen_height * 0.04))
        self.pushButton.setGeometry(int(screen_width * 0.04), int(screen_height * 0.31), int(screen_width * 0.1), int(screen_height * 0.03))
        self.label_4.setGeometry(0, int(screen_height * 0.35), int(screen_width * 0.04), int(screen_height * 0.04))
        self.pushButton_2.setGeometry(int(screen_width * 0.04), int(screen_height * 0.35), int(screen_width * 0.1), int(screen_height * 0.03))
        self.pushButton_3.setGeometry(int(screen_width * 0.03), int(screen_height * 0.39), int(screen_width * 0.1), int(screen_height * 0.03))

        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = FirstWindow()
    window.show()
    app.exec_()
