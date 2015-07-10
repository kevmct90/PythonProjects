##  You've got a stray byte floating around. You can find it by running
with open("Week_4_Example_2_Return_Values.py") as fp:
    for i, line in enumerate(fp):
        if "\xe2" in line:
            print i, repr(line)