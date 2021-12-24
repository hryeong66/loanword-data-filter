import pandas as pd
import datetime

df = pd.read_excel("dictionary.xlsx")

def getWordList():
    print("단어장이 로드될 때까지 입력을 하지 말고 조금만 기다려주세요:)------------------")
    wordList = []
    startTime = datetime.datetime.now()
    print(f"startTime {startTime}")
    for word in df["발음"]:
        wordList.append(word)
    wordList.sort()
    print(f"endTime {datetime.datetime.now()}")
    print(f"총 {len(wordList)}개의 데이터를 가져오는데 걸린 시간 : {datetime.datetime.now() - startTime}")
    return wordList

