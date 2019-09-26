def show_kuku2(max_row: int, max_col: int) -> None:
    for i in range(1, max_row + 1):
        for j in range(1, max_col + 1):
            product = i * j

            print(f'{product} ', end='')

        print('\n', end='')


def main():
    max_row = int(input('行数を入力してください: '))
    max_col = int(input('列数を入力してください: '))

    show_kuku2(max_row, max_col)


if __name__ == '__main__':
    main()
