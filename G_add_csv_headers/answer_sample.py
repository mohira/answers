import shutil
from pathlib import Path


def main():
    root_path = Path(__file__).parent

    data_path = root_path / 'score_data'
    destination_path = root_path / 'dest_data'

    # 中途半端な状態にしないようにキープするため毎回削除している
    if destination_path.exists():
        shutil.rmtree(destination_path)

    shutil.copytree(data_path, destination_path)

    for file_path in destination_path.glob('**/*.csv'):
        with file_path.open(mode='r') as f:
            lines = f.readlines()

        header = '氏名,メールアドレス,得点\n'

        # すでに追加済みのデータが混在している可能性がある
        if not lines[0] == header:
            lines.insert(0, header)

            with file_path.open(mode='w') as f:
                f.writelines(lines)


if __name__ == '__main__':
    main()

