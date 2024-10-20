# (Стешенко Станіслав КН-31.1)
# Словник для зберігання даних про студентів
students = {
    "Стешенко Станіслав Олександрович": {
        "group": "КН-31.1",
        "course": 2,
        "grades": {
            "Програмування": 5,
            "Алгоритми": 4,
            "Чисельні методи": 4
        }
    }
}

# (Стешенко Станіслав КН-31.1)
# Функція для додавання інформації про нового студента
def add_student():
    pib = input("Введіть ПІБ студента: ")
    if pib in students:
        print(f"Студент '{pib}' вже існує у словнику.")
    else:
        try:
            group = input("Введіть номер групи: ")
            course = int(input("Введіть курс (число): "))
            subjects_count = int(input("Кількість предметів: "))

            grades = {}
            for _ in range(subjects_count):
                subject = input("Назва предмета: ")
                grade = int(input("Оцінка за предмет (1-5): "))
                grades[subject] = grade

            students[pib] = {
                "group": group,
                "course": course,
                "grades": grades
            }
            print(f"Запис додано: {pib}")
        except ValueError:
            print("Помилка: Невірний формат введених даних.")

# (Мороз Володимир КН-31.1)
def remove_student():
    pib = input("Введіть ПІБ студента, якого бажаєте видалити: ")
    if pib in students:
        del students[pib]
        print(f"Студента '{pib}' успішно видалено.")
    else:
        print(f"Студента '{pib}' не знайдено у словнику.")


# (Стешенко Станіслав КН-31.1)
# Головне меню для взаємодії з користувачем
def main():
    while True:
        print("\nМеню:")
        print("1. Додати нового студента")
        print("2. Видалити студента")
        print("3. Вийти")

        choice = input("Виберіть дію (1-2): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

# Виклик головної функції для запуску програми
main()
