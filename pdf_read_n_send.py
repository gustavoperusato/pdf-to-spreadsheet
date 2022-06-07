import camelot
import sheetsAPI


file = '' # add your pdf filename (Ex: 'file.pdf')

sheet_id = '' # add your Spreadsheet ID. (To get it, copy the link of your spreadsheet and get the key beetween the "/d/" and the "/edit".
# Ex: In the link: 'https://docs.google.com/spreadsheets/d/1g2vv_Nz4m0Akau-1245WaW0C38P1d2x0E772tTzdqh0/edit#gid=1853242632',
# the ID would be: '1g2vv_Nz4m0Akau-1245WaW0C38P1d2x0E772tTzdqh0'

tables = camelot.read_pdf(file,pages='all')

for table in tables:
    sheetsAPI.sendData(table.df.values.tolist(),sheet_id,'Sheet1!A:Z','OVERWRITE')
