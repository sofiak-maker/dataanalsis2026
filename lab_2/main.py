from core.processing import process_data, get_data_length, is_valid

def main():
    print("=== Обработка данных ===\n")
    
    input_data = "это пример данных"
    print(f"Исходные данные: {input_data}")
    print(f"Длина строки: {get_data_length(input_data)}")
    print(f"Строка не пустая? {is_valid(input_data)}")
    
    result = process_data(input_data)
    print(f"Результат обработки: {result}")
    
    empty_data = ""
    print(f"\nПустая строка: '{empty_data}'")
    print(f"Строка не пустая? {is_valid(empty_data)}")

if __name__ == "__main__":
    main() 
