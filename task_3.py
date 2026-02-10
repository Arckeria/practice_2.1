def main():
    print("=== ОБРАБОТКА CSV-ФАЙЛА ТОВАРОВ ===")
    
    try:
        with open("products.csv", "r", encoding="utf-8") as f:
            data = f.read()
    except:
        data = "Название,Цена,Количество\nЯблоки,100,50\nБананы,80,30\nМолоко,120,20\nХлеб,40,100"
        with open("products.csv", "w", encoding="utf-8") as f:
            f.write(data)
        print("Файл создан")
    
    products = []
    total_value = 0
    
    with open("products.csv", "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines[1:]:
        line = line.strip()
        if line:
            parts = line.split(',')
            if len(parts) >= 3:
                try:
                    name = parts[0]
                    price = int(parts[1])
                    quantity = int(parts[2])
                    value = price * quantity
                    total_value += value
                    
                    products.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity,
                        "value": value
                    })
                except:
                    continue
    
    print("\nТовары на складе:")
    print("-" * 40)
    for p in products:
        print(f"{p['name']}: {p['price']} руб. × {p['quantity']} шт. = {p['value']} руб.")
    
    print("-" * 40)
    print(f"ОБЩАЯ СТОИМОСТЬ: {total_value} руб.")
    
    print("\n--- Поиск товара ---")
    search = input("Введите название для поиска: ").lower()
    found = [p for p in products if search in p["name"].lower()]
    
    if found:
        print(f"Найдено {len(found)} товаров:")
        for p in found:
            print(f"  - {p['name']}: {p['price']} руб., {p['quantity']} шт.")
    else:
        print("Товар не найден")
    
    print("\n--- Добавление товара ---")
    add_more = input("Добавить новый товар? (да/нет): ").lower()
    
    if add_more == "да":
        name = input("Название: ")
        try:
            price = int(input("Цена: "))
            quantity = int(input("Количество: "))
            
            with open("products.csv", "a", encoding="utf-8") as f:
                f.write(f"\n{name},{price},{quantity}")
            print("Товар добавлен")
        except:
            print("Ошибка при добавлении")
    
    print("\nПрограмма завершена")

if __name__ == "__main__":
    main()