from datetime import datetime
from statistics import mean
from typing import Any, List, Tuple


def lecture_00() -> None:
    print('Escola de Dados da Alura!')

    firstname: str = 'Jefferson'
    lastname: str = 'Campos'

    bday_day: int = 5
    bday_month: str = 'August'
    bday_year: int = 1986
    print(f'Name is......: {firstname}')
    print(f'Lastname is..: {lastname}')
    for letter in firstname:
        print(letter)

    print('-----------------------')
    res: List[Any] = [print(char) for char in lastname]
    print(res)
    print(bday_day, bday_month, bday_year)
    print('Actual year:', 2024)
    print('Better actual year:', datetime.now().year)
    print(type(res))
    print(type(firstname))
    print(type(bday_day))
    print(type(True))
    print(type(100.00))

    name = 'Fabricio Daniel'
    age = 15
    score = 8.45
    approved = True
    print(name, age, score, approved)

    job_salary: List[Tuple[str, int, float]] = [
        ('Segurança', 5, 3000.00),
        ('Docente', 16, 6000.00),
        ('Diretoria', 1, 12500.00),
    ]

    total_job: int = 0
    total_salary: float = 0.00

    for job in job_salary:
        total_job += job[1]
        total_salary += job[1] * job[2]

    avarage_salary: float = total_salary / total_job
    print(f'{avarage_salary=}')

    print(f'Total employee: {total_job}')
    print(f'Salary difference: {job_salary[2][2] - job_salary[0][2]}')
    print(f'cube of 2: {2**3}')
    print(f'module of 7 by 3: {7 % 3}')
    print(f'integer division 7 // 3: {7 // 3}')

    txt = '  Geovana Alessandra dias Sanyos '
    print(txt.upper())
    print(txt.lower())
    print(txt.strip().replace('y', 't'))
    print(chr(64), chr(79), chr(108), chr(225))

    student: str = 'Jose Sampaio'
    student_score: float = 7.5
    print('Student name: %s got %.3f.' % (student, student_score))
    another_student: str = 'Jose Carlos'
    another_student_age: int = 14
    print('Nome do aluno: {} age {}'.format(another_student, another_student_age))  # noqa: E501


def lecture_01() -> None:
    person_name: str = str(input('Please, inform your name: '))
    person_age: int = int(input('Please, inform your age: '))
    person_height: float = float(input('Please, inform your height (mts): '))
    print(f'Hello, {person_name}, you are {person_age} years old and has {person_height} mts.')  # noqa: E501

    nombre: str = input('Write your name here: ')
    print(f'Collected name was: {nombre}')

    year: int = int(input('Inform the YEAR of your birthday: '))
    print('Year is:', year, type(year))

    initial_score: float = float(input('Show your initial score: '))
    print('Initial score:', initial_score, type(initial_score))


def lecture_02() -> None:
    number_00: float = float(input('inform number 01: '))
    number_01: float = float(input('inform number 02: '))
    number_02: float = float(input('inform number 03: '))

    print(f'sum of two {number_00} + {number_01} is: {number_00 + number_01}')
    print(f'sum of all three {number_00} + {number_01} + {number_02} is: {number_00 + number_01 + number_02}')  # noqa: E501
    print(f'difference from {number_00} - {number_01}: {number_00 - number_01}')  # noqa: E501
    print(f'mult {number_00} * {number_01}: {number_00 * number_01}')
    print(f"div {number_00} / {number_01} (second number {number_00} can't be null): {number_00 / number_01}")  # noqa: E501
    print(f'pot {number_00} ^ {number_01}: {number_00 ** number_01}')
    print(f'div int {number_00} // {number_01}: {number_00 // number_01}')
    print(f'remain {number_00} % {number_01}: {number_00 % number_01}')
    print(f'avarege ({number_00} + {number_01} {number_02}) / 3: {(number_00 + number_01 + number_02) / 3}')  # noqa: E501

    print(f'avg 5, 12, 20, 15: {(5 * 1) + (12 * 2) + (20 * 3) + (15 * 4) / 10}')  # noqa: E501

    phrase: str = 'Starting...'
    print(phrase)
    phrase = input('Inform some pharse here... ')
    print(phrase.upper())
    print(phrase.lower())
    my_phrase: str = '   MY   PHRASE   '
    print(my_phrase.strip())
    print(phrase.strip())
    print(phrase.strip().upper())
    print(phrase.strip().replace('e', 'f'))
    print(phrase.strip().replace('a', '@'))
    print(phrase.strip().replace('s', '$'))


def lecture_02b() -> None:
    avarage: float = 7.3
    result: str = 'NOT DONE'
    if avarage >= 7.00:
        result = 'DONE'

    print(f'result is: {result}')

    age_mary = int(input('Mary age: '))
    age_bia = int(input('Bia age: '))
    if age_mary > age_bia:
        print('Mary is older than Bia.')
    elif age_mary < age_bia:
        print('Bia is older than Mary.')

    employees_01 = int(input('Inform of totals of employees of company 01: '))
    employees_02 = int(input('Inform of totals of employees of company 02: '))
    if employees_01 >= employees_02:
        print('Company 01 has the same amount (or more) than company 02.')  # noqa: E501
    elif employees_01 <= employees_02:
        print('Company 01 has the same amount (or less) than company 02.')  # noqa: E501

    book_01 = input('Inform book 01: ')
    book_02 = input('Inform book 02: ')
    if book_01 == book_02:
        print('The title is equal!!')
    elif book_01 != book_02:
        print('The title is not equal!!')


def lecture_02_chalange() -> None:
    # n01: float = float(input('Inform number 01: '))
    # n02: float = float(input('Inform number 02: '))
    # print(f'The bigest number is: {f"Number 01: {n01}" if n01 > n02 else f"Number 02: {n02}"}')  # noqa: E501

    # growth: float = float(input('Inform the growth of your company (%): '))
    # print(f'The growth was {"positive" if growth > 0 else "negative"}!!')

    # letter: str = input('Inform a letter: ')
    # print(f'The is {"vogal" if letter in ["a", "e", "i", "o", "u"] else "consonant"}!!')  # noqa: E501

    # car_year_01: float = float(input("Inform car's value in year 01: "))
    # car_year_02: float = float(input("Inform car's value in year 02: "))
    # car_year_03: float = float(input("Inform car's value in year 03: "))
    # print(f'Avarage is: {mean([car_year_01, car_year_02, car_year_03])}; max is: {max([car_year_01, car_year_02, car_year_03])}; min is: {min([car_year_01, car_year_02, car_year_03])}')  # noqa: E501

    product_01: float = float(input("Inform product's value 01: "))
    product_02: float = float(input("Inform product's value 02: "))
    product_03: float = float(input("Inform product's value 03: "))
    print(f'min value is: {min([product_01, product_02, product_03])}')
    min_value: float = product_01
    if product_02 < min_value:
        min_value = product_02

    # if product_03 < min_value:
    #     min_value = product_03

    # print(f'min value is: {min_value}')


# lecture_00()

# lecture_01()

# lecture_02()

# lecture_02b()

lecture_02_chalange()
