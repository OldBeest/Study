import random
import os
import operator

students = []

# -----make student data----- #
class Student:
    
    STU_NO = 1
    def __init__(self, name, kor, eng, math, total=0, avg=0.0, rank=1) -> None: # 번호 입력 순서 수정
        self.stuNo = Student.STU_NO
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.total = self.kor + self.eng + self.math
        self.avg = round(self.total/3, 2)   
        self.rank = rank
        print(self.STU_NO, self.name)  
        Student.STU_NO += 1    

    # when we call object, print student data. return : string
    def __str__(self) -> str:
        return f'{self.stuNo}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}'
        
# generate student data
def data_generate():
    # generate data set
    last_name_list = ['김', '이', '박', '최', '정', '조', '강', '손', '장', '임', '신', '오', '송', '한']
    first_name_list = ['철수', '영희', '민호', '윤아', '지은', '지훈', '민수', '나래', '아라', '현우', '민지', '혜린', '선우', '재형', '보라', '은서']
    
    print('1. 수동입력')
    print('2. 랜덤입력')
    choice = int(input('원하는 메뉴 선택 >>'))
    
    # manual generate
    if choice == 1:
        name = input('이름을 입력하세요. >>')
        kor = int(input('국어 점수를 입력하세요. >>'))
        eng = int(input('영어 점수를 입력하세요. >>'))
        math = int(input('수학 점수를 입력하세요. >>'))
        students.append(Student(name, kor, eng, math))
        
    # auto generate
    elif choice == 2:
        stu_num = int(input('몇 명의 데이터를 만드시겠습니까? >>'))
        for _ in range(stu_num):
            name = random.choice(last_name_list)+random.choice(first_name_list)
            kor = random.randint(70, 100)
            eng = random.randint(70, 100)
            math = random.randint(70, 100)
            students.append(Student(name, kor, eng, math))
            
