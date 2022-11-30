import os

print("###### lees scherm ######")
chat_file = "chat.txt"
isExist = True


def lees():
    f = open(chat_file, 'r')
    print(f.read())


def check_bestand():
    if isExist == os.path.exists(chat_file):
        lees()
    else:
       f = open("chat.txt", 'a')
       f.write("Welkom!")
       f.close()
       lees()

check_bestand()