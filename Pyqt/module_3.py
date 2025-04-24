import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget

app = QApplication(sys.argv)

# Создание окна
window = QWidget()
window.setWindowTitle("Пример QLabel")
window.setGeometry(100, 100, 400, 200)  # Установка размеров окна

# Создание метки и установка ее как дочерний элемент для окна
label = QLabel("Привет, мир!", parent=window)
label.move(150, 80)  # Позиционирование метки вручную

# Показ окна
window.show()

sys.exit(app.exec())