import re
#pattern1 は、 例題　「2647, TYPE NO.=   53, POINT NO.=    10」 の2647の判定用の正規表現
pattern1 = re.compile(r"TYPE NO.=")
with open('Ag001hist0.txt','r',encoding='CP932') as f:
 whole_file =f.readlines()
 for word in whole_file:
        if re.search(pattern1,word) == None:
            pass
        else:
            print(word,end='')


