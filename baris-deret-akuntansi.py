import math

periode = int(input("Periode (thn): "))
modal = int(input("Modal (1000): "))
bunga = int((input("Bunga (%): ")))
bunga = bunga / 100

#Function
def rounddown(num):
    return int(math.floor(num / 100000.0)) * 100000

def Anuitas(modal, bunga, periode):
    pembilang = modal*bunga
    penyebut = (1+(bunga))**(0-periode)
    anuitas = pembilang / (1 - penyebut)
    return anuitas

nilai_anuitas = rounddown(Anuitas(modal, bunga, periode))
anuitas = Anuitas(modal, bunga, periode)

print("\nHasil:")
print("Anuitas: Rp{:,.2f}". format(nilai_anuitas) + ", Selisih: Rp{:,.2f}". format(anuitas-nilai_anuitas))
for i in range(1, periode+1):
    print("\nModal: Rp{:,.2f}, ".format(modal))
    def Bunga(bunga):
        nilai_bunga = modal*bunga
        return int(nilai_bunga)

    def Angsuran(nilai_anuitas, nilai_bunga):
        nilai_angsuran = nilai_anuitas - nilai_bunga
        return int(nilai_angsuran)

    def Hutang(modal, nilai_angsuran):
        modal -= nilai_angsuran
        return int(modal)

    nilai_bunga = Bunga(bunga)
    nilai_angsuran = Angsuran(nilai_anuitas, nilai_bunga)
    modal = Hutang(modal, nilai_angsuran)

    print(f"Periode ke-{i} : " + "Bunga: Rp{:,.2f}, ".format(nilai_bunga) + "Angsuran: Rp{:,.2f}, ".format(nilai_angsuran) + "Sisa Hutang: Rp{:,.2f}".format(modal))

print("Besar Anuitas : Rp{:,.2f}".format(nilai_anuitas))