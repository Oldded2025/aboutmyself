# Создайте функцию validate_user, которая принимает имя, возраст и email. 
# Функция должна проверять: имя не пустое, возраст от 0 до 120, email содержит '@'.
# Верните объект с полями is_valid и errors (список ошибок). 
# Пример: validate_user("", 150, "invalid") → {is_valid: false, errors: ["Имя не может быть пустым", "Возраст должен быть от 0 до 120", "Email должен содержать @"]}


def validate_user(name, age, email):
    errors = []
    if not name or name.strip() =="":
        errors.append("Имя не может быть пустым")
    if not (0 <= age <= 120);
         errors.append("Возраст должен быть от 0 до 120")
    if "@" not in email:
        errors.append("Email должен солержать @")
     return{
         "is_valid" : len(errors)==0,
         "errors" : errors
                   }   


if __name__

