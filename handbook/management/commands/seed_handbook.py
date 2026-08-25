from django.core.management.base import BaseCommand

from handbook.models import Exercise, Module

MODULES = [
    dict(
        number=1, slug='matematika', title='Рациональные числа',
        tag='Модуль 01 · Математика', accent='math', order=1,
        intro=(
            'Действия с положительными и отрицательными числами, обыкновенными '
            'и десятичными дробями — фундамент, на котором позже строится код '
            'в Модуле 3.'
        ),
    ),
    dict(
        number=2, slug='english', title='There is / There are · This / That',
        tag='Модуль 02 · English', accent='eng', order=2,
        intro=(
            'Грамматика, которая нужна, чтобы описать словами то, что в Модуле 3 '
            'будет описано блок-схемой: рабочий стол, серверную комнату, '
            'компоненты интерфейса.'
        ),
    ),
    dict(
        number=3, slug='informatika', title='Блок-схемы и алгоритмы на Python',
        tag='Модуль 03 · Информатика', accent='info', order=3,
        intro=(
            'То, что в Модуле 1 считалось на бумаге, здесь превращается '
            'в алгоритм: сначала блок-схема, затем код на Python с ветвлением '
            'if / elif / else.'
        ),
    ),
    dict(
        number=4, slug='optimizatsiya', title='Оптимизация алгоритма и antigravity',
        tag='Модуль 04 · Спецпрактикум', accent='opt', order=4,
        intro=(
            'Программа из Модуля 3 работает — но легко ломается. Здесь она '
            'превращается в код, который не боится плохого ввода.'
        ),
    ),
]

# (module_number, group_label, prompt, answer)
EXERCISES = [
    # Модуль 1 — Математика
    (1, '', '−5.6 + 3.2', '−2.4'),
    (1, '', '4⁄9 − (−2⁄9)', '6⁄9 = 2⁄3'),
    (1, '', '(−7) · (−0.5)', '3.5'),
    (1, '', '(−18) : 3 + (−4)', '−10'),
    (1, '', '2¼ − 3¾', '9⁄4 − 15⁄4 = −6⁄4 = −1.5'),
    (1, '', '(−1⁄2) · (4 − 6)', '(−1⁄2)·(−2) = 1'),
    (1, '', '0.6 − 1.2 + (−0.4)', '−1.0'),
    (1, '', '(−3⁄5) : (1⁄10)', '−6'),
    (1, '', '|−7| − |4 − 9|', '7 − 5 = 2'),
    (1, '', '(5 − 8) · (−2) + (−1⁄2)', '6 + (−0.5) = 5.5'),
    (1, '', (
        'Задача. Утром на складе было 240 деталей. За день привезли 75, '
        'а отгрузили 130. Сколько деталей осталось к вечеру? (представьте '
        'изменения как рациональные числа)'
    ), '240 + 75 − 130 = 185 деталей'),
    (1, '', (
        'Задача. Температура воды изменялась так: было 18 °C, опустилась '
        'на 5.5 °C, затем поднялась на 2 °C. Какая температура стала в итоге?'
    ), '18 − 5.5 + 2 = 14.5 °C'),

    # Модуль 2 — English
    (2, 'A. Вставьте is / are, isn’t / aren’t', 'There ___ a new laptop on my desk.', 'is'),
    (2, 'A. Вставьте is / are, isn’t / aren’t', 'There ___ many cables under the table.', 'are'),
    (2, 'A. Вставьте is / are, isn’t / aren’t', 'There ___ a printer in this room — we need to bring one. (отриц.)', 'isn’t'),
    (2, 'A. Вставьте is / are, isn’t / aren’t', '___ there any files in this folder?', 'Are'),
    (2, 'A. Вставьте is / are, isn’t / aren’t', 'There ___ much free space on the server. (отриц.)', 'isn’t'),
    (2, 'A. Вставьте is / are, isn’t / aren’t', 'There ___ three routers in the network room.', 'are'),
    (2, 'A. Вставьте is / are, isn’t / aren’t', '___ there a password on this computer?', 'Is'),
    (2, 'B. Выберите this / these / that / those', '(показывая на монитор рядом) ___ monitor is very old.', 'This'),
    (2, 'B. Выберите this / these / that / those', '(показывая на серверы в дальнем углу комнаты) ___ servers store our data.', 'Those'),
    (2, 'B. Выберите this / these / that / those', '(держа в руках клавиатуру) ___ is a mechanical keyboard.', 'This'),
    (2, 'B. Выберите this / these / that / those', '(показывая на старые кабели в углу комнаты) ___ cables are not used any more.', 'Those'),
    (2, 'C. Составьте предложение из слов, используя IT-лексику', 'there / be / two monitors / on the desk', 'There are two monitors on the desk.'),
    (2, 'C. Составьте предложение из слов, используя IT-лексику', 'there / not be / a printer / in the server room', 'There isn’t a printer in the server room.'),
    (2, 'C. Составьте предложение из слов, используя IT-лексику', 'this / be / my desktop — that / be / the server', 'This is my desktop; that is the server.'),
    (2, 'C. Составьте предложение из слов, используя IT-лексику', 'are / there / any icons / on the desktop', 'Are there any icons on the desktop?'),

    # Модуль 3 — Информатика (открытые задания, ответы не приводятся)
    (3, '', (
        'Постройте блок-схему и напишите функцию analyze_number(a), которая '
        'определяет знак числа a и вычисляет его модуль (используйте if / elif / '
        'else по трём случаям: a > 0, a < 0, a == 0).'
    ), ''),
    (3, '', 'Дополните compare_numbers так, чтобы она также сообщала, у какого из чисел модуль больше.', ''),
    (3, '', (
        'Запустите compare_numbers на числах из заданий Модуля 1 (например, №1 и №3) '
        'и сверьте вывод программы со своими вычислениями на бумаге — это и есть '
        'межпредметная связь между Модулем 1 и Модулем 3.'
    ), ''),

    # Модуль 4 — Спецпрактикум (открытые задания)
    (4, '', 'Добавьте в read_rational проверку на пустую строку с отдельным сообщением об ошибке.', ''),
    (4, '', (
        'Перепишите safe_ratio через try / except ZeroDivisionError вместо явной '
        'проверки if b == 0. Сравните оба подхода: какой ближе к принципу '
        '«Errors should never pass silently»?'
    ), ''),
    (4, '', (
        'Прогоните compare_numbers_v2.py на всех числах из заданий Модуля 1 '
        'и убедитесь, что ввод b = 0 больше не приводит к аварийному завершению '
        'программы.'
    ), ''),
]


class Command(BaseCommand):
    help = 'Наполняет пособие «Число, слово, код» модулями и заданиями (идемпотентно).'

    def handle(self, *args, **options):
        for data in MODULES:
            module, created = Module.objects.update_or_create(
                number=data['number'], defaults=data,
            )
            self.stdout.write(f'{"Создан" if created else "Обновлён"} модуль: {module}')

        counters = {}
        for number, group_label, prompt, answer in EXERCISES:
            module = Module.objects.get(number=number)
            counters[number] = counters.get(number, 0) + 1
            Exercise.objects.update_or_create(
                module=module, prompt=prompt,
                defaults=dict(group_label=group_label, answer=answer, order=counters[number]),
            )

        self.stdout.write(self.style.SUCCESS('Пособие «Число, слово, код» готово.'))
