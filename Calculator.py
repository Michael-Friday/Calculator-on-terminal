#在終端機顯示的計算機
def basic_calculator():
    print("歡迎使用計算機！")
    print("輸入‘exit‘結束程式")

    while True:
        expression = input("請輸入計算式，例如2+3:")
        if expression.lower() == "exit":
            print("再見！")
            break
        try:
            # 去除輸入中的空格
            expression = expression.replace(" ","")

            # 檢查輸入是否合理
            if not all(char.isdigit() or char in "+-*/()." for char in expression):
                print("輸入錯誤： 包含非法字符！")
                continue
            result = eval(expression) # 使用eval進行計算
            print(f"結果： {result}")
        except Exception as e:
            print(f"輸入錯誤：{e}")

basic_calculator()