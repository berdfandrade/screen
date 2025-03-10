import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtGui import QAction, QKeySequence, QFont

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
        
        # Criando menu
        self.create_menu()
    
    def create_menu(self):
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("Arquivo")
        
        new_action = QAction("Novo", self)
        new_action.setShortcut(QKeySequence.StandardKey.New)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction("Abrir", self)
        open_action.setShortcut(QKeySequence.StandardKey.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        save_action = QAction("Salvar", self)
        save_action.setShortcut(QKeySequence.StandardKey.Save)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        exit_action = QAction("Sair", self)
        exit_action.setShortcut(QKeySequence.StandardKey.Quit)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
    
    def new_file(self):
        self.text_edit.clear()
    
    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Abrir Arquivo", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "r", encoding="utf-8") as file:
                self.text_edit.setText(file.read())
    
    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Salvar Arquivo", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.text_edit.toPlainText())
    
    def apply_script_style(self):
        # Definir fonte padrão para roteiro (Courier New, 12pt)
        font = QFont("Courier New", 12)
        self.text_edit.setFont(font)
        
        # Aplicando estilo visual para parecer uma folha de roteiro
        self.text_edit.setStyleSheet("""
            QTextEdit {
                background-color: #f5f5f5;
                color: #000000;
                padding: 20px;
                border: none;
                selection-background-color: #b0c4de;
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())