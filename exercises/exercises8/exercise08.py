month = 4
day_classroom = 2
week_in_one_month = 4
class_missed = 0

_100_percent = (month*week_in_one_month)*day_classroom

_75_percent = (_100_percent*0.75)

class_missed =  int((_100_percent - _75_percent))

print(f"Os dias que Ricardo pode faltar aula são: {class_missed}")


