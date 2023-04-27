import tkinter # tkinter 기능을 사용 하겠다
import tkinter.font # tkinter의 .font 메소드 기능을 사용 하겠다
import random # random의 기능을 사용하겠다

lotto_num = range(1,46) # range x ~ y 의 전 숫자 까지 생성

def buttonClick(): # 함수를 생성
    label = tkinter.Label(window, text=str(random.sample(lotto_num,6))) # tkinter의 .Label 메소드를 이용해서 라벨을 프로그램 창 안에 배치하고 문자열을 이용해 lotto_num의 숫자 6개를 불러온다
    label.pack() # 라벨 배치
    
window=tkinter.Tk() # tkinter의 .TK 메소드 기능 사용
window.title("lotto") # 상단에 표시 될 프로그램 제목
window.geometry("400x200") # 생성한 프로그램의 창의 크기 (숫자x숫자)
window.resizable(False, False) # 창의 크기 넓이 , 길이 수정 불가 (False)

button = tkinter.Button(window, overrelief="solid",text="번호확인", width=15, command=buttonClick, repeatdelay=1000, repeatinterval=100)
# tkinter 의 button 메소드를 이용해 프로그램 창 안에 배치 / 버튼 음영 생성, 너비:15 , 커맨드 : 버튼 클릭 , 첫번째 클릭 시 지연 속도 1초 , 버튼 클릭 후 유지 시 0.1초 마다 생성
button.pack() # 버튼 배치

window.mainloop() # 종료 하지 않는 한 계속 가동되는 기능