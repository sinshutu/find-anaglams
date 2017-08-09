# coding: utf-8
import os #テスト用
    
#ひらがなをローマ字で返す########################################
def jap_to_Alphabet(jap): 
    japWords   = list(jap)
    fiftyWords = list(
                 #a i u e o 
                 'あいうえお'\
                 'かきくけこ'\
                 'さしすせそ'\
                 'たちつてと'\
                 'なにぬねの'\
                 'はひふへほ'\
                 'まみむめも'\
                 'や＿ゆ＿よ'\
                 'らりるれろ'\
                 'わ＿を＿＿'\
                 'がぎぐげご'\
                 'ざじずぜぞ'\
                 'だぢづでど'\
                 'ばびぶべぼ'\
                 'ぱぴぷぺぽ'\
                 'ぁぃぅぇぉ'\
                 '＿＿っ＿＿'\
                 'ゃ＿ゅ＿ょ'
                 ) 
    initial     = ",k,s,t,n,h,m,y,r,w,g,z,d,b,p,x,xt,xy".split(",")
    aiueo       = list("aiueo")        
    
    specialWords = {'ん':'n','ー':'-'}
    
    ans = ''
    
    for jp in japWords:                         #入力文字　一文字ずつ
        for idx,fif in enumerate(fiftyWords):   #五十音    一文字ずつ
            if jp == fif:
                ans += initial[int(idx/5)]
                ans += aiueo[int(idx%5)]   
                continue
        for sp in specialWords:
            if jp == sp:
                ans += specialWords[sp] 
                continue

            
    return ans


#文字列をアルファベットで受け取り 
#アルファベットの数をリストで返す
def countAlphabet(word):
    alphabet        = list("abcdefghijklmnopqrstuvwxyz")#比較用配列
    alphabet_count  = [0]*len(alphabet)                 #文字集計用
    spell = list(word)

    for spl in spell:
        for idx , alp in enumerate(alphabet):
            if spl == alp :
                alphabet_count[idx] += 1
    return alphabet_count
#################################################################


#################################################################
#ファイルから　文字列を取得し　リストで返す　テスト用############
def getdata(dirName,fileName): #(ディレクトリ/ファイル群配列)
    readFile = open(dirName + '/' + fileName) #ファイルデータ取得
    words = readFile.readlines()              #文字列取得
    words2 = []                               #返却用
    for w in words:
        words2.append(w.replace('\n','') )    #改行文字削除
    return words2
#文字をリストで取得
#################################################################

#テスト
wordData = getdata('txtFile','testdata.txt')

for word in wordData:
    spldata = jap_to_Alphabet(word)
    cntdata = countAlphabet(spldata)

    print(word)
    print(spldata)
    print(cntdata,"\n")
