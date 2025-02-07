kuukausi_nro = int(input("anna jokin kuukausi numeromuodossa: "))

kuukaudet = ("tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu")
kuukausi = kuukaudet[kuukausi_nro-1]

if kuukausi_nro in range(3,6):
    print("kuukausi on kevät kuukausi!")
if kuukausi_nro in range(6,9):
    print("kuukausi on kesä kuukausi!")
if kuukausi_nro in range(9,12):
    print("kuukausi on kevät kuukausi!")
if kuukausi_nro in range(1,3):
    print("kuukausi on talvi kuukausi!")
if (kuukausi_nro == 12):
    print("kuukausi on talvi kuukausi!")






