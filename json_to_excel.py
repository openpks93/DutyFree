import pandas

# xlsx 형식으로 만들기
pandas.read_json('granddfs_cosmetics.json',  encoding='UTF8', orient='index').to_excel('granddfs_cosmetics.xlsx', encoding='UTF8')

# csv형식으로 만들기 -> 엑셀로 열면 한글이 깨짐 메모장으로 열면 안깨짐 -> xlsx파일을 csv로 변환해야할거 같음
pandas.read_json('granddfs_cosmetics.json',  encoding='UTF8', orient='index').to_csv('granddfs_cosmetics.csv', encoding='UTF8')

