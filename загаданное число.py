import numpy as np

print('Программа загадала число, вы должны его отгадать')
N = input('Введите максимальное число которое может загадать компьютер: ')
k = k_0 = int(input('Введите сколько попыток дается пользователю на правильный ответ: '))
n_random = np.random.randint(0, N)
print(n_random)

flag = 0
print('Попробуйте угадать загаданное компьютером число: ')
while k != 0 and flag == 0:
    n_answer = int(input())
    if n_random == n_answer:
        flag = 1  # Вы угадали число
    else:
        k -= 1  # if k == 0: Попытки закончились
        if k != 0:
            if n_random < n_answer:
                answer_1 = 'МЕНЬШЕ'
            else:
                answer_1 = 'БОЛЬШЕ'
            print(f'Поробуйте угадать число ещё раз, зная что загаданное компьютером число {answer_1} введенного вами.')
if flag == 0:
    if k_0 == 1:
        answer_2 = 'попытку.'
    elif k_0 > 1 and k_0 < 5:
        answer_2 = 'попытки.'
    else:
        answer_2 = 'попыток.'
    print(f'Попытки закончились, вы не смогли угадать число {n_random} за {k_0} {answer_2}')
else:
    if k == 1:
        answer_2 = 'попытку'
    elif k > 1 and k < 5:
        answer_2 = 'попытки'
    else:
        answer_2 = 'попыток'
    print(f'Поздравляю, вы смогли угадать число {n_random} за {k} {answer_2} !!!')