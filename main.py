from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import decorator

if __name__ == '__main__':
    print(datetime.now())
    calculate_salary()
    get_employees()