def main():
    try:
        print("Чтение данных из файла students.txt...")
        try:
            with open('students.txt', 'r', encoding='utf-8') as file:
                lines = file.readlines()
            print(f"Успешно прочитано {len(lines)} строк.")
        except FileNotFoundError:
            print("Ошибка: Файл students.txt не найден в текущей директории.")
            return
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return
        
        if not lines:
            print("Файл students.txt пуст.")
            return
        
        students_data = []
        
        print("\nОбработка данных...")
        for line_num, line in enumerate(lines, 1):
            try:
                line = line.strip()
                if not line:
                    continue
                    
                if ':' not in line:
                    print(f"Предупреждение: Строка {line_num} имеет неверный формат. Пропускаем.")
                    continue
                    
                name, grades_str = line.split(':', 1)
                name = name.strip()
                
                try:
                    grades = [int(grade.strip()) for grade in grades_str.split(',')]
                except ValueError:
                    print(f"Предупреждение: Неверный формат оценок в строке {line_num}. Пропускаем.")
                    continue
                
                if any(grade < 1 or grade > 5 for grade in grades):
                    print(f"Предупреждение: Оценки должны быть от 1 до 5 в строке {line_num}. Пропускаем.")
                    continue
                
                if not grades:
                    print(f"Предупреждение: Нет оценок у студента {name}. Пропускаем.")
                    continue
                
                average = sum(grades) / len(grades)
                
                students_data.append({
                    'name': name,
                    'grades': grades,
                    'average': average
                })
                
            except Exception as e:
                print(f"Ошибка обработки строки {line_num}: {e}. Пропускаем.")
                continue
        
        if not students_data:
            print("Нет корректных данных для обработки.")
            return
        
        print("\nФильтрация студентов со средним баллом выше 4.0...")
        filtered_students = [s for s in students_data if s['average'] > 4.0]
        
        if filtered_students:
            try:
                with open('result.txt', 'w', encoding='utf-8') as result_file:
                    for student in filtered_students:
                        result_file.write(f"{student['name']}:{student['average']:.2f}\n")
                print(f"Записано {len(filtered_students)} студентов в файл result.txt")
            except Exception as e:
                print(f"Ошибка при записи в файл result.txt: {e}")
        else:
            print("Нет студентов со средним баллом выше 4.0")
            with open('result.txt', 'w', encoding='utf-8') as result_file:
                result_file.write("")
        
        print("\nПоиск студента с наивысшим средним баллом...")
        best_student = max(students_data, key=lambda x: x['average'])
        
        print("\n" + "="*50)
        print("СПИСОК ВСЕХ СТУДЕНТОВ:")
        print("="*50)
        for student in students_data:
            print(f"{student['name']}: оценки {student['grades']}, средний балл: {student['average']:.2f}")
        
        print("\n" + "="*50)
        print("РЕЗУЛЬТАТЫ:")
        print("="*50)
        
        if filtered_students:
            print(f"Студенты со средним баллом выше 4.0 ({len(filtered_students)} чел.):")
            for student in filtered_students:
                print(f"  - {student['name']}: {student['average']:.2f}")
        else:
            print("Нет студентов со средним баллом выше 4.0")
        
        print(f"\nСтудент с наивысшим средним баллом:")
        print(f"  {best_student['name']}: {best_student['average']:.2f}")
        print(f"  Оценки: {best_student['grades']}")
        print("="*50)
        
        print("\nПрограмма успешно завершена!")
        
    except Exception as e:
        print(f"Критическая ошибка: {e}")

if __name__ == "__main__":
    main()