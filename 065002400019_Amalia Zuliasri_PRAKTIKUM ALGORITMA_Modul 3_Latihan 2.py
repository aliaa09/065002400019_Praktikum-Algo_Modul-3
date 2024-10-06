import cmath

def akar_persamaan_kuadrat(a, b, c):
    # Menghitung determinan
    D = b**2 - 4*a*c
    print(f"Determinan (D) = {D}")
    
    # Menghitung akar-akar persamaan kuadrat
    if D > 0:
        x1 = (-b + cmath.sqrt(D)) / (2*a)
        x2 = (-b - cmath.sqrt(D)) / (2*a)
        print(f"Akar-akar real: x1 = {x1.real}, x2 = {x2.real}")
    elif D == 0:
        x = -b / (2*a)
        print(f"Akar real: x = {x}")
    else:
        # Akar kompleks
        x1 = (-b + cmath.sqrt(D)) / (2*a)
        x2 = (-b - cmath.sqrt(D)) / (2*a)
        print(f"Akar kompleks: x1 = {x1}, x2 = {x2}")

# Input koefisien
try:
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    c = float(input("Masukkan nilai c: "))
    
    if a == 0:
        print("Nilai a tidak boleh sama dengan 0.")
    else:
        akar_persamaan_kuadrat(a, b, c)
except ValueError:
    print("Input tidak valid. Harap masukkan angka.")
