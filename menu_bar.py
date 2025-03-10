from PyQt6.QtWidgets import QMenuBar, QMenu, QFileDialog
from PyQt6.QtGui import QAction

class MenuBar(QMenuBar):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_menu()

    def init_menu(self):
        # Menu Arquivo
        file_menu = self.addMenu("Arquivo")
        
        new_action = QAction("Novo", self)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = QAction("Abrir", self)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        save_action = QAction("Salvar", self)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        file_menu.addSeparator()

        exit_action = QAction("Sair", self)
        exit_action.triggered.connect(self.parent.close)
        file_menu.addAction(exit_action)

        # Menu Editar
        edit_menu = self.addMenu("Editar")

        copy_action = QAction("Copiar", self)
        copy_action.triggered.connect(self.parent.text_edit.copy)
        edit_menu.addAction(copy_action)

        paste_action = QAction("Colar", self)
        paste_action.triggered.connect(self.parent.text_edit.paste)
        edit_menu.addAction(paste_action)

        # Menu Formato
        format_menu = self.addMenu("Formato")

        char_action = QAction("Personagem", self)
        char_action.triggered.connect(lambda: self.parent.set_text_format("char"))
        format_menu.addAction(char_action)

        dialog_action = QAction("Diálogo", self)
        dialog_action.triggered.connect(lambda: self.parent.set_text_format("dialog"))
        format_menu.addAction(dialog_action)

        action_action = QAction("Ação", self)
        action_action.triggered.connect(lambda: self.parent.set_text_format("action"))
        format_menu.addAction(action_action)

        transition_action = QAction("Transição", self)
        transition_action.triggered.connect(lambda: self.parent.set_text_format("transition"))
        format_menu.addAction(transition_action)

        # Menu Ajuda
        help_menu = self.addMenu("Ajuda")

        about_action = QAction("Sobre", self)
        about_action.triggered.connect(self.parent.show_about)
        help_menu.addAction(about_action)

    def new_file(self):
        self.parent.text_edit.clear()

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self.parent, "Abrir Arquivo", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "r", encoding="utf-8") as file:
                self.parent.text_edit.setPlainText(file.read())

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self.parent, "Salvar Arquivo", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(self.parent.text_edit.toPlainText())

