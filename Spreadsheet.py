class Spreadsheet:
    def __init__(self, row: int, column: int):
        self._sheet = [['']*column for _ in range(row)]
        self._sheet_col = column
        self._sheet_row = row

    def get_sheet(self):
        return self._sheet

    def set_cell_at(self, row: int, col: int, cell):
        self._sheet[row][col] = cell

    def get_cell_at(self, row: int, col: int):
        return self._sheet[row][col]

    def add_row(self, row_index: int):
        self._sheet.insert(row_index + 1, ['']*self._sheet_col)
        return self._sheet

    def remove_row(self, row_index: int):
        del self._sheet[row_index:row_index+1]
        return self._sheet

    def add_column(self, col_index: int):
        for item in self._sheet:
            item.insert(col_index, '')
        return self._sheet

    def remove_column(self, col_index: int):
        for item in self._sheet:
            del item[col_index:col_index+1]
        return self._sheet

    def swap_rows(self, row1: int, row2: int):
        self._sheet[row1], self._sheet[row2] = self._sheet[row2], self._sheet[row1]
        return self._sheet

    def swap_columns(self, col1: int, col2: int):
        for item in self._sheet:
            item[col1], item[col2] = item[col2], item[col1]
        return self._sheet

    def __repr__(self):
        return str(self._sheet)
