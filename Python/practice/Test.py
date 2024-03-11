students = []
# 테스트 데이터
students = [{'stuNo': 'S001', 'name': '홍길동', 'kor': 100, 'eng': 99, 'math': 100, 'total': 299, 'avg': 99.67}, 
            {'stuNo': 'S002', 'name': '유관순', 'kor': 98, 'eng': 92, 'math': 97, 'total': 287, 'avg': 95.67}, 
            {'stuNo': 'S003', 'name': '이순신', 'kor': 95, 'eng': 95, 'math': 95, 'total': 285, 'avg': 95.0}, 
            {'stuNo': 'S004', 'name': '강감찬', 'kor': 93, 'eng': 92, 'math': 97, 'total': 282, 'avg': 94.0}, 
            {'stuNo': 'S005', 'name': '김구', 'kor': 88, 'eng': 99, 'math': 93, 'total': 280, 'avg': 93.33},
            {'stuNo': 'S006', 'name': '김유신', 'kor': 93, 'eng': 99, 'math': 88, 'total': 280, 'avg': 93.33}]

category = ['stuNo', 'name', 'kor', 'eng', 'math', 'total', 'avg', 'rank']
category_korean = {'stuNo' : '학번', 'name' : '이름', 'kor' : '국어', 'eng' : '영어', 'math' : '수학', 'total' : '총점', 'avg' : '평균', 'rank' : '등수'}
menu = ['종료', '입력', '전체', '검색', '수정', '등수', '삭제', '정렬']
stu_no = len(students) + 1

# 메인 화면
def main_window():
    while 1:
        print('-'*40)
        print('[학생성적프로그램]')
        print('-'*40)
        print('1. 학생성적입력')
        print('2. 학생성적전체출력')
        print('3. 학생검색')
        print('4. 학생수정')
        print('5. 등수처리')
        print('6. 학생삭제')
        print('7. 학생정렬')
        print('0. 프로그램 종료')
        print('-'*40)
        choice = input('원하는 번호를 입력하세요:  ')
        print('-'*40)
        if not choice.isdigit():
            print('숫자만 입력 가능합니다.')
            continue 
        choice = int(choice)
        
        if choice in range(len(menu)):
            print(f'{menu[choice]} 선택하셨습니다.')
            if choice == 1:
                student_data()
                pass
            elif choice == 2:
                print_data()
                pass
            elif choice == 3:
                find_student()
                pass
            elif choice == 4:
                modify_data()
                pass
            elif choice == 5:
                ranking()
                pass
            elif choice == 6:
                delete_data()
                pass
            elif choice == 7:
                sort_data()
            elif choice == 0:
                print('프로그램을 종료합니다.')
                break
                        
        else:
            print('잘못된 입력입니다.')
        
        
# 1-1. 단순 입력        
def input_data():
    input_data = input('입력을 하세요. >>')
    if input_data.isdigit():
        input_data = int(input_data) 
    return input_data
# 1-1. 학생정보 입력
def student_data():
    student = {}
    student['stuNo'] = 'S'+ f'{stu_no:03d}'
    for key in category[1:5]:
        print(f'{category_korean[key]}', end=' ')
        student[key] = input_data()     
    student['total'], student['avg'] = total_avg(student['kor'], student['eng'], student['math'])
    students.append(student)
# 1-2. 총점 평균 계산
def total_avg(kor, eng, math):
    total = kor + eng + math
    avg = round(total / 3, 2)  
    return total, avg
        
# 2. 전체출력
def print_data():
    print('[ 학생성적전체출력 ]')
    print('-'*65)
    print('학번\t이름\t국어\t영어\t수학\t총점\t평균\t등수')
    print('-'*65)
    for s_dic in students:
        for s_key in s_dic:
            print(s_dic[s_key], end='\t')
        print()
    print('-'*65)
    
# 3. 검색
def find_student():
    find_status = False
    print('학생이름을', end = ' ')
    name = input_data()
    for index, student in enumerate(students):
        if name == student['name']:
            find_status = True
            print(f'{name}을 찾았습니다.')
        
            return find_status, name, index
    
    if not find_status:    
        print(f'{name}을 찾지 못했습니다.')
        
        return find_status, name, None  
     
# 4. 수정 
def modify_data():
    _, name, stu_idx = find_student()
    for index, key in enumerate(category[:5]):
        print(f'{index+1}. {category_korean[key]}', end=' ')
    print()
    print('-'*50)
    mod_choice = input_data()
    if mod_choice == 1:
        students[stu_idx][category[mod_choice-1]] = f'S{input_data():03d}'   
    elif mod_choice == 2:    
        students[stu_idx][category[mod_choice-1]] = input_data()
    elif 3 <= mod_choice <= 5: 
        students[stu_idx][category[mod_choice-1]] = input_data()
        students[stu_idx]['total'], students[stu_idx]['avg'] = total_avg(students[stu_idx]['kor'], students[stu_idx]['eng'], students[stu_idx]['math'] )

# 5. 등수
def ranking():
    for idx, s_dic in enumerate(students):
        rank_cnt = 1 # 등수처리변수
        for i_dic in students:
            if s_dic['total'] < i_dic['total']: # 두 수를 비교
                rank_cnt += 1 # 현재 학생의 합계보다 크면 1증가
        #print(s_dic)
        s_dic['rank'] = rank_cnt

# 6. 삭제
def delete_data():
    _, del_name, index = find_student()
    del[students[index]]
        
# 7. 정렬    
def sort_data():
    global students
    import operator
    category_some = category[:6]
    print('-'*60)
    print('1. 학번 2. 이름 3. 국어 4. 영어 5. 수학 6. 총점')
    sort_ch = input_data()
    print('1. 오름차순 2. 내림차순')
    sort_method = input_data()
    if sort_method == 1:
            sort_method = False
    elif sort_method == 2:
            sort_method = True
    students = sorted(students, key=operator.itemgetter(category_some[sort_ch-1]), reverse=sort_method)
        
    return students
        
# 메인함수
if __name__ == '__main__':
    main_window()