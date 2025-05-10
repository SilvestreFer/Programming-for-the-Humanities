list_1 = ["rachmaninoff@fcsh.unl.pt", "aquino@fcsh.unl.pt", "bach@fcsh.unl.pt",
"descartes@fcsh.unl.pt", "wagner@fcsh.unl.pt", "buxtehude@fcsh.unl.pt",
"mozart@fcsh.unl.pt", "hume@fcsh.unl.pt"]

list_2 = {"plotino@fcsh.unl.pt", "descartes@fcsh.unl.pt", "bach@fcsh.unl.pt",
"hume@fcsh.unl.pt", "mozart@fcsh.unl.pt"}
list_3 = [53891, 39170, 23840, 7849, 18752]
list_4 = {72531:"dostoievski@fcsh.unl.pt", 3617:"kafka@fcsh.unl.pt",
12132:"equeiros@fcsh.unl.pt", 19281:"ortigao@fcsh.unl.pt"}


for email in list_1:
    if len(email) > 18:
        print(email)

index = 0
for email in list_2:
    print('Número: ' + str(list_3[index]) + ' E-mail: ' + email)
    index += 1
