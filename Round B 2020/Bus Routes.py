
def main() -> str:
    def latest_day(d) -> int:
        for i in s[:: -1]:
            P = d//i
            d = P*i
        return d

    for t in range(int(input())):
        temp1 = list(map(int, input().split()))
        n = temp1[0]
        s = [int(x) for x in input().split()[ :n]]

        print("Case #{}: {}".format(t+1, latest_day(temp1[1])), flush=True)
        
main()
