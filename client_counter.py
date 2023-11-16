from websocket import create_connection
import tkinter as tk
import json

HOST = "ws://localhost:13254"

def command_man_member():
    message = {
        "group":"man_member",
        "action":"display"
    }
    json_str = json.dumps(message)
    ws = create_connection("ws://localhost:13254")
    ws.send(json_str)
    ws.close()

    print(f"Received : {message}")

def command_woman_member():
    message = {
        "group":"woman_member",
        "action":"display"
    }
    json_str = json.dumps(message)
    ws = create_connection("ws://localhost:13254")
    ws.send(json_str)
    ws.close()
    print(f"Received : {message}")

def command_man_non_member():
    message = {
        "group":"man_non_member",
        "action":"display"
    }
    json_str = json.dumps(message)
    ws = create_connection("ws://localhost:13254")
    ws.send(json_str)
    ws.close()
    print(f"Received : {message}")

def command_woman_non_member():
    message = {
        "group":"woman_non_member",
        "action":"display"
    }
    json_str = json.dumps(message)
    ws = create_connection("ws://localhost:13254")
    ws.send(json_str)
    ws.close()
    print(f"Received : {message}")


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Church member attendence counter')

    frame1 = tk.Frame(master=window, width=200, height=100, bg="red")
    frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    #add child label woman member conuter
    labelMemberWoman = tk.Label(master=frame1, text='Member Wanita', bg='red', fg='black')
    labelMemberWoman.place(x = 40, y=10)

    buttonCounterMemberWoman = tk.Button(master=frame1, text='Counter member wanita', bg='red',  command=command_woman_member)
    buttonCounterMemberWoman.place(x=5, y=50)

    frame2 = tk.Frame(master=window, width=200, height=100, bg='yellow')
    frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    #add child label man member counter
    labelMemberMemberMan = tk.Label(master=frame2, text='Member Pria', bg='yellow', fg='black')
    labelMemberMemberMan.place(x = 55, y=10)

    #add child button woman member counter
    buttonCounterMemberMan = tk.Button(master=frame2, text='Counter member pria', bg='yellow', command=command_man_member)
    buttonCounterMemberMan.place(x=25, y=50)

    #add child container woman non member
    frame3 =  tk.Frame(master=window, width=200, height=100, bg='blue')
    frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    #add child label man member counter
    labelMemberMemberMan = tk.Label(master=frame3, text='Member simpatisan pria', bg='blue', fg='black')
    labelMemberMemberMan.place(x = 25, y=10)

    buttonCounterNonMemberMan = tk.Button(master=frame3, text='Counter simpatisan pria', bg='yellow', command=command_man_non_member)
    buttonCounterNonMemberMan.place(x=10, y=50)

    frame4 = tk.Frame(master=window, width=200, height=100, bg='green')
    frame4.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    #add child label man member counter
    labelMemberMemberMan = tk.Label(master=frame4, text='Member simpatisan wanita', bg='green', fg='black')
    labelMemberMemberMan.place(x = 15, y=10)

    buttonCounterNonMemberWoman = tk.Button(master=frame4, text='Counter simpatisan wanita', bg='green', command=command_woman_non_member)
    buttonCounterNonMemberWoman.place(x=5, y=50)

    window.mainloop()
