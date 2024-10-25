# TODO Найдите количество книг, которое можно разместить на дискете
value = 1.44 * 1024 * 1024
strings = 50
symbols = 25
pages = 100
answer = int(value // (strings * symbols * pages * 4))
print("Количество книг, помещающихся на дискету:", answer)
