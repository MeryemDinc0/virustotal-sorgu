# Basit bir hesap makinesi uygulaması

# Toplama işlemi
def add(x, y):
    return x + y

# Çıkarma işlemi
def subtract(x, y):
    return x - y

# Çarpma işlemi
def multiply(x, y):
    return x * y

# Bölme işlemi
def divide(x, y):
    if y == 0:
        return "Bölme hatası! Sıfıra bölme yapılamaz."
    else:
        return x / y

# Ana fonksiyon
def main():
    print("Basit Hesap Makinesi Programına Hoş Geldiniz!")
    print("Yapabileceğiniz işlemler:")
    print("1. Toplama")
    print("2. Çıkarma")
    print("3. Çarpma")
    print("4. Bölme")

    choice = input("Lütfen bir işlem seçin (1/2/3/4): ")

    num1 = float(input("İlk sayıyı girin: "))
    num2 = float(input("İkinci sayıyı girin: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Geçersiz işlem seçimi. Lütfen geçerli bir işlem seçin.")

if __name__ == "__main__":
    main()


