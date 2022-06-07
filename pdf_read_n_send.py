import camelot
import os
import sheetsAPI

file = 'extratovhi.pdf'
#sheet_id = '1EzkwOviqVq4D0B96ugkvKRpb37qgH0qQxIcEclcWtEM'

# extract all the tables in the PDF file
tables = camelot.read_pdf(file,pages='all')
print(tables[1].df)
#for table in tables:
   # sheetsAPI.sendData(table.df.values.tolist(),sheet_id,'Vitoria!A:Z','OVERWRITE')
   