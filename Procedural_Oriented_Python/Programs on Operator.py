print("Area of a circle")
r=int(input("Enter radius of a circle: "))
print(f"Area of a circle is {round((2*(22/7))*(r**2),2)}")

print("\nTemprature Converter")
t=float(input("Enter temprature in degree celcius: "))
print(f"{t}° celsius = {t*(9/5)+32}° Fahrenheit. ")
print(f"{t}° celsius = {t+273.15}° Kelvin")

print("\nCurrency Converter")
c=int(input("Enter India rupees: "))
USD = round(c*0.011,2)
SAR = round(c*0.040,2)
CHY = round(c*0.071,2)
KWD = round(c*0.0032,2)
EUR = round(c*0.0091,2)
print(f"Equivalent to ..\nAmerican Dollar={USD}$\nSaudi Riyal={SAR}ر.س\nChinese Yuan={CHY}¥\nKuwaiti Dinar={KWD}د.ك\nEuro={EUR}€")

