import random

shape_list = ['spade', 'diamond', 'heart', 'clover']
number_list = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

card_deck = [0 for _ in range(len(shape_list)*len(number_list))]
check_first_deck = True
regame_ch = ''
# 0. main screen
def main_screen():
    while 1:
        print('[ 카드뽑기게임 ]')
        print('1. 카드 덱 생성')
        print('2. 카드 덱 섞기')
        print('3. 카드 뽑기')
        print('4. 카드 확인')
        print('0. 종료')
        print('-'*30)
        
        menu_choice = int(input('원하는 메뉴를 선택하세요. >>'))
        
        print(menu_choice)
        if menu_choice == 1:
            make_deck(card_deck)
        elif menu_choice == 2:
            shuffle_deck(card_deck)
        elif menu_choice == 3:
            global check_first_deck # global
            if check_first_deck:
                draw, rest = draw_card(card_deck)
                check_first_deck = False
            else:
                draw, rest = draw_card(rest)
            check_regame(draw, rest)
        elif menu_choice == 4:
            show_card(draw, rest)
        elif menu_choice == 0:
            break
        
        #cardgame_module.regame(rest)
    
    
# 1. make card deck
def make_deck(card_deck):
    idx = 0
    for shape in shape_list:
        for num in number_list:
            card_deck[idx] = {'shape' : shape, 'number' : num}
            idx += 1

# 2. shuffle card deck

def shuffle_deck(card_deck):
    random.shuffle(card_deck)

# 3. draw some card
def draw_card(card_deck):
    draw_count = int(input('뽑을 카드 개수 >>'))
    draw = card_deck[:draw_count]
    rest = card_deck[draw_count:]
    
    return draw, rest

# 4. show drawn card and rest card
def show_card(draw, rest):
    print('뽑은 카드 : ', draw)    
    print('남은 카드 : ', rest)
    
# 5. when card deck is empty, remake new card deck 
def check_regame(draw, rest):
    global check_first_deck # global
    if len(rest) == 0:
        regame_ch = input('카드가 모두 소진 되었습니다. 새 카드 덱을 만드시겠습니까? >>')
        print('마지막 뽑은 카드', draw)
        if regame_ch == 'y':
            make_deck(card_deck)
            check_first_deck = True
    else:
        pass
