import tkinter # tkinter 기능을 사용 하겠다
import tkinter.font # tkinter의 .font 메소드 기능을 사용 하겠다
import random # random의 기능을 사용하겠다

lotto_num = range(1, 46) # range x ~ y 의 전 숫자 까지 생성

def buttonClick(): # buttonClick 함수 생성
    print(random.sample(lotto_num,6)) # 버튼 클릭 시 랜덤 기능을 이용해 숫자 6개 랜덤 생성 하고 보여준다

window = tkinter.Tk()
window.title("lotto") # 상단에 표시 될 프로그램 제목
window.geometry("400x200") # 생성한 프로그램의 창의 크기 (숫자x숫자)
window.resizable(False, False) # 창의 크기 넓이 , 길이 수정 불가 (False)

button = tkinter.button(window, overrelief = "solid", text = "번호 확인", width = 15, # tkinter 의 button 메소드를 이용해 프로그램 창 안에 배치 및 클릭 시 번호 확인 되고 버튼의 위치 설명
                        command = buttonClick, repeatdelay = 1000, repeatinterval = 100)
button.pack() # 버튼 배치

window.mainloop # 종료 하지 않는 한 계속 가동되는 기능