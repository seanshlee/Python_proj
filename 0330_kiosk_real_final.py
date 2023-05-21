#스타벅스 키오스크
class Kiosk :
    def __init__(self):
        self.menu_coffee = {
    '1':{'1.아메리카노': [4500,'hot/ice']},
    '2':{'2.카페라떼': [5000,'hot/ice']}
    }
        self.menu_tea = {
    '1':{'1.자몽허니블랙티':[6400,'hot/ice']},
    '2':{'2.제주유기녹차':[7000,'hot/ice']}
    }
        self.menu_beverage = {
    '1':{'1.망고바나나':[6100,' ']},
    '2':{'2.딸기라떼':[6100,'hot/ice']},
    '3':{'3.밀크티':[6400,'hot/ice']}
    }

    def select_menu(self):
        fp = [] # final price가 저장될 리스트 
        flag=False
        while True :
            category = input("원하시는 메뉴 카테고리 번호를 입력해주세요 (1.커피 / 2.차 / 3.음료 ) : ")
            if category == '1' : #커피 카테고리를 선택한 경우
                menu_list = list(self.menu_coffee.values())
                for menu in menu_list:
                    for k, v in menu.items():
                        print(f"{k} {v[0]}원")
                while True :
                    order = input("원하시는 메뉴의 번호를 입력해주세요 : ")
                    if int(order) not in range(1, len(menu_list)+1) :
                        print("해당 메뉴는 없는 메뉴입니다.")
                        continue
                    else :
                        break
                selected_menu = self.menu_coffee[order] #선택된 메뉴 번호를 키 값으로 하여 메뉴 정보 가져오기

            elif category == '2' : #차 카테고리를 선택한 경우
                menu_list = list(self.menu_tea.values())
                for menu in menu_list:
                    for k, v in menu.items():
                        print(f"{k} {v[0]}원")
                while True :
                    order = input("원하시는 메뉴의 번호를 입력해주세요 : ")
                    if int(order) not in range(1, len(menu_list)+1) :
                        print("해당 메뉴는 없는 메뉴입니다.")
                        continue
                    else :
                        break
                selected_menu = self.menu_tea[order] #선택된 메뉴 번호를 키 값으로 하여 메뉴 정보 가져오기
            
            elif category == '3' : #음료 카테고리를 선택한 경우
                menu_list = list(self.menu_beverage.values())
                for menu in menu_list:
                    for k, v in menu.items():
                        print(f"{k} {v[0]}원")
                while True :
                    order = input("원하시는 메뉴의 번호를 입력해주세요 : ")
                    if int(order) not in range(1, len(menu_list)+1) :
                        print("해당 메뉴는 없는 메뉴입니다.")
                        continue
                    else :
                        break
                selected_menu = self.menu_beverage[order] #선택된 메뉴 번호를 키 값으로 하여 메뉴 정보 가져오기
            else :  
                print("다시 입력해 주시기 바랍니다.")
                continue

            s_menu = selected_menu.keys()
            s_menu2 = list(s_menu)
            s_menu3 = s_menu2[0] #메뉴명만 남긴 것이 s_menu3 이다.

            s_price = selected_menu.values()
            s_price2 = list(s_price)
            s_price3 = (s_price2[0]) #메뉴의 value에 해당하는 리스트가 그대로 출력된 상태가 s_price3 이다. 
            s_price4 = s_price3[0] #리스트에서 가격의 숫자만 추출한 것이 s_price4 이다.

            if s_price3[1] is not ' ' : #Hot/ice 부분이 ' '이면 Hot/ice 구분이 필요 없는 메뉴이다.
                while True :
                    hi = input("1.Hot 2. Ice 중 원하시는 번호를 입력해주세요 : ")
                    if int(hi) not in range(1, 3) :
                        print("다시 입력해주십시오.")
                        continue
                    else :
                        break
            while True :
                    size = input("1.Tall  2.Grande  3.Venti 사이즈 중 원하시는 번호를 입력해주세요 : ")
                    if int(size) not in range(1, 4) :
                        print("다시 입력해주십시오.")
                        continue
                    else :
                        break

            if int(size) == 2 :
                s_price4 = s_price4 + 500
            elif int(size) == 3 :
                s_price4 = s_price4 + 1000

            y = input("원하시는 수량을 입력하세요 : ")
            final_price = int(s_price4)*int(y)

            print(f'선택하신 메뉴는 {s_menu3}이고, 수량은 {y}잔, 가격은 {final_price} 입니다')
            fp.append(final_price)
            ################################################################################
            while True :
                additional = input('추가로 주문하시겠습니까? (1.예  2.아니오) 번호를 입력해주세요 : ')
                if str(additional) == '1' :
                    flag = True
                    break
                elif str(additional) == '2' :
                    flag=False
                    print("결제를 진행해주십시오.")
                    break  
                elif str(additional) not in ['1','2']: 
                    print("'1' 또는 '2' 로 다시 입력해 주시기 바랍니다.")
            if flag : 
                continue
            return sum(fp) #select_menu() 함수의 리턴값은 final_price 값 리스트(fp)를 모두 sum한 값이다.
   
class Run(Kiosk):
    def sb_kiosk(self):
        self.payments = ['1. 신용카드 결제','2. 현금 결제']
        i = 0
        while i < 100 : 
            flag = False
            print("스타벅스에 오신 것을 환영합니다.")
            final = super().select_menu() #상속받은 클래스 Kiosk에서 함수 select_menu의 리턴값 sum(fp)를 final에 저장.
            print(f'{self.payments[0]} {self.payments[1]}')

            while True :
                flag = False
                pd = input("원하시는 결제방식의 번호를 입력해주세요 : ")
                if int(pd) == 1 :
                    print(f"결제금액은 {final}원 입니다. 신용카드를 투입해주세요")
                    flag = True
                    break
                elif int(pd) == 2 :
                    print(f'{final}원을 투입해주세요')
                    flag = True
                    break
                else :
                    print("다시 입력해주세요")
                    continue
            if flag : 
                break #break으로 나와서 만약 flag=True 이면 바깥쪽 반복문까지 탈출하는 코드. 
                      # 1. 신용카드, 2.현금 모두 두 개의 반복문을 다 빠져 나가야 한다. 

starbucks = Run()
starbucks.sb_kiosk()

#수정, 주문취소 기능. 
#클래스 이름 만들 때 보통 첫글자는 대문자로 한다. 
#상수는 다 대문자
#함수는 소문자
