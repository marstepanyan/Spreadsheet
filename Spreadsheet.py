class Spreadsheet:
    def __init__(self, row: int, column: int):
        self._sheet = [['']*column for _ in range(row)]
        self._sheet_col = column
        self._sheet_row = row

    def get_sheet(self):
        return self._sheet

    def set_cell_at(self, row: int, col: int, cell):
        if row > self._sheet_row or col > self._sheet_col:
            raise IndexError('out of spreadsheet')
        if (type(row) is not int) or (type(col) is not int):
            raise ValueError('row and col must be int')
        if row < 0 or col < 0:
            raise ValueError('row and col must not be negative')

        self._sheet[row][col] = cell

    def get_cell_at(self, row: int, col: int):
        if row > self._sheet_row or col > self._sheet_col:
            raise IndexError('out of spreadsheet')
        if (type(row) is not int) or (type(col) is not int):
            raise ValueError('row and col must be int')
        if row < 0 or col < 0:
            raise ValueError('row and col must not be negative')

        return self._sheet[row][col]

    def add_row(self, row_index: int):
        if row_index > self._sheet_row:
            raise IndexError('out of spreadsheet')
        if not isinstance(row_index, int):
            raise ValueError('row index must be int')
        if row_index < 0:
            raise ValueError('row index must not be negative')

        self._sheet.insert(row_index + 1, ['']*self._sheet_col)
        return self._sheet

    def remove_row(self, row_index: int):
        if row_index > self._sheet_row:
            raise IndexError('out of spreadsheet')
        if not isinstance(row_index, int):
            raise ValueError('row index must be int')
        if row_index < 0:
            raise ValueError('row index must not be negative')

        del self._sheet[row_index:row_index+1]
        return self._sheet

    def add_column(self, col_index: int):
        if col_index > self._sheet_col:
            raise IndexError('out of spreadsheet')
        if not isinstance(col_index, int):
            raise ValueError('column index must be int')
        if col_index < 0:
            raise ValueError('column index must not be negative')

        for item in self._sheet:
            item.insert(col_index, '')
        return self._sheet

    def remove_column(self, col_index: int):
        if col_index > self._sheet_col:
            raise IndexError('out of spreadsheet')
        if not isinstance(col_index, int):
            raise ValueError('column index must be int')
        if col_index < 0:
            raise ValueError('column index must not be negative')

        for item in self._sheet:
            del item[col_index:col_index+1]
        return self._sheet

    def swap_rows(self, row1: int, row2: int):
        if row1 > self._sheet_row or row2 > self._sheet_row:
            raise IndexError('out of spreadsheet')
        if (type(row1) is not int) or (type(row2) is not int):
            raise ValueError('row and col must be int')
        if row1 < 0 or row2 < 0:
            raise ValueError('row and col must not be negative')

        self._sheet[row1], self._sheet[row2] = self._sheet[row2], self._sheet[row1]
        return self._sheet

    def swap_columns(self, col1: int, col2: int):
        if col1 > self._sheet_col or col2 > self._sheet_col:
            raise IndexError('out of spreadsheet')
        if (type(col1) is not int) or (type(col2) is not int):
            raise ValueError('row and col must be int')
        if col1 < 0 or col2 < 0:
            raise ValueError('row and col must not be negative')

        for item in self._sheet:
            item[col1], item[col2] = item[col2], item[col1]
        return self._sheet

    def __repr__(self):
        return str(self._sheet)
