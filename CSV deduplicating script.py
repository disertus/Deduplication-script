# Name of the original csv file: davidyurman.com-backlinks.csv

import csv
import time
from tkinter import *


# Defining the function activated by the button

def timer_wrapper(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func()
        end = time.time()
        return print(start - end)

    return wrapper


def write_deduplicated_links_to_new_csv(cleaned_list, dirty_list):
    """Writes the deduplicated entries into a new CSV file"""

    # Creating a new CSV file
    new_csv = new_csv_text.get()

    # 'newline' parameter makes sure no blank lines appear between cells in the new_csv, otherwise they do
    with open(new_csv, "w+", newline='', encoding='utf-8') as fhand:
        csv_writer = csv.writer(fhand)
        # putting 'newcell' in [] assures that the list items are iterated as a whole, not as characters of the string
        [csv_writer.writerow([newcell]) for newcell in cleaned_list]
        print("*********\nDeletion of partial duplicates among URL - Finished")

    l1 = Label(window, text='The operation has been successfully finished! \nTotal amount of items changed: \n' + str(
        len(dirty_list)) + ' ---> ' + str(len(cleaned_list)) + ' items\n', bg='#6A5F5D', fg='#8EE373')
    l1.grid(row=3, column=0, padx=10, pady=10)

    print("End of program...")
    return cleaned_list


def clean_the_duplicates(dirty_list):
    """Deletes the duplicates from the original list of domains and adds unique links to a new 'clean' list"""

    empty_list = []
    empty_set = set()

    # Trying to find all expressions with regex pattern for URLs

    for i in dirty_list:
        search_item = re.findall('//.*?/', i)  # Identifies the url pattern //.../ inside the raw
        if len(search_item) < 1:
            continue
        elif search_item[0] not in empty_set:
            empty_set.add(search_item[0])
            empty_list.append(i)
        else:
            continue
    return write_deduplicated_links_to_new_csv(empty_list, dirty_list=dirty_list)


def read_the_csv():
    """Opens the original csv file, reads through each row and appends contents to an empty list"""

    try:
        list_with_duplicates = []
        with open(original_csv_text.get(), newline='', encoding='utf-8') as csv_file:
            row_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            for row in row_reader:
                list_with_duplicates.append(row[0])

    except:
        l1 = Label(window, text='The operation has failed due to bad input! \nPlease try again \n', bg='#6A5F5D',
                   fg='#FF8B73')
        l1.grid(row=3, column=0, padx=10, pady=15)

    return clean_the_duplicates(list_with_duplicates)


@timer_wrapper
def click():
    """High-level function triggered by the GUI button"""

    return read_the_csv()


# Creating a window object
window = Tk()
window.title("Deduplication script")
window.configure(background='#6A5F5D')

# Creating explanatory text near the 'input' fields
l1 = Label(window, bg='#6A5F5D', height=2)
l1.grid(row=0, column=0)

l1 = Label(window, width=40, text="Enter the name of a CSV file: ", bg='#6A5F5D', fg='#E5D4D1')
l1.grid(row=1, column=0)

l1 = Label(window,
           width=40,
           text="Give a name to the new CSV file \nwhich will store the results: ",
           bg='#6A5F5D',
           fg='#E5D4D1')
l1.grid(row=2,
        column=0)

l1 = Label(window, bg='#6A5F5D', height=3)
l1.grid(row=3, column=0)

# Adding the text input field
original_csv_text = StringVar()
old_csv_name = Entry(window, width=40, textvariable=original_csv_text, bg='#6A5F5D', fg='#E5D4D1')
old_csv_name.grid(row=1, column=1, padx=20)

new_csv_text = StringVar()
new_csv_name = Entry(window, width=40, textvariable=new_csv_text, bg='#6A5F5D', fg='#E5D4D1')
new_csv_name.grid(row=2, column=1, padx=20)

# Adding a button activating program's function 'click()'
Button(window, text='Run', width=10, bg='#6A5F5D', fg='#E5D4D1', command=click).grid(row=3, column=1, sticky=N)

# Output window showing the 'writing' process + scroll bar to navigate through results


window.mainloop()
