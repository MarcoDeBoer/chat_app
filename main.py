from applescript import tell
where_is_lees = 'PycharmProjects/chat_app/lees.py'
where_is_schrijf = 'PycharmProjects/chat_app/schrijf.py'
name = ""

while name == "":
    name = input("Voor de chat app is een naam belangrijk, geef uw naam op : ")
    if len(name)== 0:
        print("Om chats te kunnen onderscheiden hebben we uw naam nodig.")
    else:
        # lees app
        what_to_start = f"python3 {where_is_lees}"
        tell.app('Terminal', 'do script "' + what_to_start + '"')
        # schrijf app
        what_to_start = f"python3 {where_is_schrijf}"
        tell.app('Terminal', 'do script "' + what_to_start + '"')
