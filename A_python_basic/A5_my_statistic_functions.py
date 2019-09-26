from typing import List


def calculation_total(numbers: List[int]) -> int:
    total = 0

    for num in numbers:
        total += num

    return total


def calculation_max(numbers: List[int]) -> int:
    max_number = numbers[0]

    for num in numbers[1:]:
        if num > max_number:
            max_number = num

    return max_number


def calculation_min(numbers: List[int]) -> int:
    min_number = numbers[0]

    for num in numbers[1:]:
        if num < min_number:
            min_number = num

    return min_number


def calculation_avg(numbers: List[int]) -> int:
    total = calculation_total(numbers)

    return total // len(numbers)


def main():
    # ユーザーからの入力を受け取る
    input_data = input('データを入力してください(スペース区切り) > ')

    # 文字列のリストに変換する
    numbers_as_str = input_data.split(' ')

    # 整数リストに変換する
    numbers = []  # 空のリストを生成
    for number_as_str in numbers_as_str:
        int_num = int(number_as_str)  # 整数に変換

        numbers.append(int_num)  # numbersというリストに要素を追加

    # リスト内包表記をつかってもよい
    numbers = [int(num) for num in numbers_as_str]

    # 各統計量を計算する(合計値, 最大値, 最小値, 平均値)
    total = calculation_total(numbers)
    maximum = calculation_max(numbers)
    minimum = calculation_min(numbers)
    average = calculation_avg(numbers)

    # ユーザーに見やすいようにフォーマットして出力する
    print(f'合計値: {total}')
    print(f'最大値: {maximum}')
    print(f'最小値: {minimum}')
    print(f'平均値: {average}')


if __name__ == '__main__':
    main()
