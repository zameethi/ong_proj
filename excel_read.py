# import openpyxl
# from openpyxl import load_workbook
#
# workbook = load_workbook('Visão Geral Iniciativas_v2.xlsm')
# worksheet = workbook.get_active_sheet()
#
# ws_range = worksheet.range('A1:Z20')
# for row in ws_range:
#     print(row)
#
#
#
#
#
# # print(sh['A2'].fill.start_color.index)

from StyleFrame import StyleFrame, Styler, utils



#
sf = StyleFrame.read_excel('teste.xlsx', sheet_name='Planilha1', read_style=True)
# print(sf)
#
# #
# sf = sf[[col for col in sf.columns
#          if col.style.fill.fgColor.rgb in ('FFFFFFFF', utils.colors.white)]]
#          # "white" can be represented as 'FFFFFFFF' or
#          # '00FFFFFF' (which is what utils.colors.white is set to)
# print(sf)
