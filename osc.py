print('이 게임은 AI와 승부하는 가위바위보 게임입니다. 게임을 시작하시려면 "게임을 시작한다."를 입력하여 게임을 시작해주세요')
print('만약 게임을 하고 싶지 않다면 "게임을 종료한다."를 입력해주세요.')
gamePlay = ['게임을 시작한다.', '게임을 종료한다.', '게임을 계속한다.']
inpt1 = input('나:')
if inpt1 != gamePlay[1] and gamePlay[0]:
    print('잘못된 입력입니다. 다시 입력해주세요.')
    inpt1 = input('나:')
if inpt1 == gamePlay[1]:
    print('게임을 종료합니다.')
    print('ByeBye')
while inpt1 == gamePlay[0]:
    import random
    num = [1, 2, 3]
    you = random.choice(num) #1=가위; 2=바위; 3=보;
    print('가위바위보가 사작되면 가위, 바위, 보 중 무엇을 낼지 선택하세요.')
    print('안내면 진거, 가위바위보!')
    me = input('나:')
    if me == "가위":
        if you == 1:
            print('상대방:가위')
            print('비겼다')
        elif you == 2:
            print('상대방:바위')
            print('졌다')
        else:
            print('상대방:보')
            print('이겼다')
    elif me == "바위":
        if you == 1:
            print('상대방:가위')
            print('이겼다')
        elif you == 2:
            print('상대방:바위')
            print('비겼다')
        else:
            print('상대방:보')
            print('졌다')
    elif me == "보":
        if you == 1:
            print('상대방:가위')
            print('졌다')
        elif you == 2:
            print('상대방:바위')
            print('이겼다')
        else:
            print('상대방:보')
            print('비겼다')
    else:
        if you == 1:
            print('상대방:가위')
            print('졌다')
        elif you == 2:
            print('상대방:바위')
            print('졌다')
        else:
            print('상대방:보')
            print('졌다') 
    
    print('게임을 종료하실건가요? 아니면 게임을 계속하실건가요. 다음 선택지를 보고 번호를 입력하여 선택하세요')
    print('1.', end="")
    print(gamePlay[1], '2.', end="")
    print(gamePlay[2])
    inpt2 = int(input())
    if inpt2 == 1:
        print('게임을 종료합니다.')
        print('ByeBye')
        break
    elif inpt2 == 2:
        print('게임을 계속합니다.')
