def generator():
    num = yield
    while True:
        num = yield print(num)


gen = generator()
gen.send(None)  # идиентификация генератора
gen.send(5)
gen.throw(ValueError)  # отправляем ошибку в генератор для обработки
gen.close()  # закрываем генератор
