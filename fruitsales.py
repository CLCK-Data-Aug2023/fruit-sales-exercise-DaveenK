import pandas as pd
import csv

fruit_sales = pd.DataFrame([[35, 21], [41, 34]],
columns = ['Apples', 'Bananas'],
index = ["2017 Sales", "2018 Sales"])
print(fruit_sales)

#fruit_sales.to_csv('fruits.csv', index=False)

csv_filename = '/Users/Nick/Documents/Daveen/Code_Kentucky/fruit-sales-exercise-DaveenK/fruits.csv'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(fruit_sales)

print(f'CSV file "{csv_filename}" has been created.')