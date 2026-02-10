import json
import os

def task_5():
    LIBRARY_FILE = 'library.json'
    
    def load_library():
        if os.path.exists(LIBRARY_FILE):
            try:
                with open(LIBRARY_FILE, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Внимание: Файл поврежден или пуст. Создаем новую библиотеку.")
                return []
        return []
    
    def save_library(library):
        try:
            with open(LIBRARY_FILE, 'w', encoding='utf-8') as file:
                json.dump(library, file, ensure_ascii=False, indent=2)
            return True
        except IOError:
            print("Ошибка при сохранении файла!")
            return False
    
    def view_all_books(library):
        print("\n" + "=" * 60)
        print("ВСЕ КНИГИ В БИБЛИОТЕКЕ:")
        print("=" * 60)
        
        if not library:
            print("Библиотека пуста!")
            return
        
        for book in library:
            status = "Доступна" if book['available'] else "Выдана"
            print(f"ID: {book['id']}")
            print(f"  Название: {book['title']}")
            print(f"  Автор: {book['author']}")
            print(f"  Год издания: {book['year']}")
            print(f"  Статус: {status}")
            print("-" * 40)
    
    def search_books(library):
        print("\n" + "=" * 40)
        print("ПОИСК КНИГ:")
        print("=" * 40)
        
        search_term = input("Введите автора или название для поиска: ").strip().lower()
        
        results = []
        for book in library:
            if (search_term in book['title'].lower() or 
                search_term in book['author'].lower()):
                results.append(book)
        
        if results:
            print(f"\nНайдено {len(results)} книг(и):")
            for book in results:
                status = "Доступна" if book['available'] else "Выдана"
                print(f"  • {book['title']} ({book['author']}, {book['year']}) - {status}")
        else:
            print("Книги не найдены!")
        
        return results
    
    def add_book(library):
        print("\n" + "=" * 40)
        print("ДОБАВЛЕНИЕ НОВОЙ КНИГИ:")
        print("=" * 40)
        
        try:
            new_id = max([book['id'] for book in library], default=0) + 1
            
            title = input("Введите название книги: ").strip()
            author = input("Введите автора: ").strip()
            year = int(input("Введите год издания: ").strip())
            
            new_book = {
                'id': new_id,
                'title': title,
                'author': author,
                'year': year,
                'available': True
            }
            
            library.append(new_book)
            save_library(library)
            print(f"Книга '{title}' успешно добавлена с ID {new_id}!")
            
        except ValueError:
            print("Ошибка: Некорректный ввод года!")
        except Exception as e:
            print(f"Ошибка при добавлении книги: {e}")
    
    def change_availability(library):
        print("\n" + "=" * 40)
        print("ИЗМЕНЕНИЕ СТАТУСА КНИГИ:")
        print("=" * 40)
        
        try:
            book_id = int(input("Введите ID книги: ").strip())
            
            for book in library:
                if book['id'] == book_id:
                    current_status = "доступна" if book['available'] else "выдана"
                    new_status = not book['available']
                    
                    book['available'] = new_status
                    save_library(library)
                    
                    action = "возвращена" if new_status else "выдана"
                    print(f"Книга '{book['title']}' {action}!")
                    return
            
            print(f"Книга с ID {book_id} не найдена!")
            
        except ValueError:
            print("Ошибка: ID должен быть числом!")
    
    def delete_book(library):
        print("\n" + "=" * 40)
        print("УДАЛЕНИЕ КНИГИ:")
        print("=" * 40)
        
        try:
            book_id = int(input("Введите ID книги для удаления: ").strip())
            
            for i, book in enumerate(library):
                if book['id'] == book_id:
                    confirm = input(f"Вы уверены, что хотите удалить '{book['title']}'? (да/нет): ").strip().lower()
                    if confirm == 'да':
                        deleted_book = library.pop(i)
                        save_library(library)
                        print(f"Книга '{deleted_book['title']}' удалена!")
                    else:
                        print("Удаление отменено!")
                    return
            
            print(f"Книга с ID {book_id} не найдена!")
            
        except ValueError:
            print("Ошибка: ID должен быть числом!")
    
    def export_available_books(library):
        print("\n" + "=" * 40)
        print("ЭКСПОРТ ДОСТУПНЫХ КНИГ:")
        print("=" * 40)
        
        available_books = [book for book in library if book['available']]
        
        if not available_books:
            print("Нет доступных книг для экспорта!")
            return
        
        try:
            with open('available_books.txt', 'w', encoding='utf-8') as file:
                file.write("СПИСОК ДОСТУПНЫХ КНИГ В БИБЛИОТЕКЕ\n")
                file.write("=" * 50 + "\n\n")
                
                for book in available_books:
                    file.write(f"ID: {book['id']}\n")
                    file.write(f"Название: {book['title']}\n")
                    file.write(f"Автор: {book['author']}\n")
                    file.write(f"Год: {book['year']}\n")
                    file.write("-" * 30 + "\n")
            
            print(f"Экспортировано {len(available_books)} книг в файл available_books.txt!")
            
        except IOError:
            print("Ошибка при экспорте файла!")
    
    def show_menu():
        print("\n" + "=" * 50)
        print("МЕНЮ БИБЛИОТЕКИ:")
        print("=" * 50)
        print("1. Просмотр всех книг")
        print("2. Поиск по автору/названию")
        print("3. Добавление новой книги")
        print("4. Изменение статуса доступности")
        print("5. Удаление книги по ID")
        print("6. Экспорт доступных книг в файл")
        print("7. Выход")
        print("-" * 50)
    
    def initialize_library():
        initial_books = [
            {
                "id": 1,
                "title": "Мастер и Маргарита",
                "author": "Булгаков",
                "year": 1967,
                "available": True
            },
            {
                "id": 2,
                "title": "Преступление и наказание",
                "author": "Достоевский",
                "year": 1866,
                "available": False
            },
            {
                "id": 3,
                "title": "Война и мир",
                "author": "Толстой",
                "year": 1869,
                "available": True
            },
            {
                "id": 4,
                "title": "Евгений Онегин",
                "author": "Пушкин",
                "year": 1833,
                "available": True
            }
        ]
        
        if not os.path.exists(LIBRARY_FILE):
            save_library(initial_books)
            print("Библиотека инициализирована начальными данными!")
    
    try:
        initialize_library()
        
        library = load_library()
        print(f"Загружено {len(library)} книг из библиотеки")
        
        while True:
            show_menu()
            
            try:
                choice = input("\nВыберите действие (1-7): ").strip()
                
                if choice == '1':
                    view_all_books(library)
                elif choice == '2':
                    search_books(library)
                elif choice == '3':
                    add_book(library)
                elif choice == '4':
                    change_availability(library)
                elif choice == '5':
                    delete_book(library)
                elif choice == '6':
                    export_available_books(library)
                elif choice == '7':
                    print("\n" + "=" * 50)
                    print("Выход из программы. До свидания!")
                    print("=" * 50)
                    break
                else:
                    print("Неверный выбор! Пожалуйста, выберите от 1 до 7.")
            
            except KeyboardInterrupt:
                print("\n\nПрограмма прервана пользователем.")
                break
            except Exception as e:
                print(f"Произошла ошибка: {e}")
    
    except Exception as e:
        print(f"Критическая ошибка: {e}")

if __name__ == "__main__":
    task_5()