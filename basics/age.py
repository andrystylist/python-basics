from datetime import date 
  
def calculate_age(born_date: date, current_date: date=None) -> int: 
    today: date = current_date if current_date else date.today() # Operador Ternario o Expresion Ternaria
    # today = date.today()
    # if current_date:
    #     today = current_date
    # today = current_date ? current_date : date.today() # En otros lenguajes
    age: int = today.year - born_date.year - int((today.month, today.day) < (born_date.month, born_date.day))
    return age
