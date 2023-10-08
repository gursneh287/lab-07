histogram = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0}

while True:
    user_input = int(input("Enter a number (1-10, -1 to exit): "))
    
    if user_input == -1:
        break
    
    if 1 <= user_input <= 10:
        histogram[user_input] += 1
    else:
        print("Invalid input. Enter a number in the range 1-10.")

for start, end in [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]:
    count = sum(histogram[i] for i in range(start, end + 1))
    if (sum(histogram.values()))!=0:
        percentage = (count / sum(histogram.values())) * 100 
    else:
        percentage = 0
    print(f"{start} - {end}: {' # ' * count} {percentage:.2f} %")


# def histogram():
#     print("Enter numbers between 1 and 10. Type -1 to stop.")
#     counts = [0]*10
#     total = 0
#     while True:
#         num = int(input())
#         if num == -1:
#             break
#         elif 1 <= num <= 10:
#             counts[num-1] += 1
#             total += 1

#     print("Histogram:")
#     for i in range(0, 10, 2):
#         percentage = round(sum(counts[i:i+2]) / total * 100, 2)
#         print(f"{i+1} - {i+2}: {'#'*counts[i]} {'#'*counts[i+1]} {percentage} %")

# histogram()