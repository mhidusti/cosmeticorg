def manage_computers(n, m, requests):
    computers = [False] * n

    for request in requests:
        s, l = request
        allocated = False

        for i in range(n - l + 1):
            if all(not computers[i+j] for j in range(l)):
                for j in range(l):
                    computers[i+j] = True
                allocated = True
                print("Yes")
                break

        if not allocated:
            print("No")

n = int(input("Enter the number of computers: "))
m = int(input("Enter the number of groups: "))

requests = []
print("Enter the requests in the format s l:")
for _ in range(m):
    s, l = map(int, input().split())
    requests.append((s, l))

manage_computers(n, m, requests)