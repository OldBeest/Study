import random
import os

class Student:
    
    # generate data set
    FIRST_NAME_LIST = ['철수', '영희', '민호', '윤아', '지은', '지훈', '민수', '나래', '아라', '현우', '민지', '혜린', '선우', '재형', '보라', '은서']
    LAST_NAME_LIST = ['김', '이', '박', '최', '정', '조', '강', '손', '장', '임', '신', '오', '송', '한']
    STU_NO = 1

    def __init__(self) -> None:
        
        # self.data = {
        #         'stuNo' : 0,
        #         'name' : '',
        #         'kor' : 0,
        #         'eng' : 0,
        #         'math' : 0,
        # }
        
        # generate student data using random function
        self.data = {
                'stuNo' : f'{Student.STU_NO}',
                'name' : f'{random.choice(Student.LAST_NAME_LIST)}{random.choice(Student.FIRST_NAME_LIST)}',
                'kor' : random.randint(70, 100),
                'eng' : random.randint(70, 100),
                'math' : random.randint(70, 100),
        }
        self.data['total'] = self.data['kor'] + self.data['eng'] + self.data['math']
        self.data['avg'] = round(self.data['total']/3, 2)
        self.data['rank'] = 1
        Student.STU_NO += 1
        
    # def generate_student(self):       
    #     self.data = {
    #             'stuNo' : f'{Student.STU_NO}',
    #             'name' : f'{random.choice(Student.LAST_NAME_LIST)}{random.choice(Student.FIRST_NAME_LIST)}',
    #             'kor' : random.randint(70, 100),
    #             'eng' : random.randint(70, 100),
    #             'math' : random.randint(70, 100),
    #     }
    #     self.data['total'] = self.data['kor'] + self.data['eng'] + self.data['math']
    #     self.data['avg'] = round(self.data['total']/3, 2)
    #     self.data['rank'] = 1
    #     Student.STU_NO += 1

    # save student data
    def save_student_data(self, students):
        with open(f'{os.getcwd()}\\python\\practice\\data\\studata.txt', 'w', encoding='utf-8') as file:
            #file.write('stuNo,name,kor,eng,math,total,avg,rank\n')
            for student in students:
                file.write(f'{student.data['stuNo']},{student.data['name']},{student.data['kor']},{student.data['eng']},{student.data['math']},{student.data['total']},{student.data['avg']},{student.data['rank']}\n')

    # give rank in student data
    def give_ranking(self, students):
        rank = 1
        for a_student in students:
            for b_student in students:
                if a_student.data['total'] < b_student.data['total']:
                    rank += 1
            a_student.data['rank'] = rank
            rank = 1

    # load student data file        
    def read_student_data(self):
        stu_data = []
        with open(f'{os.getcwd()}/python/practice/data/studata.txt', 'r', encoding='utf-8') as file:
            while True:
                text = file.readline().strip()
                if text == '':
                    break
                stu_data.append(text.split(','))
            return stu_data
    
    # print student data
    def print_upper(self):
        print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
        print('-'*70)
    
    def print_student_data(self, students):
        for student in students:
            print(f'{student.data['stuNo']}\t{student.data['name']}\t{student.data['kor']}\t{student.data['eng']}\t{student.data['math']}\t{student.data['total']}\t{student.data['avg']}\t{student.data['rank']}')
        
if __name__ == '__main__':
    students = [Student() for i in range(100)]
    #print(students[0].data)
    stu1 = Student()
    stu1.save_student_data(students)
    stu2 = stu1.read_student_data()
    print(stu2)
    stu1.give_ranking(students)
    stu1.print_upper()
    stu1.print_student_data(students)
    
# example result
""" 
번호    이름    국어    영어    수학    총점    평균    등수
----------------------------------------------------------------------
1       손아라  93      93      100     286     95.33   2
2       최민호  95      79      81      255     85.0    41
3       송지훈  93      82      99      274     91.33   11
4       임선우  72      72      79      223     74.33   99
5       박은서  96      82      93      271     90.33   15
6       김현우  97      79      70      246     82.0    63
7       최철수  92      73      71      236     78.67   87
8       장혜린  71      79      80      230     76.67   92
9       조나래  86      90      73      249     83.0    55
10      박윤아  79      100     71      250     83.33   52
"""