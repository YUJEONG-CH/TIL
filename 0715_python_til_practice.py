#01.txt파일 만들었음  #r:읽기전용, w:쓰기전용-덮어씀, a: append이어씀
with open('01.txt', 'w', encoding='utf-8') as f:
    f.write('연습\n')
    for i in range(1,5):
       f.write(f'{i}번째\n')

    f.write('김유정\n')
    f.write('김이정\n')
    f.write('김오정\n')
    f.write('박은정\n')
    f.write('정유정\n')
    f.write('민유정\n')
    f.write('최유정\n')





with open('01.txt', 'r', encoding='utf-8') as f:
    text=f.read()
    print(text, type(text))
    names=text.split()
    cnt=0
    for name in names:
        #김씨
        if name[0]=='김':
            cnt+=1
    print(cnt)