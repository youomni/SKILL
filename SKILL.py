import time 
def move_forward(): 
  print("Робот делает шаг вперёд...") 
  time.sleep(1) # Ждём 1 секунду print("Шаг завершён.") 

# Основная программа
if __name__ == "__main__": 
  print("Начинаем движение.") 
  move_forward() # Делаем первый шаг 
  move_forward() # Делаем второй шаг print("Закончили движение.")
