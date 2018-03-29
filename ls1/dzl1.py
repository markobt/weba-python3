userInput = 0

while True:
  try:
     userInput = int(input("Введите совй год рождения: "))
  except ValueError:
     print("Не коректные данные (not an integer!)")
     continue
  else:
#    print("Correct (yes an integer!)")
     break

old = 2018 - userInput

#print(sum)

if old >= 18:
    print("Поздравляем на нашем сайте за", old )
else:
    print("Для Вас сайт не доступен, из-за возраста", old )

