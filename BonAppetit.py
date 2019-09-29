from Calculate import bonAppetit

print("https://www.hackerrank.com/challenges/bon-appetit/problem")

nk = input().rstrip().split()

n = int(nk[0])

k = int(nk[1])

bill = list(map(int, input().rstrip().split()))

b = int(input().strip())

bonAppetit(bill, k, b)