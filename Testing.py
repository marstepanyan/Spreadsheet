from Spreadsheet import Spreadsheet
from Cell import Cell
from Colors import Color


def testing(func, arg):
    if func(arg):
        print(f'{type(arg)}\'s {func.__name__} passed')
    else:
        print(f'{type(arg)}\'s {func.__name__} failed')


cell1 = Cell('9', Color(7))


def test_get_value(cell):
    if cell.get_value() != '9':
        return False
    return True


def test_get_color(cell):
    if cell.get_color() != Color(7):
        return False
    return True


def test_to_int(cell):
    if cell.to_int() != 9:
        return False
    return True


def test_to_float(cell):
    if cell.to_float() != 9.0:
        return False
    return True


def test_reset(cell):
    cell.reset()
    if cell1.get_value() != '' and cell1.get_color() != '':
        return False
    return True


spread_sheet1 = Spreadsheet(5, 7)
# print('spread_sheet1:', spread_sheet1)


def test_set_cell_at(spread_sheet):
    spread_sheet.set_cell_at(2, 1, cell1)
    if cell1 != spread_sheet.get_sheet()[2][1]:
        return False
    return True


def test_get_cell_at(spread_sheet):
    if spread_sheet.get_cell_at(2, 1) != cell1:
        return False
    return True


def test_add_row(spread_sheet):
    spread_sheet.add_row(1)
    if spread_sheet.get_cell_at(2+1, 1) != cell1:
        return False
    return True


def test_add_column(spread_sheet):
    spread_sheet.add_column(1)
    if spread_sheet.get_cell_at(3, 1+1) != cell1:
        return False
    return True


def test_remove_row(spread_sheet):
    spread_sheet.remove_row(1)
    if spread_sheet.get_cell_at(3 - 1, 2) != cell1:
        return False
    return True


def test_remove_column(spread_sheet):
    spread_sheet.remove_column(1)
    if spread_sheet.get_cell_at(2, 2-1) != cell1:
        return False
    return True


def test_swap_rows(spread_sheet):
    spread_sheet.swap_rows(1, 2)
    if spread_sheet.get_cell_at(1, 1) != cell1:
        return False
    return True


def test_swap_columns(spread_sheet):
    spread_sheet.swap_columns(1, 0)
    if spread_sheet.get_cell_at(1, 0) != cell1:
        return False
    return True


def test_cell_funcs():
    print('Testing cell\'s methods.')
    for f in [test_get_value, test_get_color, test_to_int, test_to_float, test_reset]:
        testing(f, cell1)
    return 'Done!'


def test_spreadsheet_funcs():
    print('Testing spreadsheet\'s methods.')
    for f in [test_set_cell_at, test_get_cell_at, test_add_row, test_add_column,
              test_remove_row, test_remove_column, test_swap_rows, test_swap_columns]:
        testing(f, spread_sheet1)
    return 'Done!'


print(test_cell_funcs())
print()
print(test_spreadsheet_funcs())
