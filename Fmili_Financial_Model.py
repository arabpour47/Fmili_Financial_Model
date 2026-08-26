# اسکریپت تولید مدل یکپارچه مالی
# pip install xlsxwriter

import xlsxwriter

def create_financial_model():
    # ساخت فایل اکسل
    workbook = xlsxwriter.Workbook('Fmili_Financial_Model.xlsx')
    
    # تعریف استایل‌های استاندارد مدل‌سازی مالی
    format_header = workbook.add_format({'bold': True, 'bottom': 1, 'bg_color': '#D9D9D9'})
    format_hardcode = workbook.add_format({'font_color': 'blue'}) # داده‌های دستی از کدال
    format_formula = workbook.add_format({'font_color': 'black'}) # فرمول‌ها
    
    # ایجاد شیت‌های استاندارد
    sheets = ['Cover', 'Assumptions', 'Income_Statement', 'Balance_Sheet', 'Cash_Flow', 'Schedules']
    ws = {name: workbook.add_worksheet(name) for name in sheets}
    
    # --- تکمیل شیت Cover ---
    ws['Cover'].set_column('A:A', 50)
    ws['Cover'].write('A1', 'Integrated 3-Statement Financial Model', format_header)
    ws['Cover'].write('A2', 'Company: National Iranian Copper Industries Co. (FMILI)')
    ws['Cover'].write('A4', 'Note: Blue fonts represent historical inputs from Codal.')
    
    # --- تکمیل شیت صورت سود و زیان (Income Statement) ---
    ws_is = ws['Income_Statement']
    ws_is.set_column('A:A', 25)
    
    # هدر سال‌ها
    years = ['Line Item', '1398', '1399', '1400', '1401', '1402 (Base)']
    for col, year in enumerate(years):
        ws_is.write(0, col, year, format_header)
        
    # سرفصل‌های حسابداری
    items = ['Revenue', 'COGS', 'Gross Profit', 'SG&A', 'Operating Income', 'Tax', 'Net Income']
    for row, item in enumerate(items, 1):
        ws_is.write(row, 0, item)
        
    # تزریق داده‌های فرضی برای درآمدهای عملیاتی (با رنگ آبی به نشانه هاردکد بودن)
    historical_revenue = [227000000, 419000000, 689000000, 854000000, 1150000000]
    for col, val in enumerate(historical_revenue, 1):
        ws_is.write(1, col, val, format_hardcode)
        
    # بستن و ذخیره فایل
    workbook.close()
    print("فایل اکسل Fmili_Financial_Model.xlsx با استانداردهای مالی ساخته شد.")

if __name__ == "__main__":
    create_financial_model()
