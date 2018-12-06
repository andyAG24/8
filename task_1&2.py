phrase_list = input('Введите выражение, используя пробелы и только положительные числа:\n').split(' ')
i = 0

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

arguments = []
operations = ('+', '-', '*', '/')

if phrase_list[0] not in operations:
  raise AssertionError('Это не префиксная форма записи')
for item in phrase_list:
    if item in operations:
      operation = item
    elif is_number(item):
      try:
        assert int(item) >= 0
        arguments.append(int(item))
      except:
        print('Только положительные числа!')

try:
  if operation == '+':
    final_phrase = arguments[0] + arguments[1]
  elif operation == '-':
    final_phrase = arguments[0] - arguments[1]
  elif operation == '*':
    final_phrase = arguments[0] * arguments[1]
  elif operation == '/':
    final_phrase = arguments[0] / arguments[1]
except:
  print('Неправильный ввод')

try:
  print(arguments[0], operation, arguments[1], '=', final_phrase)
except:
  print('')