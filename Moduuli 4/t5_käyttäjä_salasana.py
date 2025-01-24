käyttäjä_oikea = "python"
salasana_oikea = "rules"

yritykset = 0
yritykset_enintään = 5

while yritykset<yritykset_enintään:
    käyttäjä = input("anna käyttäjätunnus: ")
    salasana = input("anna salasana: ")
    if käyttäjä==käyttäjä_oikea and salasana==salasana_oikea:
        print("Tervetuloa!")
        break
    else:
        yritykset+=1
if yritykset==yritykset_enintään:
    print("pääsy evätty.")




















