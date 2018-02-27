# ch_4_ex1 - create program that counts for the user

print("\t\t Hello, let's go ahead and count for you\n\n")

start = int(input("Please input a start number to count from: "))
stop = int(input("Please input a stop number to count to: "))
interval = int(input("Please input the interval that you'd like to count by: "))

if interval > 0:
	stop += 1
elif interval < 0:
	stop -= 1

for i in range(start, stop, interval):
	print(i)

print("\nAll done!")