import os
DIARY_FILE = "my_mood_diary.txt"

def update_mood_diary():
    
    while True:
        mood = input("Як ти себе почуваєшь сьогодні (обери 'chudowo', 'normalno', 'vtomlenno', 'pogano'): ").lower()
        if mood in ['chudowo', 'normalno', 'vtomlenno', 'pogano']:
            break
        print("Будь ласка введи один з варіантів настрою.")
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = f"[{timestamp}] Настрій: {mood}\n"

    try:
        with open(DIARY_FILE, 'a', encoding='utf-8') as file:
            file.write(log_entry)
    
    except IOError:
        print(f"Помилка: Не вдалося записати у файл {DIARY_FILE}.")
        return
    else:
        print(f"Настрій успішно записано у файл! ✅ ({mood}).")
    print("\n--- Histrory настрою ---")


    try:
        if not os.path.exists(DIARY_FILE):
            print("Ще немає записів у щоденнику настрою.")
            return

        with open(DIARY_FILE, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

    except IOError:
        
        print(f"Помилка: Не вдалося прочитати файл {DIARY_FILE}.")
    
    
update_mood_diary()
