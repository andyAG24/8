phrase_input = input('Введите выражение, используя пробелы и только положительные числа:\n').split(' ')
phrase_list = list(phrase_input)
i = 0

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

a = []

if phrase_list[0] != '+' and phrase_list[0] != '-' and phrase_list[0] != '*' and phrase_list[0] != '/':
  raise AssertionError('Это не префиксная форма записи')   

while i < len(phrase_list):
  if phrase_list[i] == '+' or phrase_list[i] == '-' or phrase_list[i] == '*' or phrase_list[i] == '/':
    znak = phrase_list[i]
  elif is_number(phrase_list[i]) == True:
    if int(phrase_list[i]) <= 0: 
      raise AssertionError('Введено отрицательное число')  
    a.append(int(phrase_list[i]))
  i += 1

try:
  if znak == '+':
    final_phrase = a[0] + a[1]
  elif znak == '-':
    final_phrase = a[0] - a[1]
  elif znak == '*':
    final_phrase = a[0] * a[1]
  elif znak == '/':
    final_phrase = a[0] / a[1]
except:
  print('Неправильный ввод')

try:
  print(a[0], znak, a[1], '=', final_phrase)
except:
  print('')

