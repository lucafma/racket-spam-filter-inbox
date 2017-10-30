import random

names = ["luca", "jheni", "patati", "blat", "pietro", "iago", "gui", "napo", "raj", "bia"]
servers = ["@gmail.com", "@hotmail.com", "@rc.unesp.br", "@yahoo.com", "@outlook.com", "@xxxgirls.com", "@xxxgirls.br"]
subjects = ["Prova", "Trabalho", "Spam", "Iniciacao Cientifica", "Aumento Peniano", "Aumente seu penis", "Gosta de cu?"]
messages = ["Professor gostaria de saber se a prova vai ter esses assuntos", "Quer aumentar seu penis? clique nesse link e descubra como: ", "Gostaria de marcar uma reuniao sobre iniciacao cientifica. Quando voce estaria disponivel?"]
email = "("

def build_email(names, servers):
    return random.choice(names) + random.choice(servers)

for i in range(0, int(input("Entre com número de emails a serem criados: "))):
    email += "(\"{}\" \"{}\" \"{}\" {})\n".format(build_email(names, servers), random.choice(subjects), random.choice(messages), i)

with open("test-db.txt", "a+") as f:
    f.write("{})".format(email))
f.closed
