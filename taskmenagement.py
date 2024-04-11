########
# יצירת תיקיה
########

import os
DirPath = 'Tasks' 
filename = 'tasks.txt'
# יצירת תיקיה
os.makedirs(DirPath, exist_ok=True)
# מיקום
FilePath = os.path.join(DirPath, filename)


#####
# רישום לקובץ מתוך מערך
#####

tesks = [[1,'דוד','07.04.24','הערה'],
        [2,'שמואל','08.04.24','הערה'],
        [3,'פינחס','09.04.24','הערה']]
string = ''

# פעולות על הקובץ
with open(FilePath, 'w+', encoding='utf-8') as Fl:    
    for task in tesks:
        for pice in task:
            string += str(pice)+', '
        string += '\n'
    Fl.write(string)

######
# הוצאת מהקובץ חזרה אל המערך
######

    # חוזר לנקודת 0
    Fl.seek(0)
    # קריאת כל השורות מהקובץ
    lines = Fl.readlines()

    tesks = []
    for line in lines:
        words  = line.split(', ')
        del words[-1]
        words[0] = int(words[0])
        tesks.append(words)

# הדפסת התוצאה
print(tesks)

