# coding :utf-8
hira = list(''\
    'あいうえお'\
    'かきくけこ'\
    'さしすせそ'\
    'たちつてと'\
    'なにぬねの'\
    'はひふへほ'\
    'まみむめも'\
    'らりるれろ'\
    'がぎぐげご'\
    'ざじずぜぞ'\
    'だぢづでど'\
    'ばびぶべぼ'\
    'ぱぴぷぺぽ'\
    'やゆよ'\
    'わをん'\
    'ぁぃぅぇぉ'\
    'っゃゅょ'
    )
kana = list(''\
    'アイウエオ'\
    'カキクケコ'\
    'サシスセソ'\
    'タチツテト'\
    'ナニヌネノ'\
    'ハヒフヘホ'\
    'マミムメモ'\
    'ラリルレロ'\
    'ガギグゲゴ'\
    'ザジズゼゾ'\
    'ダヂヅデド'\
    'バビブベボ'\
    'パピプペポ'\
    'ヤユヨ'\
    'ワヲン'\
    'ァィゥェォ'\
    'ッャュョ'
    )
print("h_to_k = {")
for idx in range(0,len(hira),5):
    for pls in range(5):
        print( "\'"+hira[idx+pls]+"\':\'"+kana[idx+pls]+"\',",end="")
    print("")
print("\'ー\':\'-\' }")



