import operator
# 학생 성적 유형 : 학번, 이름, 국어, 영어, 수학, 과학, 총점, 평균, 등수
students = [] # list
# 샘플 데이터 입력
students.append({'학번' : 'K000', '이름' : '홍길동', '국어' : 100, '영어' : 100, '수학' : 100, '과학' : 100, '총점' : 400, '평균' : 100.0, '등수' : 0})
students.append({'학번' : 'K001', '이름' : '유관순', '국어' : 99, '영어' : 99, '수학' : 99, '과학' : 99, '총점' : 396, '평균' : 98.0, '등수' : 0})
students.append({'학번' : 'K002', '이름' : '이순신', '국어' : 90, '영어' : 90, '수학' : 90, '과학' : 90, '총점' : 360, '평균' : 90.0, '등수' : 0})
students.append({'학번' : 'K003', '이름' : '강감찬', '국어' : 95, '영어' : 95, '수학' : 95, '과학' : 95, '총점' : 380, '평균' : 95.0, '등수' : 0})
students.append({'학번' : 'K004', '이름' : '김구', '국어' : 96, '영어' : 95, '수학' : 94, '과학' : 95, '총점' : 380, '평균' : 95.0, '등수' : 0})

stu_category = ['학번', '이름', '국어점수', '영어점수', '수학점수', '과학점수', '총점', '평균', '등수']
stu_num = 4


