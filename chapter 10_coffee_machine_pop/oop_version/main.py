from menu import Menu               # from 파일명(소문자 시작) import 클래스 (대문자 시작)
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 외부 파일에서 import 해온 class들의 객체 생성
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# 반복
is_on = True
while is_on:
    choice = input(f"어떤 음료를 드시겠습니까? {menu.get_items()} >>> ").lower()
    # todo -1 : choice가 -> off / report / 오타났을 떄 작성하는 부분을 완성해라.
    if choice == "off":
        is_on = False
        print("자판기가 종료되었습니다.")
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    # 그 다음부터는 음료 이름을 정확하게 적었을 때, 혹은 오타났을 때에 해당합니다.
    else:
        drink = menu.find_drink(choice)  # 음료 객체를 변수명 drink에 저장
        if drink == None:  # choice에 오타가 있을 경우에 None이 반환되기 때문에 작성
            continue  # continue가 실행되면이 밑의 코드라인은 실행되지 않고, while 반복문의 맨 앞으로 돌아감
        # 여기서 부터 오타가 없이 메뉴 이름을 정확하게 작성했을 때의 로직
        # 재료가 충분한지 확인 -> 돈 받는다 -> 받은 돈의 음료 가격보다 높으면 -> 커피를 만든다
        # import 받은 애들은 하나도 수정 안하고 여기 부분만 작성해서 동일한 자판기 프로그램을 완성해라
        if coffee_maker.is_resource_sufficient(drink):
    # coffee_maker.is_resource_sufficient() 메서드를 확인해보면, drink.ingredients를 반복문 돌린다는 것을 확인할 수 있음.
    # 이제 주의해서 봐야할 점은 미리 작성된 메서드가 어떤 자료형의 argument를 요구하고 있는지임.
    # 즉, pop version에서처럼 동일하게 생각해서 drink.ingredidents를 argument로 넣었따면 오류가 발생했을 거임.
    # -> 미리 작성된 코드 부분이랑 return 타입을 확인해봐야함
            if money_machine.make_payment(drink) and money_machine.make_payment():
                coffee_maker.make_coffee(drink)