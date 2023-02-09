from Spreadsheet import Spreadsheet
from Cell import Cell
from Colors import Color


def test_cells_funcs():
    cell1 = Cell('7', Color(7))

    if cell1.get_value() != '7':
        print('cell\'s get_value() function failed')
    else:
        print('cell\'s get_value() function passed')

    if cell1.get_color() != Color(7):
        print('cell\'s get_color() function failed')
    else:
        print('cell\'s get_color() function passed')

    if cell1.to_int() != 7:
        print('cell\'s to_int() function failed')
    else:
        print('cell\'s to_int() function passed')

    if cell1.to_float() != 7.0:
        print('cell\'s to_float() function failed')
    else:
        print('cell\'s to_float() function passed')

    # print('cell1: ', cell1)

    cell1.reset()
    if cell1.get_value() != '' and cell1.get_color() != '':
        print('cell\'s reset() function failed')
    else:
        print('cell\'s reset() function passed')

    # print('cell1 after reset: ', cell1)


print('Testing cell\'s methods.')
test_cells_funcs()
print()

cell2 = Cell('9', 'red')


def test_spreadsheet_funcs():
    spread_sheet = Spreadsheet(5, 7)

    spread_sheet.set_cell_at(2, 1, cell2)
    if cell2 != spread_sheet.get_sheet()[2, 1]:
        print('Spreadsheet\'s set_cell_at function failed')
    else:
        print('Spreadsheet\'s set_cell_at function passed')

    if spread_sheet.get_cell_at(2, 1) != cell2:
        print('Spreadsheet\'s get_cell_at function failed')
    else:
        print('Spreadsheet\'s get_cell_at function passed')

    spread_sheet.add_row(2)
    if spread_sheet.get_cell_at(2+1, 1) != cell2:
        print('Spreadsheet\'s add_row function failed')
    else:
        print('Spreadsheet\'s add_row function passed')

    spread_sheet.add_column(1)
    if spread_sheet.get_cell_at(3, 1+1) != cell2:
        print('Spreadsheet\'s add_column function failed')
    else:
        print('Spreadsheet\'s add_column function passed')

    spread_sheet.remove_row()
    if spread_sheet.get_cell_at(3-1, 2) != cell2:
        print('Spreadsheet\'s remove_row function failed')
    else:
        print('Spreadsheet\'s remove_row function passed')

    spread_sheet.remove_column()
    if spread_sheet.get_cell_at(2, 2-1) != cell2:
        print('Spreadsheet\'s remove_column function failed')
    else:
        print('Spreadsheet\'s remove_column function passed')

    spread_sheet.swap_rows(1, 2)
    if spread_sheet.get_cell_at(1, 1) != cell2:
        print('Spreadsheet\'s swap_row function failed')
    else:
        print('Spreadsheet\'s swap_row function passed')

    spread_sheet.swap_columns(1, 0)
    if spread_sheet.get_cell_at(1, 0) != cell2:
        print('Spreadsheet\'s swap_column function failed')
    else:
        print('Spreadsheet\'s swap_column function passed')

    # print(spread_sheet)


print('Testing spreadsheet\'s methods.')
test_spreadsheet_funcs()
