class Kiosk :
    ordered_menu = [] #주문한 메뉴 저장
    ordered_price = [] #주문한 메뉴의 가격 저장
    size_list = [] #주문한 사이즈 저장
    quantity_list = [] #주문한 수량 저장
    fhtg_list =[] #take-out 여부 저장
    order_list =[] #최종 주문 내역 리스트
    fp = [] #final_price
    j = 1
    flag = False

    def __init__(self):
        self.coffee = {'c1':['c1. 아메리카노',4500,'Hot/Ice'],
        'c2':['c2. 카페라떼',5000,'Hot/Ice']}
        self.tea = {'t1':['t1. 제주유기녹차',6400,'Hot/Ice'],
        't2':['t2. 자몽허니블랙티',6400,'Hot/Ice']}
        self.beverage = {'b1':['b1. 망고바나나',6100,' '],
        'b2':['b2. 쿨라임피지오',6100,' ']}
        self.all_menu_keys = list(self.coffee.keys())+list(self.tea.keys())+list(self.beverage.keys())  
                                                                         #메뉴타입의 경우 c(커피),t(차),b(음료)
    def add_menu(self,menu_type,menu_name,price,temparature='Hot/Ice') : #아이스만 있는 경우 temparature에 공백 입력
        self.price = price
        self.menu_type = menu_type
        self.menu = menu_name
        self.temparature = temparature
        
        if self.menu_type.lower() == 'c' :
            self.menu_name = f'c{len(self.coffee)+1}. '+self.menu
            self.coffee.setdefault(f'c{len(self.coffee)+1}',[f'{self.menu_name}',f'{self.price}',f'{self.temparature}'])
        elif self.menu_type.lower() == 't' :
            self.menu_name = f't{len(self.tea)+1}. '+self.menu
            self.tea.setdefault(f't{len(self.tea)+1}',[f'{self.menu_name}',f'{self.price}',f'{self.temparature}'])
        elif self.menu_type.lower() == 'b' :
            self.menu_name = f'b{len(self.beverage)+1}. '+self.menu
            self.beverage.setdefault(f'b{len(self.beverage)+1}',[f'{self.menu_name}',f'{self.price}',f'{self.temparature}'])
     
    def show_menu(self):
        print('\n*****Coffee*****\n')
        for i in range(0, len(self.coffee)):
            tmp = list(self.coffee.values())[i]
            print(f'{tmp[0]} {tmp[1]}원\n')
    
        print('*****Tea*****\n')
        for i in range(0, len(self.tea)):
            tmp = list(self.tea.values())[i]
            print(f'{tmp[0]} {tmp[1]}원\n')
    
        print('*****Beverage*****\n')
        for i in range(0, len(self.beverage)):
            tmp = list(self.beverage.values())[i]
            print(f'{tmp[0]} {tmp[1]}원\n')

    def order_edit(self) :
        while True :
            self.edit_order_num = input("변경하실 주문번호를 입력해주세요. (숫자만 입력) : ")
            if int(self.edit_order_num) == AssertionError :
                print("다시 입력해주세요.")
                continue
            elif int(self.edit_order_num) not in range(len(self.order_list)+1):
                print("없는 주문 번호입니다. 다시 입력해주세요")
                continue
            else :
                break
        while True :
            self.edit_order = input("1.메뉴 변경  2.Hot/Ice 변경  3.사이즈 변경  4.수량 변경  5. 매장식사/Take-out 변경  6.주문 삭제  7. 수정사항없음\n번호를 입력해주세요(해당 번호 숫자만 입력) : ")
            if self.edit_order == '1' : #메뉴 변경
                self.order_list = self.order_list.remove(self.order_list[int(self.edit_order_num)-1])
                self.order()
                break
            elif self.edit_order == '2' : #온도 변경
                if self.order_list[int(self.edit_order_num)-1][1] not in ['Hot','Ice'] :
                    print("Ice only 메뉴입니다.\n")
                    continue
                elif self.order_list[int(self.edit_order_num)-1][1] in ['Hot','Ice'] :
                    tc = input('\n1. Hot  2. Ice 중 번호를 입력해주세요 : ')
                    if tc == '1':
                        self.order_list[int(self.edit_order_num)-1][1] == 'Hot'
                        flag = True
                        break
                    elif tc == '2':
                        self.order_list[int(self.edit_order_num)-1][1] == 'Ice'
                        flag = True
                        break
                    else :
                        print("1 또는 2로 다시 입력해주십시오.")
                        continue
                if flag :
                    break
            elif self.edit_order == '3' : #사이즈 변경
                while True :
                    sc = input('\n1.Tall  2.Grande  3.Venti 사이즈 중 원하시는 번호를 입력해주세요 : ')
                    if int(sc) not in range(1, 4) :
                        print("다시 입력해주십시오.")
                        continue
                    elif int(sc) == 1 :
                        self.order_list[int(self.edit_order_num)-1][2] =  "Tall"
                        flag = True
                        break
                    elif int(sc) == 2 :
                        self.order_list[int(self.edit_order_num)-1][2] = "Grande"
                        flag = True
                        break
                    elif int(sc) == 3 :
                        self.order_list[int(self.edit_order_num)-1][2] = "Venti"
                        flag = True
                        break
                if flag :
                    break
            elif self.edit_order == '4' : #수량 변경
                while True :
                    qc = input('변경하실 수량을 입력해주세요. (숫자만 입력) : ')
                    if int(qc) == AssertionError :
                        print("다시 입력해주세요. (숫자만 입력해주세요) : ")
                        continue
                    else :
                        self.order_list[int(self.edit_order_num)-1][3] = int(qc)
                        flag = True
                        break
                if flag :
                    break
            elif self.edit_order == '5' : #매장식사,take/out변경
                while True :
                    pc = input('번호를 입력해주세요\n1. 매장 식사  2. Take-Out \n: ')
                    if pc == '1':
                        self.order_list[int(self.edit_order_num)-1][5] = '매장 식사'
                        flag = True
                        break
                    elif pc == '2':
                        self.order_list[int(self.edit_order_num)-1][5] = 'Take-Out'
                        flag = True
                        break
                    else :
                        print("1 또는 2로 다시 입력해주십시오.")
                        continue
                if flag :
                    break
            elif self.edit_order == '6' : #주문 삭제
                del self.order_list[int(self.edit_order_num)-1]
                if len(self.order_list) == 0 :
                    print("모든 메뉴가 삭제되었습니다.\n 다시 주문해주세요.")
                    self.order()
                else :
                    break
            elif self.edit_order == '7' : #수정사항없음
                break
        #주문내역 수정 완료하기
        oe2 = input("주문내역 수정을 완료하시겠습니까?\n1.예  2.아니오\n:")
        while True :
            if oe2 == '1' :
                self.fp.clear()
                self.fp.append(self.order_list[i][4]*int(self.order_list[i][3]))
                break
            elif oe2 == '2' :
                print("주문 내역은 아래와 같습니다.")
                for i in range(len(self.order_list)):
                    print(f'{i+1}번 주문 : {self.order_list[i][0]}{self.order_list[i][1]} {self.order_list[i][2]} {self.order_list[i][3]}개 {self.order_list[i][4]*int(self.order_list[i][3])}원, {self.order_list[i][5]}\n')
                self.order_edit()
                break
            else :
                print('다시 입력해주세요')
                continue

        print("주문 내역은 아래와 같습니다.")
        for i in range(len(self.order_list)):
            print(f'{i+1}번 주문 : {self.order_list[i][0]}{self.order_list[i][1]} {self.order_list[i][2]} {self.order_list[i][3]}개 {self.order_list[i][4]*int(self.order_list[i][3])}원, {self.order_list[i][5]}\n')
            self.fp.clear()
            self.fp.append(self.order_list[i][4]*int(self.order_list[i][3]))
        self.payments()

    def payments(self):
        while True :
            pd = input("1. 신용카드 결제  2. 현금 결제\n원하시는 결제방식의 번호를 입력해주세요 : ")
            if int(pd) == 1 :
                print(f"결제금액은 {sum(self.fp)}원 입니다. 신용카드를 투입해주세요")
                break
            elif int(pd) == 2 :
                print(f'{sum(self.fp)}원을 투입해주세요')
                break
            else :
                print("다시 입력해주세요")
                continue
        print("결제가 완료되었습니다. 이용해주셔서 감사합니다.")
        
    def order(self):
        self.show_menu() #메뉴 보여주기
    ####### 메뉴 선택하기
        while True :
            self.category = input("원하시는 메뉴 번호(ex.t1, c1, b1)를 입력해주세요 : ")
            if  self.category[0].lower() == 'c' :
                self.selected_menu = self.coffee[f'{self.category}']

                self.ordered_menu.append(self.selected_menu[0])
                self.ordered_price.append(self.selected_menu[1])
                break
            elif self.category[0].lower() == 't' :
                self.selected_menu = self.tea[f'{self.category}']

                self.ordered_menu.append(self.selected_menu[0])
                self.ordered_price.append(self.selected_menu[1])
                break
            elif self.category[0].lower() == 'b' :
                self.selected_menu = self.beverage[f'{self.category}']

                self.ordered_menu.append(self.selected_menu[0])
                self.ordered_price.append(self.selected_menu[1])
                break
            elif self.category not in self.all_menu_keys :
                print("다시 입력해주십시오. (입력예시 : t1, c1, b1)\n")
                continue

    ######## 온도 선택(Hot/Ice)하기
        while True :
            if self.selected_menu[2] != ' ':
                t = input('\n1. Hot  2. Ice 중 번호를 입력해주세요 : ')
                if t == '1' :
                    self.temp = 'Hot'
                    break
                elif t == '2':
                    self.temp ='Ice'
                    break
                elif t not in range(1,3):
                    print("1 또는 2로 다시 입력해주십시오.")
                    continue
            else :
                self.temp=''
                break

    ######### Size 선택하기
        while True :
            size = input("\n1.Tall  2.Grande  3.Venti 사이즈 중 원하시는 번호를 입력해주세요 : ")
            if int(size) not in range(1, 4) :
                print("다시 입력해주십시오.")
                continue
            else :
                break
        if int(size) == 1 :
            self.size = "Tall"
            self.size_list.append(self.size)
        elif int(size) == 2 :
            self.size = "Grande"
            self.size_list.append(self.size)
        elif int(size) == 3 :
            self.size = "Venti"
            self.size_list.append(self.size)

    ######### 수량 선택하기
        self.quantity = input("\n원하시는 수량을 입력해주세요. (숫자만 입력) : ")
        while True :
            if int(self.quantity) == AssertionError :
                print("다시 입력해주세요. (숫자만 입력해주세요) : ")
                continue
            else :
                self.quantity_list.append(self.quantity)
                break
        t = input("\n원하시는 번호를 입력해주세요\n1. 매장 식사  2. Take-Out \n:")
        while True :
            if t == '1' :
                self.fhtg = '매장 식사'
                self.fhtg_list.append(self.fhtg)
                break
            elif t == '2':
                self.fhtg = 'Take-out'
                self.fhtg_list.append(self.fhtg)
                break
            elif t not in range(1,3):
                print("1 또는 2로 다시 입력해주십시오.")
                continue
        ######################################################### 이 부분에서 j 사용
        print(f'주문하신 메뉴는 {self.ordered_menu[self.j-1]} {self.temp} {self.size} {self.quantity}개이고, 가격은 {self.ordered_price[self.j-1]*int(self.quantity)}원, {self.fhtg}입니다.')
        self.order_list.append([self.ordered_menu[self.j-1],self.temp,self.size,self.quantity,self.ordered_price[self.j-1],self.fhtg])        

        oa = input("\n추가주문 하시겠습니까?\n1.예  2.아니오\n:")
        while True :
            if oa == '1' :
                self.j += 1
                self.order() ######### 추가 주문할 경우 order 함수 재실행
            elif oa == '2':
                break
            elif int(oa) not in range(1,3) :
                print("다시 입력해 주십시오")
            continue
        print("\n주문 내역은 아래와 같습니다.\n")

        for i in range(len(self.order_list)):
            print(f'{i+1}번 주문 : {self.order_list[i][0]}{self.order_list[i][1]} {self.order_list[i][2]} {self.order_list[i][3]}개 {self.order_list[i][4]*int(self.order_list[i][3])}원, {self.order_list[i][5]}\n')
            self.fp.append(self.order_list[i][4]*int(self.order_list[i][3]))

        print(f'\n총 결제 금액은 {sum(self.fp)}원 입니다.')

        oe = input("\n주문내역을 수정하시겠습니까?\n1.예  2.아니오\n:")
        while True :
            if oe == '1' :
                for i in range(len(self.order_list)):
                    print(f'{i+1}번 주문 : {self.order_list[i][0]}{self.order_list[i][1]} {self.order_list[i][2]} {self.order_list[i][3]}개 {self.order_list[i][4]*int(self.order_list[i][3])}원, {self.order_list[i][5]}\n')
                self.order_edit()
            elif oe == '2' :
                break
            else :
                continue
        self.payments()

if __name__ == '__main__':
    m=Kiosk()
    m.order()
