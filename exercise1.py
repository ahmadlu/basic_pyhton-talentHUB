def CelciusToKelvin(suhu): #function untuk mengubah dari celcius ke kelvin
    k = suhu + 273      #rumus perhitungan celcius ke kelvin
    return f"Hasilnya : {suhu} C = {k} K" #mengembalikan dan menampilkan hasil 

def KelvinToCelsius(suhu): #function untuk mengubah dari kelvin ke celcius
    c = suhu - 273 #rumus perhitungan kelvin ke celcius
    return f"Hasilnya : {suhu} K = {c} C" #mengembalikan dan menampilkan hasil 

def ToFarenheit(suhu, jenis): #function untuk mengubah dari celcius atau kelvin ke farenheit 
    if jenis == "celcius": #kondisi jika jenis sama dengan celcius maka akan menjalankan rumus perubahan suhu dari celcius ke farenheit
        C_F = (suhu*9/5) +32  #rumus perhitungan celcius ke farenheit
        return f"Hasilnya : {suhu} C = {C_F} F" #mengembalikan dan menampilkan hasil 
    elif jenis == "kelvin": #kondisi jika jenis sama dengan kelvin maka akan menjalankan rumus perubahan suhu dari celcius ke farenheit
        K_F = (9/5*(suhu-273)+32) #rumus perhitungan kelvin ke farenheit
        return f"Hasilnya : {suhu} K = {K_F} F" #mengembalikan dan menampilkan hasil 
    else:
         return "Tidak valid"

def FarentheitTo(suhu, jenis):  #function untuk mengubah dari farenheit ke celcius atau kelvin
    a = 5/9*(suhu-32) #rumus dari celcius
    if jenis =="celcius": #kondisi jika jenis sama dengan celcius maka akan menjalankan rumus perubahan suhu dari  farenheit ke celcius
        F_C = a 
        return f"Hasilnya : {suhu} F = {F_C} C" #mengembalikan dan menampilkan hasil 
    elif jenis =="kelvin": #kondisi jika jenis sama dengan kelvin maka akan menjalankan rumus perubahan suhu dari  farenheit ke kelvin
        F_K = a + 273 #rumus farenheit ke kelvin sama dengan rumus celcius ke farenheit + 273
        return f"Hasilnya : {suhu} F = {F_K} K" #mengembalikan dan menampilkan hasil 
        
        
suhu = float(input("Masukan Suhu : "))
print("\n1. Celcius -> Kelvin\n2. Celcius -> Fahrenhit\n3. Kelvin -> Celcius\n4. Kelvin -> Farentheit\n5. Farentheit -> Celcius\n6. Fahrenhit -> Kelvin\n7. Tutup\n")
opsi = input("Pilih opsi 1-7 :")
if opsi =="1":
    print(CelciusToKelvin(suhu))
elif opsi =="2":
    print(ToFarenheit(suhu, jenis=("celcius")))
elif opsi == "3":
    print(KelvinToCelsius(suhu))
elif opsi == "4":
    print(ToFarenheit(suhu, jenis=("kelvin")))
elif opsi =="5":
    print(FarentheitTo(suhu, jenis=("celcius")))
elif opsi =="6":
    print(FarentheitTo(suhu, jenis=("kelvin")))
else:
    print("Keyword Anda Salah, Silahkan coba lagi!!")





    
    
    

        
        
