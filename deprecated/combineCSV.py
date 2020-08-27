import os, glob
import pandas as pd 

def combineCSV():
    try:
        os.chdir(r"C:\Users\svill\Documents\Programación\Proyectos cortos Python\Backmarket scrapper\BMscrapper\CSV")
        extension = 'csv'
        
        # Use glob to match the pattern 'csv'
        all_filenames = [i for i in glob.glob('*.{}'.format(extension))]

        # Combine all files in the list and export as CSV
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])

        # Export to CSV
        combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
    except Exception as err:
        print('Ha habido un error al combinar los CSV: '+ str(err))
        
combineCSV()