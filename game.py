"frist game"
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def info(self):
        print(f"Имя: {self.name}, Здоровье: {self.health}, Сила удара: {self.attack_power}")

    def attack(self, other):
        print(f"Вы встретили другого игрока {other.name}. Ваши действия:\n"
              "1. Убегу\n"
              "2. Ударю рукой\n"
              "3. Ударю ногой")
        action = input("Выберите номер действия: ")
        if action == "1":
            print(f"Вы убежали от игрока {other.name} ")
            print(f"игрок {other.name} запустил в вас свое оружие,\nи его оружие настигает вас")
            self.health -= self.attack_power * 2
            print(f"вы теперь имеет {self.health} здоровья")
            if other.health <= 0:
                print(f"вы повержаны(( вы проиграли")
            else:
                print(f"у вас еще есть {self.health} здоровье")
        elif action == "2":
            print(f"Вы ударили игрока {other.name} рукой и он потерял часть здоровья.")
            other.health -= self.attack_power
            print(f"Игрок {other.name} теперь имеет {other.health} здоровья")
            print(f"Игрок {other.name} разозлился и атакует вас. Ваши действия:\n"
                  "1. Увернусь\n"
                  "2. Увернусь и ударю его")

            counter_action = input("Выберите номер действия: ")
            if counter_action == "1":
                print(f"Вы увернулись от атаки игрока {other.name}.")
            elif counter_action == "2":
                print(f"Вы увернулись и сразу же атаковали игрока {other.name}.")
                other.health -= self.attack_power
                print(f"Игрок {other.name} теперь имеет {other.health} здоровья")
                if other.health <= 0:
                    print(f"Игрок {other.name} повержен! Вы победили!")
                else:
                    print("Игрок еще жив, продолжайте борьбу.")
                    print("выбор ваших действие:\n 1.ударю \n 2.использую супер\n выберите номер действие") 
                    user = input(": ")
                    if user == "1":
                        print("вы ударили его и он потерял часть здоровье")
                        other.health -= self.attack_power
                        print(f"Игрок {other.name} теперь имеет {other.health} здоровья")   
                        if other.health <= 0:
                          print(f"Игрок {other.name} повержен! Вы победили!")
                        else:
                           print("Игрок еще жив, продолжайте борьбу")                
                    
                    elif user == "2":
                        print("вы ударили его своим супером и нанесли тройной урон")
                        other.health -= self.attack_power * 3
                        print(f"Игрок {other.name} теперь имеет {other.health} здоровья")
                        if other.health <= 0:
                          print(f"Игрок {other.name} повержен! Вы победили!")
                        else:
                           print("Игрок еще жив, продолжайте борьбу")
            else:
                print("Неверный выбор. Вы пропустили свой ход")
        elif action == "3":
            print(f"Вы ударили игрока {other.name} ногой, и он потерял много здоровья")
            other.health -= self.attack_power * 2
            print(f"Игрок {other.name} теперь имеет {other.health} здоровья")
            if other.health <= 0:
                print(f"Игрок {other.name} повержен! Вы победили!")
            else:
                print("Игрок еще жив, продолжайте борьбу")
                print("выберите действие:\n 1.разабью его ебло чтоб не втыкал ато заебал\n 2.опять вьебу со всей силой с ноги\n выберите номер действие: ")
                user2 = input(": ")
                if user2 == "1":
                    print("разбили ему ебло и он потерял некоторую часть здоровья")
                    other.health -= self.attack_power

                    print(f"Игрок {other.name} теперь имеет {other.health} здоровья")
                    if other.health <= 0:
                      print(f"Игрок {other.name} повержен! Вы победили!")
                    else:
                      print("Игрок еще жив, продолжайте борьбу")
                elif user2 == "2":
                    print("вы вьебали ему с ноги он получил двойной урон")
                    other.health -= self.attack_power 
                    print(f"Игрок {other.name} теперь имеет {other.health} здоровья")
                    if other.health <= 0:
                      print(f"Игрок {other.name} повержен! Вы победили!")
                    else:
                      print("Игрок еще жив, продолжайте борьбу")
        else:
            print("Неверный выбор. Попробуйте снова")



# player = Character("Sultan(●'◡'●)", 50, 10)
# enemy = Character("игорь228", 30, 5)
# player.info()
# player.attack(enemy)
"second game"
import random
class Kamen:
        def __init__(self):
            self.choices = ["камень", "ножницы", "бумага"]
            
        def info(self):
            print(f"Вы можете выбрать из: {self.choices}")
            
        def igrat(self):
            print("выберите действие: камень, ножницы или бумага")
            bot_choice = random.choice(self.choices)
            player_choice = input("выберите: ").strip().lower()
            
            print(f"Бот выбрал: {bot_choice}")
            
            if player_choice == bot_choice:
                print("Ничья!")
            elif (player_choice == "камень" and bot_choice == "ножницы") or \
                (player_choice == "ножницы" and bot_choice == "бумага") or \
                (player_choice == "бумага" and bot_choice == "камень"):
                print("Вы победили!")
            elif (bot_choice== "камень" and player_choice == "ножницы") or \
                (bot_choice== "ножницы" and player_choice == "бумга") or \
                (bot_choice== "бумага" and player_choice == "камень"):
                print("Победил бот!")
            else:
                print("Нету такого ответа!")
                
igra = Kamen()
igra.info()
igra.igrat()
