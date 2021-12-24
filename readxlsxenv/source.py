import wordData
import pandas as pd
import openpyxl as xl
import datetime


wordList = wordData.getWordList()
print("다른 파일 이름을 입력한 후 엔터를 눌러주세요! 끝내려면 q를 입력해주세요")
fileName = input()
while(fileName != 'q'):
    df = pd.read_excel(f"data/{fileName}.xlsx")
    wb = xl.Workbook()
    sheet = wb.active
    sheet.title = "sheet"
    startTime = datetime.datetime.now()

    def refineList(wordList):
        deleteList = []
        wordList.sort(key=len)
        for i in range(len(wordList) - 1):
            for j in range(i + 1, len(wordList)):
                if wordList[i] in wordList[j]:
                    deleteList.append(wordList[i])
        return list(set(wordList).difference(deleteList))


    for statement in df["스크립트"]:
        if type(statement) != type(""):
            sheet.append([" "])
            continue
        containWordList = []
        for word in wordList:
            if word in statement and len(word) > 1:
                containWordList.append(word)
        containWordList = refineList(containWordList)
        containWordList.insert(0, statement)
        sheet.append(containWordList)
        print(f"{containWordList}")

    print(f"총 걸린 시간 : {datetime.datetime.now() - startTime}")
    wb.save(f"1220/result/{fileName}.xlsx")
    wb.close()
    print("다른 파일 이름을 적어주세요, 끝내려면 q를 입력해주세요")
    fileName = input()

