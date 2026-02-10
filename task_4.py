from datetime import datetime

def get_time():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def show_last_operations():
    try:
        with open("calculator.log", "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        if lines:
            print("\nПоследние 5 операций:")
            print("-" * 40)
            for line in lines[-5:]:
                print(line.strip())
        else:
            print("Лог-файл пуст")
    except:
        print("Лог-файл не найден")

def log_calculation(a, op, b, result):
    time_str = get_time()
    log_line = f"{time_str} {a} {op} {b} = {result}\n"
    
    with open("calculator.log", "a", encoding="utf-8") as f:
        f.write(log_line)
    
    print(f"Записано в лог: {log_line.strip()}")

def main():
    print("=== КАЛЬКУЛЯТОР С ЛОГИРОВАНИЕМ ===")
    print("(для выхода введите 'выход')")
    
    show_last_operations()
    
    while True:
        print("\n" + "=" * 40)
        
        try:
            a_input = input("Первое число: ").strip()
            if a_input.lower() == 'выход':
                break
            
            op = input("Операция (+, -, *, /): ").strip()
            if op.lower() == 'выход':
                break
            
            b_input = input("Второе число: ").strip()
            if b_input.lower() == 'выход':
                break
            
            a = float(a_input)
            b = float(b_input)
            
            if op == '+':
                result = a + b
            elif op == '-':
                result = a - b
            elif op == '*':
                result = a * b
            elif op == '/':
                if b == 0:
                    print("ОШИБКА: Деление на ноль!")
                    continue
                result = a / b
            else:
                print("ОШИБКА: Неверная операция!")
                continue
            
            print(f"Результат: {a} {op} {b} = {result}")
            
            log_calculation(a, op, b, result)
            
        except ValueError:
            print("ОШИБКА: Введите корректные числа!")
        except KeyboardInterrupt:
            print("\nВыход...")
            break
        except Exception as e:
            print(f"ОШИБКА: {e}")
    
    print("\nПрограмма завершена")

if __name__ == "__main__":
    main()