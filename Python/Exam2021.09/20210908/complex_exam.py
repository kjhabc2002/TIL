def buy_A_car(options):
    print(f"다음 사양의 자동차를 구입하십니다:")

    for option in options:
        print(f"{option} : {options[option]}")

options={"seat" : "가죽", "blackbox":"최신"}

buy_A_car(options)