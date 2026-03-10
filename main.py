from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime

if __name__ == '__main__':
    calculate_salary(100500)
    get_employees('Список сотрудников пуст!')
    
    time = datetime.now()

    months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    print(f"Сегодня {time.day} {months[time.month - 1]} {time.year} года")
    print(f"Текущее время: {time.strftime('%H:%M')}")
    