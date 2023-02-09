import numpy as np
from Cell import Cell


class Spreadsheet:
    def __init__(self, row, column):
        self._sheet = np.empty(shape=(row, column), dtype=Cell)

    def get_sheet(self):
        return self._sheet

    def set_cell_at(self, row, col, cell: Cell):
        self._sheet[row, col] = cell

    def get_cell_at(self, row, col):
        return self._sheet[row, col]

    def add_row(self, row_index):
        pass

    def remove_row(self):
        pass

    def add_column(self, col_index):
        pass

    def remove_column(self):
        pass

    def swap_rows(self, row1, row2):
        pass

    def swap_columns(self, col1, col2):
        pass

    def __repr__(self):
        return str(self._sheet)
