#스타벅스 키오스크
import re
class Kiosk :
    def __init__(self):
        self.all_menu = ['아메리카노','카페라떼','자몽허니블랙티','제주유기녹차','망고바나나','딸기라떼','밀크티']
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
        fp = []
        m_list = [] #메뉴
        m_show_list = [] #보여주기용 메뉴
        flag=False
        i=1
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
            
            elif category == '2' : #차(tea) 카테고리를 선택한 경우
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
            # else :  
            #     print("다시 입력해 주시기 바랍니다.")
            #     continue

            s_menu = selected_menu.keys()
            s_menu2 = list(s_menu)
            s_menu3 = s_menu2[0] #메뉴명만 남긴 것이 s_menu3 이다.
            s_menu4 = re.sub(r"[^가-힣]","",s_menu3)

            s_price = selected_menu.values()
            s_price2 = list(s_price)
            s_price3 = (s_price2[0]) #메뉴의 value에 해당하는 리스트가 그대로 출력된 상태가 s_price3 이다. 
            s_price4 = s_price3[0] #리스트에서 가격의 숫자만 추출한 것이 s_price4 이다.

            if s_price3[1] != ' ' : #Hot/ice 부분이 ' '이면 Hot/ice 구분이 필요 없는 메뉴이다.
                while True :
                    hi = input("1.Hot 2. Ice 중 원하시는 번호를 입력해주세요 : ")
                    if int(hi) not in range(1, 3) :
                        print("다시 입력해주십시오.")
                        continue
                    elif hi == '1':
                        t = 'Hot'
                        break
                    elif hi == '2':
                        t = 'Ice'
                        break
                # if flag:
                #     break
            elif s_price3[1] == ' ' : t= ''
            while True :
                    size = input("1.Tall  2.Grande  3.Venti 사이즈 중 원하시는 번호를 입력해주세요 : ")
                    if int(size) not in range(1, 4) :
                        print("다시 입력해주십시오.")
                        continue
                    else :
                        break
            if int(size) == 1 :
                s = "Tall"
            elif int(size) == 2 :
                s_price4 = s_price4 + 500
                s = "Grande"
            elif int(size) == 3 :
                s_price4 = s_price4 + 1000
                s = "Venti"

            y = input("원하시는 수량을 입력하세요 : ")
            final_price = int(s_price4)*int(y)

            # 메뉴명 / 
            ordered_menu = [s_menu4,t,s,final_price] #0,1,2,3
            m_list.append(ordered_menu)

            self.m_list = m_list

            show_list = f'{i}'+'.'+''+t+' '+s_menu4+' '+s+' '+str(y)+'개'+' '+':'+' '+str(final_price)+'원'
            m_show_list.append(show_list) #name+H/I

            self.m_show_list = m_show_list

            fp.append(final_price)
            self.final = sum(fp)
            ################################################################################
            while True :
                additional = input('추가주문 하시겠습니까? 번호를 입력해주십시오(1.예  2.아니오) : ')
                if str(additional) == '1' :
                    flag = True
                    i+=1
                    break
                elif str(additional) == '2' :
                    print('*'*40)
                    print(f"최종 주문내역은\n{[a for a in m_show_list]}이고,\n총 가격은 {sum(fp)} 원입니다.주문내역을 변경하시겠습니까?\n 1.예  2.아니오\n번호를 입력해주십시오 : ")
                    print('*'*40)
                    flag = False
                    break  
                elif str(additional) not in ['1','2']: 
                    print("'1' 또는 '2' 로 다시 입력해 주시기 바랍니다.")
            if flag : 
                continue
            else :
                break

k = Kiosk()
k.select_menu()
mb = []
for k in k.menu_beverage.values() :
    pp1 = list(k)
    pp2 = pp1[0]
    pp3 = re.sub(r"[^가-힣]","",pp2)
    mb.append(pp3)
mb
k.menu_beverage.values()


s_menu = selected_menu.keys()
s_menu2 = list(s_menu)
s_menu3 = s_menu2[0] #메뉴명만 남긴 것이 s_menu3 이다.
s_menu4 = re.sub(r"[^가-힣]","",s_menu3)



sb = k.m_list
sb[0]
re = 2
k.m_list[re-1]

#메뉴 리스트 뽑기(key로)
mb =[]
k.menu_beverage
k.m_list
kl = list(k.menu_beverage.values())
kl
klk = [a.keys for a in kl]
klk

for k in k.menu_beverage.keys() :
    print(k)
    # k2 = re.sub(r"[^가-힣]","",str(k))
    # mb.append(k2)
mb

s_menu4 = re.sub(r"[^가-힣]","",s_menu3)


list(list(k.menu_coffee.values())[0].keys())

class Run(Kiosk):
    def sb_kiosk(self):
        print(self.m_show_list)
        re = input('변경하실 주문내역 번호를 입력해주세요. : ')
        print(f'변경하실 주문 내역은\n{self.m_list[re-1]} 입니다.')
        print('*'*40)
        print('메뉴판 참고')
        print(self.menu_coffee, self.menu_tea, self.menu_beverage)
        print('*'*40)

        # fix = input('1. 메뉴변경 2. 수량 변경 3. 사이즈 변경\n수정하실 항목 번호를 입력해주세요 : ')
        #메뉴 수정
        # mc = input(f'{self.m_list[re-1][0]}를 변경하시겠습니까?\n1.예  2.아니오 : ')
        # if mc == '1'
        while True :
            changed_menu = input("변경하실 메뉴명을 직접 입력해주세요 : ")
            changed_temp = input("변경사항을 입력해주세요. (Hot 또는 Ice로 입력) : ")
            changed_quan = input("변경하실 수량을 입력해주세요. (숫자만 입력) : ")
            changed_size = input("변경하실 size를 입력해주세요. (Tall / Grande / Venti 중 입력) : ")

            #메뉴변경
            if changed_menu not in self.all_menu :
                print("다시 입력해주세요")
                continue 
            elif changed_menu in self.all_menu :
                self.m_list[re-1][0] = changed_menu
            
            #냉온 변경
            if changed_temp not in ['Hot', 'Ice'] :
                print("다시 입력해주세요")
                continue 
            elif changed_menu in self.all_menu :
                self.m_list[re-1][1] = changed_temp
            
            #
            self.m_list[re-1][0] = changed_menu
            if self.m_list[re-1][1] != '' :
                self.m_list[re-1][1] = input("변경사항을 입력해주세요 : ")
            else :
                pass
            self.m_list[re-1][2] = input("변경하실 size를 입력해주세요 : ")


        if fix == '1':
            print(self.menu_coffee,self.menu_tea,self.menu_beverage)
            new_menu = input()

        #수량 수정
        if fix == '2':

        #사이즈 수정
        if fix == '3':


        print('')
        print(self.menu_coffee,self.menu_tea,self.menu_beverage)




        self.payments = ['1. 신용카드 결제','2. 현금 결제']
        i = 0
        while i < 100 : 
            flag = False
            print("스타벅스에 오신 것을 환영합니다.")
            # final
            # final = super().select_menu() #상속받은 클래스 Kiosk에서 함수 select_menu의 리턴값 sum(fp)를 final에 저장.
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
