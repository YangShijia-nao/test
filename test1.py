import math

class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []
    
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("错误：除数不能为零！")
        return a / b
    
    def power(self, a, b):
        return a ** b
    
    def square_root(self, a):
        if a < 0:
            raise ValueError("错误：不能对负数开平方！")
        return math.sqrt(a)
    
    def factorial(self, a):
        if a < 0:
            raise ValueError("错误：不能计算负数的阶乘！")
        if a == 0:
            return 1
        return math.factorial(int(a))
    
    def log(self, a, base=10):
        if a <= 0:
            raise ValueError("错误：对数函数的参数必须大于零！")
        if base <= 0 or base == 1:
            raise ValueError("错误：对数的底数必须大于零且不等于1！")
        return math.log(a, base)
    
    def evaluate_expression(self, expression):
        """计算表达式（使用eval，注意安全性）"""
        try:
            # 限制可用的函数和变量，增强安全性
            allowed_names = {
                'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
                'log': math.log, 'log10': math.log10, 'sqrt': math.sqrt,
                'pi': math.pi, 'e': math.e
            }
            
            # 编译表达式
            code = compile(expression, "<string>", "eval")
            
            # 检查允许的名称
            for name in code.co_names:
                if name not in allowed_names:
                    raise NameError(f"使用未允许的名称: {name}")
            
            result = eval(code, {"__builtins__": {}}, allowed_names)
            return result
        except Exception as e:
            raise ValueError(f"表达式错误: {str(e)}")
    
    def add_to_history(self, operation, result):
        self.history.append(f"{operation} = {result}")
        if len(self.history) > 10:  # 只保留最近10条记录
            self.history.pop(0)
    
    def show_history(self):
        if not self.history:
            print("历史记录为空")
        else:
            print("计算历史：")
            for i, record in enumerate(self.history, 1):
                print(f"{i}. {record}")

def main():
    calc = Calculator()
    
    print("=" * 50)
    print("            Python 计算器")
    print("=" * 50)
    print("支持的操作：")
    print("1. 加法 (+)")
    print("2. 减法 (-)")
    print("3. 乘法 (*)")
    print("4. 除法 (/)")
    print("5. 幂运算 (^)")
    print("6. 平方根 (sqrt)")
    print("7. 阶乘 (!)")
    print("8. 对数 (log)")
    print("9. 表达式计算")
    print("10. 查看历史记录")
    print("11. 退出")
    print("=" * 50)
    
    while True:
        try:
            choice = input("\n请选择操作 (1-11): ").strip()
            
            if choice == '11':
                print("感谢使用计算器！")
                break
            
            elif choice == '10':
                calc.show_history()
                continue
            
            elif choice == '9':
                expr = input("请输入表达式 (例如: 2 + 3 * 4, sin(pi/2)): ")
                result = calc.evaluate_expression(expr)
                calc.add_to_history(expr, result)
                print(f"结果: {result}")
                continue
            
            if choice in ['1', '2', '3', '4', '5', '8']:
                try:
                    a = float(input("请输入第一个数字: "))
                    b = float(input("请输入第二个数字: "))
                except ValueError:
                    print("错误：请输入有效的数字！")
                    continue
                
                if choice == '1':
                    result = calc.add(a, b)
                    operation = f"{a} + {b}"
                elif choice == '2':
                    result = calc.subtract(a, b)
                    operation = f"{a} - {b}"
                elif choice == '3':
                    result = calc.multiply(a, b)
                    operation = f"{a} * {b}"
                elif choice == '4':
                    try:
                        result = calc.divide(a, b)
                        operation = f"{a} / {b}"
                    except ValueError as e:
                        print(e)
                        continue
                elif choice == '5':
                    result = calc.power(a, b)
                    operation = f"{a} ^ {b}"
                elif choice == '8':
                    try:
                        base = float(input("请输入底数 (默认为10): ") or 10)
                        result = calc.log(a, base)
                        operation = f"log_{base}({a})"
                    except ValueError as e:
                        print(e)
                        continue
            
            elif choice == '6':
                try:
                    a = float(input("请输入数字: "))
                    result = calc.square_root(a)
                    operation = f"√{a}"
                except ValueError as e:
                    print(e)
                    continue
            
            elif choice == '7':
                try:
                    a = float(input("请输入数字: "))
                    result = calc.factorial(a)
                    operation = f"{a}!"
                except ValueError as e:
                    print(e)
                    continue
            
            else:
                print("无效选择，请重新输入！")
                continue
            
            calc.add_to_history(operation, result)
            print(f"结果: {result}")
            
        except KeyboardInterrupt:
            print("\n\n感谢使用计算器！")
            break
        except Exception as e:
            print(f"发生错误: {str(e)}")

if __name__ == "__main__":
    main()