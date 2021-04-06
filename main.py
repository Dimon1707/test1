print('привет угадай один из крупнейших городов россии')
my_word = 'Москва'
gess= ""
while gess != my_word:
    gess = input("")
    if gess == my_word:
        print('УГАДАЛ')
        break
    if gess != my_word:
        print('Попробуй ещё раз')
