import sys
from PyQt6.QtWidgets import QApplication, QMainWindow

# Создание приложения
app = QApplication(sys.argv)

# Создание главного окна
window = QMainWindow()
window.setWindowTitle("Простое окно")
window.setGeometry(100, 100, 600, 400)  # Устанавливаем размер и позицию окна

# Показ окна
window.show()

# Запуск основного цикла обработки событий
sys.exit(app.exec())