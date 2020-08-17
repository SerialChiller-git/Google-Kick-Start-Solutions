
def main() -> str:
    def check_peak(c=0) -> int:
        for i in range(n):    
            try:
                if i != 0 and arr[i] > arr[i+1] and arr[i] > arr[i-1]:
                    c += 1
            except IndexError:
                pass
        return c
    for t in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()[:n]))
        
        
        print("Case #{}: {}".format(t+1,check_peak()))
main()
