from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QMessageBox
from functools import partial

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("TicTacToe")
        self.setFixedSize(350, 350)
        self.layout = QGridLayout()

        self.player = "X"
        self.grid = [[None] * 3 for _ in range(3)]

        self.buttons = []
        for row in range(3):
            button_row = []
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(partial(self.make_move, row, col))  # Use partial function
                self.layout.addWidget(button, row, col)
                button_row.append(button)
            self.buttons.append(button_row)

        self.status_label = QLabel("Player X's turn")
        self.layout.addWidget(self.status_label, 3, 0, 1, 3, Qt.AlignCenter)

        self.setLayout(self.layout)

    def make_move(self, row, col):
        if self.grid[row][col] is not None:
            return

        self.grid[row][col] = self.player
        self.buttons[row][col].setText(self.player)

        if self.check_winner():
            self.show_winner_message()
            self.reset_game()
            return

        if self.check_draw():
            self.show_draw_message()
            self.reset_game()
            return

        self.player = "O" if self.player == "X" else "X"
        self.status_label.setText("Player {}'s turn".format(self.player))

    def check_winner(self):
        # Check rows
        for row in self.grid:
            if row[0] == row[1] == row[2] and row[0] is not None:
                return True

        # Check columns
        for col in range(3):
            if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] is not None:
                return True

        # Check diagonals
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[0][0] is not None:
            return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[0][2] is not None:
            return True

        return False

    def check_draw(self):
        for row in self.grid:
            if None in row:
                return False
        return True

    def show_winner_message(self):
        winner = self.player
        QMessageBox.information(self, "Game Over", "Player {} wins!".format(winner))

    def show_draw_message(self):
        QMessageBox.information(self, "Game Over", "It's a draw!")

    def reset_game(self):
        self.player = "X"
        self.grid = [[None] * 3 for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.setText("")
        self.status_label.setText("Player X's turn")


if __name__ == "__main__":
    app = QApplication([])
    game = TicTacToe()
    game.show()
    app.exec()
