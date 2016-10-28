import sys
from typing import Callable

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget
from savings import PresentRequiredEarningsObserver
from savings import SavingsObserver


class QtRequiredEarningsObserver(PresentRequiredEarningsObserver):
    def __init__(self):
        super().__init__()
        self.required_earnings = None

    def did_present_required_earnings(self, required_earnings: float):
        self.required_earnings = required_earnings


class QtSavingsObserver(SavingsObserver):
    def register_savings_functions(self, present_required_earnings: Callable[[int,
                                                                              float,
                                                                              PresentRequiredEarningsObserver],
                                                                             None]):
        qt_application = QApplication(sys.argv)
        desktop_center = QDesktopWidget().availableGeometry().center()

        main_window = QWidget()

        desired_savings_title_label = QLabel('Desired Savings')
        desired_savings_value_edit = QLineEdit()

        tax_rate_title_label = QLabel('Tax Rate')
        tax_rate_value_edit = QLineEdit()

        required_earnings_title_label = QLabel('Need to earn')
        required_earnings_value_label = QLabel('-')

        calculate_button = QPushButton('Calculate')

        def handle_calculate_event():
            tax_rate = int(tax_rate_value_edit.text())
            desired_savings = float(desired_savings_value_edit.text())
            observer = QtRequiredEarningsObserver()
            present_required_earnings(tax_rate, desired_savings, observer)
            required_earnings = observer.required_earnings
            required_earnings_value_label.setText('{}'.format(required_earnings))

        calculate_button.clicked.connect(handle_calculate_event)
        desired_savings_value_edit.returnPressed.connect(handle_calculate_event)
        tax_rate_value_edit.returnPressed.connect(handle_calculate_event)

        grid = QGridLayout()
        grid.setSpacing(20)

        grid.addWidget(desired_savings_title_label, 1, 0)
        grid.addWidget(desired_savings_value_edit, 1, 1)

        grid.addWidget(tax_rate_title_label, 2, 0)
        grid.addWidget(tax_rate_value_edit, 2, 1)

        grid.addWidget(required_earnings_title_label, 3, 0)
        grid.addWidget(required_earnings_value_label, 3, 1)

        grid.addWidget(calculate_button, 4, 1)

        main_window.setLayout(grid)

        main_window.setGeometry(300, 300, 300, 150)
        main_window.setWindowTitle('Buttons')

        widget_frame_geometry = main_window.frameGeometry()
        widget_frame_geometry.moveCenter(desktop_center)
        main_window.show()
        sys.exit(qt_application.exec_())