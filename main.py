#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

#print kata sambutan
print("Welcome to the tip calculator!")
#inputan untuk bill yang sudah diubah menjadi float
bill = float(input("What was the total bill? "))
#inputan untuk tip dan people yang sudah diubah jadi int
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

#perhitungan tip sebagai percent
tip_as_percent = tip / 100
#total tip
total_tip_amount = bill * tip_as_percent
#total bayar
total_bill = bill + total_tip_amount
#total bayar per orang
bill_per_person = total_bill / people

#jumlah akhir perorang menggunakan round
final_amount = round(bill_per_person, 2)

#atau kita dapat menggunakan suatun format yang bisa langsung mengubah hasil bill per person ke string
#final_amount = "{:.2f}".format(bill_per_person)

#print atau di tampilkan menggunakan f-string
print(f"Each person should pay: ${final_amount}")