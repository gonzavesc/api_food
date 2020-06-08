import sys
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
def upload_food(values):
    ok = 0
    while ok == 0:
        try:
            creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)
            ok = 1
        except:
            pass
    ok = 0
    while ok == 0:
        try:
            client = gspread.authorize(creds)
            ok = 1
        except:
            pass
    gsh = client.open('Comida')
    sheet = gsh.get_worksheet(0)
    sheet2 = gsh.get_worksheet(1)
    tod = datetime.date.today()
    day = "{}".format(tod)
    column1 = sheet.col_values(1)
    column2 = sheet.col_values(2)
    column2_5 = sheet2.col_values(5)
    column2_1 = sheet2.col_values(1)
    codes = values['code']
    qtty = float(values['quantity'])
    energ_100 = float(values['nutriments']['calories'])
    energ = energ_100 * qtty / 100
    fat_100 = float(values['nutriments']['fat_value'])
    fat = fat_100 * qtty / 100
    prot_100 = float(values['nutriments']['proteins_value'])
    prot =  prot_100 * qtty / 100
    carbs_100 = float(values['nutriments']['carbohydrates_value'])
    carbs =  carbs_100 * qtty / 100
    name = values['product_name']
    if day not in column1:
        L = len(column2)
        sheet.update_cell(L+1,1,day)
        sheet.update_cell(L + 1, 3, qtty)
        sheet.update_cell(L + 1, 4, carbs)
        sheet.update_cell(L + 1, 5, fat)
        sheet.update_cell(L + 1, 6, prot)
        sheet.update_cell(L + 1, 7, energ)

        sheet.update_cell(L + 2, 2, name)
        sheet.update_cell(L + 2, 3, qtty)
        sheet.update_cell(L + 2, 4, carbs)
        sheet.update_cell(L + 2, 5, fat)
        sheet.update_cell(L + 2, 6, prot)
        sheet.update_cell(L + 2, 7, energ)
        sheet.update_cell(L + 2, 8, codes)
    else:
        L = len(column2)
        J = column1.index(day)
        print(J)
        energ_tot = float(sheet.cell(J + 1, 7).value)
        fat_tot = float(sheet.cell(J + 1, 5).value)
        prot_tot = float(sheet.cell(J + 1, 6).value)
        carbs_tot = float(sheet.cell(J + 1, 4).value)
        qtty_tot = float(sheet.cell(J + 1, 3).value)
        
        sheet.update_cell(J + 1, 3, qtty + qtty_tot)
        sheet.update_cell(J + 1, 4, carbs + carbs_tot)
        sheet.update_cell(J + 1, 5, fat + fat_tot)
        sheet.update_cell(J + 1, 6, prot + prot_tot)
        sheet.update_cell(J + 1, 7, energ + energ_tot)

        sheet.update_cell(L + 1, 2, name)
        sheet.update_cell(L + 1, 3, qtty)
        sheet.update_cell(L + 1, 4, carbs)
        sheet.update_cell(L + 1, 5, fat)
        sheet.update_cell(L + 1, 6, prot)
        sheet.update_cell(L + 1, 7, energ)
        sheet.update_cell(L + 1, 8, codes)
    if codes not in column2_5:
        L = len(column2_1)
        sheet2.update_cell(L + 1, 1, name)
        sheet2.update_cell(L + 1, 2, energ_100)
        sheet2.update_cell(L + 1, 3, prot_100)
        ratio = prot_100 / energ_100 * 100
        sheet2.update_cell(L + 1, 4, ratio)
        sheet2.update_cell(L + 1, 5, codes)

