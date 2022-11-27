import csv
with open('students.txt','r',encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count=0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            row[2]=int(row[2])
            if row[2]<30:
                print(f'{row[0]}  {row[1]}  {row[4]}')
                line_count += 1
