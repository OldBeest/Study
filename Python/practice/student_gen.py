import random
import os

students = []

# generate data set
first_name_list = ['철수', '영희', '민호', '윤아', '지은', '지훈', '민수', '나래', '아라', '현우', '민지', '혜린', '선우', '재형', '보라', '은서']
last_name_list = ['김', '이', '박', '최', '정', '조', '강', '손', '장', '임', '신', '오', '송', '한']
stuNo = 1

# generate student data using random function
def generate_student():
    global stuNo
    for _ in range(100):
        student = {
                'stuNo' : f'{stuNo}',
                'name' : f'{random.choice(last_name_list)}{random.choice(first_name_list)}',
                'kor' : random.randint(70, 100),
                'eng' : random.randint(70, 100),
                'math' : random.randint(70, 100),
        }
        student['total'] = student['kor'] + student['eng'] + student['math']
        student['avg'] = round(student['total']/3, 2)
        student['rank'] = 1
        students.append(student)
        stuNo += 1

# save student data
def save_student_data(students):
    with open(f'{os.getcwd()}\\python\\practice\\data\\studata.txt', 'w', encoding='utf-8') as file:
        #file.write('stuNo,name,kor,eng,math,total,avg,rank\n')
        for student in students:
            file.write(f'{student['stuNo']},{student['name']},{student['kor']},{student['eng']},{student['math']},{student['total']},{student['avg']},{student['rank']}\n')

# give rank in student data
def give_ranking(students):
    rank = 1
    for a_student in students:
        for b_student in students:
            if a_student['total'] < b_student['total']:
                rank += 1
        a_student['rank'] = rank
        rank = 1

# load student data file        
def read_student_data():
    stu_data = []
    with open(f'{os.getcwd()}/python/practice/data/studata.txt', 'r', encoding='utf-8') as file:
        while True:
            text = file.readline().strip()
            if text == '':
                break
            stu_data.append(text.split(','))
        return stu_data
            
         
if __name__ == '__main__':
    generate_student()
    give_ranking(students)
    save_student_data(students)
    stu_data = read_student_data()
    print(stu_data)
    