import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QMessageBox
from PyQt6.QtGui import QFont   
from menu_bar import MenuBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Editor de Roteiros")
        self.setGeometry(100, 100, 800, 600)
        
        # Criando o editor de texto
        self.text_edit = QTextEdit(self)
        self.text_edit.setPlaceholderText("Escreva seu roteiro aqui...")
        
        # Aplicando estilo de roteiro
        self.apply_script_style()
        
        # Layout principal
        central_widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
        # Criando menus
        self.menu_bar = MenuBar(self)
        self.setMenuBar(self.menu_bar)
    
    def apply_script_style(self):
        font = QFont("Courier New", 12)
        self.text_edit.setFont(font)
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #f5f5f5;
                color: #000000;
                padding: 20px;
                border: none;
                selection-background-color: #b0c4de;
            }
        """)
    
    def set_text_format(self, format_type):
        font = QFont("Courier New", 12)
        if format_type == "char":
            font.setBold(True)
        elif format_type == "dialog":
            font.setItalic(True)
        elif format_type == "action":
            font.setBold(False)
            font.setItalic(False)
        elif format_type == "transition":
            font.setBold(True)
            font.setItalic(True)
        self.text_edit.setFont(font)
    
    def show_about(self):
        QMessageBox.about(self, "Sobre", "Editor de Roteiros\nVersão 1.0\nDesenvolvido com PyQt6")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