# 메인 화면
while 1:
    process_status = False

    print('-'*20)
    print('[학생성적프로그램]')
    print('1. 학생성적입력')
    print('2. 학생성적수정')
    print('3. 학생성적삭제')
    print('4. 학생검색')
    print('5. 학생성적출력')
    print('6. 등수처리')
    print('7. 학생정렬')
    print('0. 프로그램종료')
    print('-'*20)

    menu_num = input('원하는 메뉴 번호를 선택하세요. >>')

    if not menu_num.isdigit() or not (0 <= int(menu_num) < 8): # 입력이 숫자가 아닌경우와 메뉴에 없는 숫자 번호일 경우
        print('입력이 잘못되었습니다. 다시 선택해주세요.')

    else:
        # 학생성적입력
        if menu_num == '1':
            print('학생성적을 입력합니다.')
            while not process_status:
                student = {} # 학생 하나의 정보
                student['학번'] = f'K{stu_num:03d}'
                stu_name = input('학생 이름을 입력해주세요. >>')
                student['이름'] = stu_name
                stu_kor = int(input('국어 점수를 입력해 주세요. >>'))
                student['국어'] = stu_kor
                stu_eng = int(input('영어 점수를 입력해 주세요. >>'))
                student['영어'] = stu_eng
                stu_math = int(input('수학 점수를 입력해 주세요. >>'))
                student['수학'] = stu_math
                stu_sci = int(input('과학 점수를 입력해 주세요. >>'))
                student['과학'] = stu_sci
                stu_total = stu_kor + stu_eng + stu_math + stu_sci
                student['총점'] = stu_total
                stu_avg = round(stu_total / 4, 2)
                student['평균'] = stu_avg
                if len(student) != 8:
                    print('정보가 누락되었습니다. 다시 입력해주세요')
                    continue
                else:
                    print('성적 입력이 완료되었습니다.')
                    students.append(student)
                    stu_num += 1
                    process_status = True                               


        # 학생성적수정
        elif menu_num == '2':
            print('학생성적을 수정합니다.')
            while not process_status:
                search_name = input('수정을 원하는 학생 이름을 입력하세요. >>')
                for student in students:
                    if search_name == student['이름']:
                        print(f'{search_name} 학생을 찾았습니다.')
                        print('-'*15)
                        print('1. 이름')
                        print('2. 국어 점수')
                        print('3. 영어 점수')
                        print('4. 수학 점수')
                        print('5. 과학 점수')
                        print('-'*15)
                        fix_menu_ch = input('수정을 원하는 메뉴 번호를 입력 해 주세요. >>')
                        while not process_status:
                            if fix_menu_ch == '1':
                                print('이름 수정을 진행합니다.')
                                fix_name = input('원하는 이름을 입력하세요. >>')
                                print(f'변경 전: {student['이름']}, 변경 후: {fix_name}')
                                student['이름'] = fix_name
                                print('수정이 완료 되었습니다.')
                                process_status = True
                                
                            elif fix_menu_ch == '2':
                                print('국어 점수 수정을 진행합니다.')
                                fix_kor = int(input('원하는 국어 점수를 입력하세요. >>'))
                                print(f'변경 전: {student['국어']}, 변경 후: {fix_kor}')
                                student['국어'] = fix_kor
                                student['총점'] = student['국어'] + student['영어'] + student['수학'] + student['과학']
                                student['평균'] = round(student['총점'] / 4, 2)
                                print('수정이 완료 되었습니다.')
                                process_status = True
                                
                            elif fix_menu_ch == '3':
                                print('영어 점수 수정을 진행합니다.')
                                fix_eng = int(input('원하는 영어 점수를 입력하세요. >>'))
                                print(f'변경 전: {student['영어']}, 변경 후: {fix_eng}')
                                student['영어'] = fix_eng
                                student['총점'] = student['국어'] + student['영어'] + student['수학'] + student['과학']
                                student['평균'] = round(student['총점'] / 4, 2)
                                print('수정이 완료 되었습니다.')
                                process_status = True
                                
                            elif fix_menu_ch == '4':
                                print('수학 점수 수정을 진행합니다.')
                                fix_math = int(input('원하는 수학 점수를 입력하세요. >>'))
                                print(f'변경 전: {student['수학']}, 변경 후: {fix_math}')
                                student['수학'] = fix_math
                                student['총점'] = student['국어'] + student['영어'] + student['수학'] + student['과학']
                                student['평균'] = round(student['총점'] / 4, 2)
                                print('수정이 완료 되었습니다.')
                                process_status = True
                           
                            elif fix_menu_ch == '5':
                                print('과학 점수 수정을 진행합니다.')
                                fix_sci = int(input('원하는 과학 점수를 입력하세요. >>'))
                                print(f'변경 전: {student['과학']}, 변경 후: {fix_sci}')
                                student['과학'] = fix_sci
                                student['총점'] = student['국어'] + student['영어'] + student['수학'] + student['과학']
                                student['평균'] = round(student['총점'] / 4, 2)
                                print('수정이 완료 되었습니다.')
                                process_status = True
                            
                            else:
                                print("잘못된 입력입니다.")
                                continue
                            
                        
                        # print('학번\t이름\t국어\t영어\t수학\t과학\t총점\t평균\t등수')
                        # print('-'*70)
                        # for data in student:
                        #     print(f'{student[data]}', end='\t')
                        #     process_status = True
                        # print()
                if not process_status:
                    print(f'{search_name} 학생을 찾을 수 없습니다.')
                    process_status = True
                
        
        # 학생성적삭제
        elif menu_num == '3':
            print('학생성적을 삭제합니다.')
            while not process_status:
                search_name = input('수정을 원하는 학생 이름을 입력하세요. >>')
                for index, student in enumerate(students):
                    if search_name == student['이름']:
                        print(f'{search_name} 학생을 찾았습니다.')
                        del_ch = input('학생 정보를 삭제할까요? (y/n) >>')
                        if del_ch == 'y':
                            del(students[index])
                            print(f'{search_name} 학생의 정보가 삭제되었습니다.')
                            process_status = True
                        elif del_ch == 'n':
                            print('취소하셨습니다. 이전으로 돌아갑니다.')
                            process_status = True
                        else:
                            print('잘못 입력하셨습니다. 이전으로 돌아갑니다')
                            process_status = True
                            
                if not process_status:
                    print(f'{search_name} 학생을 찾을 수 없습니다.')
                    process_status = True
            
        # 학생검색
        elif menu_num == '4':
            print('학생 정보를 검색합니다.')
            while not process_status:
                search_name = input('수정을 원하는 학생 이름을 입력하세요. >>')
                for student in students:
                    if search_name == student['이름']:
                        print(f'{search_name} 학생을 찾았습니다.')
                        print('학번\t이름\t국어\t영어\t수학\t과학\t총점\t평균\t등수')
                        print('-'*70)
                        for data in student:
                            print(f'{student[data]}', end='\t')
                            process_status = True
                        print()
                if not process_status:
                    print(f'{search_name} 학생을 찾을 수 없습니다.')
                    process_status = True
                                   
        # 학생성적출력
        elif menu_num == '5':
            print('학생성적을 출력합니다.')
            print('학번\t이름\t국어\t영어\t수학\t과학\t총점\t평균\t등수')
            print('-'*70)
            for student in students:
                for data in student:
                    print(f'{student[data]}', end='\t')
                print()
            
        # 등수처리
        elif menu_num == '6':
            print('등수처리를 진행합니다.')
            # 총점을 기준으로 내림차순 정렬
            # 1. sorted 함수 활용
            students = sorted(students, key=operator.itemgetter('총점'), reverse=True) #총점이 높은 순으로 내림차순
            score_list = [] # 총점을 저장하는 list
            rank = 0
            for student in students:
                print(student['총점'])
                if student['총점'] not in score_list: # 현재 총점이 이전 총점보다 낮은경우 총점 리스트에 값을 추가하고 등수를 1 올림                   
                    rank += 1
                    student['등수'] = rank
                    score_list.append(student['총점'])
                else: # 총점이 같은 경우 등수 변동 없이 등수를 등록함                    
                    student['등수'] = rank
            
                
            
        
        # 학생정렬
        elif menu_num == '7':
            print('학생정렬를 진행합니다.')
            while not process_status:
                sort_menu = ['학번', '이름', '국어', '영어', '수학', '과학', '총점']
                
                print('-'*20)
                print('1. 학번')
                print('2. 이름')
                print('3. 국어')
                print('4. 영어')
                print('5. 수학')
                print('6. 과학')
                print('7. 총점')
                print('-'*20)
                
                sort_ch = input('정렬을 원하는 번호를 선택하세요. >>')
                
                if 0 < int(sort_ch) < 8:
                    print('-'*20)
                    print('1. 오름차순')
                    print('2. 내림차순')                    
                    print('-'*20)
                    sort_opt_ch = input('정렬방식을 선택하세요. >>')
                    if sort_opt_ch == '1':
                        sort_opt = False
                    elif sort_opt_ch == '2':
                        sort_opt = True
                    else:
                        print('입력이 잘못되었습니다. 이전으로 돌아갑니다.')
                        continue  
                    students = sorted(students, key=operator.itemgetter(sort_menu[int(sort_ch)-1]), reverse=sort_opt)
                    print('정렬이 완료되었습니다.')
                    break             

        
        # 프로그램종료
        elif menu_num == '0':
            print("프로그램을 종료합니다.")
            break

        

