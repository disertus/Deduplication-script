# Name of the original csv file: davidyurman.com-backlinks.csv

import csv
from tkinter import *
from tkinter import filedialog

# Defining the function activated by the button

def click():
    old_csv = old_csv_text.get()

    # Opening the original csv file, reading through each row and appending contents to an empty_list
    try:
        empty_list = []
        with open(old_csv, newline='', encoding='utf-8') as csvfile:
            rowreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in rowreader:
                cell = row[0]
                empty_list.append(cell)

    except:
        l1 = Label(window, text='The operation has failed due to bad input! \nPlease try again \n', bg='#6A5F5D', fg='#FF8B73')
        l1.grid(row=3, column=0, padx=10, pady=15)

    # Creating/opening the new CSV file
    new_csv = new_csv_text.get()
    fhand = open(new_csv, "w+", newline='', encoding='utf-8') # 'newline' parameter makes sure no blank lines appear between cells in the new_csv, otherwise they do
    items = empty_list                      # reference to the list filled with rows from the old_csv

    emplist1 = []
    emplist2 = []

    # Trying to find all expressions with regex pattern for URLs

    for i in items:
        searchitem = re.findall('//.*?/', i)
        if len(searchitem) < 1:
            continue
        elif searchitem in emplist1:
            continue
        else:
            emplist1.append(searchitem)
            emplist2.append(i)

    # Writing deduplicated items into a new CSV file
    csvwriter = csv.writer(fhand)
    for newcell in emplist2:
        csvwriter.writerow([newcell])   # putting 'newcell' in [] assures that the list items are iterated as a whole, not characters of the string
    print("*********\nDeletion of partial duplicates among URL - Finished")

    l1 = Label(window, text='The operation has been successfully finished! \nTotal amount of items changed: \n' + str(len(empty_list)) + ' ---> ' + str(len(emplist2)) + ' items\n', bg='#6A5F5D', fg='#8EE373')
    l1.grid(row=3, column=0, padx=10, pady=10)


    result=emplist2

    print("End of program...")
    return result



# Creating a window object
window=Tk()
window.title ("Deduplication script")
window.configure (background='#6A5F5D')

# Creating explanatory text near the 'input' fields
l1=Label (window, bg='#6A5F5D', height=2)
l1.grid (row=0, column=0)

l1=Label (window,  width=40, text="Enter the name of a CSV file: ", bg='#6A5F5D', fg='#E5D4D1')
l1.grid (row=1, column=0)

l1=Label (window, width=40, text="Give a name to the new CSV file \nwhich will store the results: ", bg='#6A5F5D', fg='#E5D4D1')
l1.grid(row=2, column=0)

l1=Label(window, bg='#6A5F5D', height=3)
l1.grid(row=3, column=0)

# Adding the text input field
old_csv_text=StringVar()
old_csv_name=Entry(window, width=40, textvariable=old_csv_text, bg='#6A5F5D', fg='#E5D4D1')
old_csv_name.grid(row=1, column=1, padx=20)

new_csv_text=StringVar()
new_csv_name=Entry(window, width=40, textvariable=new_csv_text, bg='#6A5F5D', fg='#E5D4D1')
new_csv_name.grid(row=2, column=1, padx=20)

# Adding a button activating program's function 'click()'
Button(window, text='Run', width=10, bg='#6A5F5D', fg='#E5D4D1', command=click) .grid(row=3, column=1, sticky=N)

# Output window showing the 'writing' process + scroll bar to navigate through results


window.mainloop()