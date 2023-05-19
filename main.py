import tkinter as tk
import csv
import os


def get_grade(score):
    if score >= 92:
        return 'A'
    elif score >= 85:
        return 'B'
    elif score >= 77:
        return 'C'
    elif score >= 69:
        return 'D'
    else:
        return 'F'


def add_student():
    global id_entry, name_entry, score_entry, info_label

    id = id_entry.get()
    name = name_entry.get()
    score = score_entry.get()

    if not id.isdigit():
        info_label['text'] = "Numerical ID Required"
        return

    if not score.isdigit():
        info_label['text'] = "Numerical Score Required"
        return

    score = int(score)
    grade = get_grade(score)

    if not os.path.isfile('students.csv'):
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Score", "Grade"])

    updated = False
    temp_data = []
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                row[1], row[2], row[3] = name, score, grade
                updated = True
            temp_data.append(row)
    if not updated:
        with open('students.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([id, name, score, grade])

    info_label['text'] = "Student updated successfully" if updated else "Student added successfully"

    id_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    score_entry.delete(0, 'end')


def search_student():
    global id_entry, name_entry, score_entry, info_label

    id = id_entry.get()

    if not id.isdigit():
        info_label['text'] = "Numerical ID Required"
        return

    student_found = False
    with open('students.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                info_label['text'] = f"{row[1]} has {row[2]}% with a(n) {row[3]}"
                student_found = True
                break

    if not student_found:
        info_label['text'] = "Student not found"

    id_entry.delete(0, 'end')
    name_entry.delete(0, 'end')
    score_entry.delete(0, 'end')


def main():
    global id_entry, name_entry, score_entry, info_label

    root = tk.Tk()
    root.geometry("300x300")
    root.title("Student Scoring")

    id_label = tk.Label(root, text="ID:", font=("Arial", 14), bg="lightblue")
    id_label.pack()

    id_entry = tk.Entry(root, font=("Arial", 14))
    id_entry.pack()

    name_label = tk.Label(root, text="Name:", font=("Arial", 14), bg="lightblue")
    name_label.pack()

    name_entry = tk.Entry(root, font=("Arial", 14))
    name_entry.pack()

    score_label = tk.Label(root, text="Score:", font=("Arial", 14), bg="lightblue")
    score_label.pack()

    score_entry = tk.Entry(root, font=("Arial", 14))
    score_entry.pack()

    add_button = tk.Button(root, text="Add Student", command=add_student, font=("Arial", 12))
    add_button.pack()

    search_button = tk.Button(root, text="Search Student", command=search_student, font=("Arial", 12))
    search_button.pack()

    info_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgreen")
    info_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