""" 
# ----- processing functions ----- # 
"""
# ----- print student data -----#
def print_category():
    print('번호\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('-'*70)

def print_student_data():
    for student in students:
        print(student)
        
# ----- file processing ----- #
def save_data():
    # write data
    with open(f'{os.getcwd()}\\data\\stu2.txt', 'w', encoding='utf-8') as f:
        for student in students:
            f.write(f'{student.stuNo},{student.name},{student.kor},{student.eng},{student.math},{student.total},{student.avg},{student.rank}\n')
    print('파일 저장이 완료되었습니다.')
    
def read_data():
    if students == []:
        print('읽기준비 성공')
    # read data from file
        with open(f'{os.getcwd()}\\data\\stu2.txt', 'r', encoding='utf-8') as f:
            while True:
                text = f.readline().strip()
                if text == '':
                    break
                text_list = text.split(',')
                student = Student(text_list[1], int(text_list[2]), int(text_list[3]), int(text_list[4]))
                students.append(student) # 객체로 변환
    else:
        print('저장된 파일을 확인해주세요.')

# -----  handling student data -----#

# ----- find student ----- #
def find_student():
    print('학생검색')
    print('1. 이름으로 검색')
    print('2. 점수로 검색')
    print('0. 돌아가기')
    
    choice = int(input('원하는 메뉴의 번호를 입력하세요. >>'))
    if choice == 1:
        find_status = False
        find_list = []
        search = input('찾고자하는 학생을 입력하세요. >>')
        
        for student in students:
            if search in student.name:
                find_list.append(student)
                find_status = True
        
        if find_status:
            print('검색 결과')
            print_category()
            for student in find_list:
                print(student)
            
        else:
            print('찾는 학생이 없습니다.')
    
    elif choice == 2:
        sub_title = ['', '국어', '영어', '수학', '총점']
        print('1. 국어점수 검색')
        print('2. 영어점수 검색')
        print('3. 수학점수 검색')
        print('4. 총점 검색')
        sub_choice = int(input('원하는 메뉴의 번호를 입력하세요. >>'))
        
        if 1 <= sub_choice <= 4:
            cut_score = int(input(f'{sub_title[sub_choice]}점수의 커트라인을 입력하세요. >>'))
            up_down = int(input('이상이면 1, 이하면 0을 입력해주세요. >>'))
            score_find_list = []
            for student in students:
                student_subject = ['', student.kor, student.eng, student.math, student.total]
                find_up_and_down(score_find_list, student, student_subject[sub_choice], cut_score, up_down)
            print_category()
            for student in score_find_list:
                print(student)
            
def find_up_and_down(score_find_list, student, subject, cut_score, up_down):
    if up_down == 1:
        if subject >= cut_score: 
            score_find_list.append(student)                                    
    elif up_down == 0:
        if subject <= cut_score:   
            score_find_list.append(student)     
                           
# ----- modify student score data ----- #
def modify_student():
    search = input('찾고자하는 학생을 입력하세요. >>')
        
    for student in students:
        if search not in student.name:
            print('찾는 학생이 없습니다.')
            
        else:
            print_category()
            print(student)
            title_list = [['', '국어성적', '영어성적', '수학성적'],
                          ['', student.kor, student.eng, student.math]]
            print('1. 국어성적 수정')
            print('2. 영어성적 수정')
            print('3. 수학성적 수정')
            print('0. 돌아가기')
            
            choice = int(input('원하는 메뉴를 선택하세요. >>'))
            
            if choice == 0:
                break
            elif 1 <= choice <= 3:
                change_value(title_list, choice, student)

def change_value(title_list, choice, student):
    print(f'{title_list[0][choice]} 수정을 선택하였습니다.')
    print(f'현재 점수는 {title_list[1][choice]}입니다.')
    new_score = int(input('새로운 점수를 입력해 주세요. >>'))
    if choice == 1:
        student.kor = new_score
    elif choice == 2:
        student.eng = new_score
    elif choice == 3:
        student.math = new_score
    student.total = student.kor + student.eng + student.math
    student.avg = round(student.total/3, 2)

# ----- delete student data ----- #
def delete_student():
    del_list = []
    search = input('찾고자하는 학생을 입력하세요. >>')
            
    for idx, student in enumerate(students):
        if search not in student.name:
            print('찾는 학생이 없습니다.')
        else:
            del_list.append([student, idx])    
    print_category()
    for student, idx in del_list:
        print(student, f'\t\tindex : {idx}')
    del_idx = int(input('삭제하고싶은 학생의 index를 입력해주세요. >>'))
    decide_delete = input('정말 삭제하시겠습니까? (y)')
    if decide_delete == 'y':
        del(students[del_idx])
    else:
        print('취소하셨습니다.')

# ----- add rank data ----- #
def give_ranking():     
    for student in students:
        rank = 1 # give rank variable
        for compare_student in students.copy():
            if student.total < compare_student.total:
                rank += 1
                student.rank = rank     

# ----- sorting student data ----- #
def sort_data():
    global students
    sort_menu = ['','stuNo', 'name', 'kor', 'eng', 'math', 'total']
    print('1. 학번')
    print('2. 이름')
    print('3. 국어점수')
    print('4. 영어점수')
    print('5. 수학점수')
    print('6. 총점')
    print('0. 돌아가기')
    
    choice = int(input('정렬하고 싶은 데이터 번호를 선택 해주세요. >>'))
    
    if choice == 0:
        print('이전 화면으로 갑니다.') 
    elif 1 <= choice <= 6:
        print('1. 오름차순')
        print('2. 내림차순')
        print('0. 취소')
        
        sort_method = int(input('정렬 방식을 선택하세요. >>'))
        if sort_menu == 0:
            print('취소합니다.')
        elif sort_method == 1:
            students = sorted(students, key=operator.attrgetter(sort_menu[choice]), reverse=False)
        elif sort_method == 2:
            students = sorted(students, key=operator.attrgetter(sort_menu[choice]), reverse=True)
                 
# ----- main screen ----- #    
def main_window():        
    while 1:
        print('[ 학생성적처리 프로그램 ]')
        print('1. 학생성적입력')
        print('2. 학생성적전체출력')
        print('3. 학생검색')
        print('4. 학생성적수정')
        print('5. 학생성적삭제')
        print('6. 등수처리')
        print('7. 학생정렬')
        print('8. 파일 읽어오기')
        print('9. 파일로 저장하기')
        print('0. 프로그램종료')
        
        choice = int(input('원하는 메뉴의 번호를 입력하세요. >>'))
        
        if choice == 0:
            print('프로그램을 종료합니다.')
            break
        
        elif choice == 1:
            data_generate()
            
        elif choice == 2:
            print_category()
            print_student_data()
            
        elif choice == 3:
            find_student()
        
        elif choice == 4:
            modify_student()
        
        elif choice == 5:
            delete_student()
        
        elif choice == 6:
            give_ranking()
   
        elif choice == 7:
            sort_data()
        
        elif choice == 8:
            read_data()
            
        elif choice == 9:
            save_data()
            
        else:       
            print('잘못된 입력입니다.')
            continue
    
"""  
#----- main function -----#
"""
if __name__ == '__main__':
    main_window()