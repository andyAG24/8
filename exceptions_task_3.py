documents = [
  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
  {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
  {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
  {"type": "license", "number": "1236"}
]

directories = {
  '1': ['2207 876234', '11-2'],
  '2': ['10006'],
  '3': []
}

def show_all_list():
  print("----------Команда-l(list)------------")
  i = 0
  while i <= len(documents) - 1:
    try:
      documents[i]["name"] == ""
    except:
      documents[i]["name"] = "Владелец не найден"
    print(documents[i]["type"], documents[i]["number"], documents[i]["name"])
    i += 1
  print("\n")

show_all_list()
