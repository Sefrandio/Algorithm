def hanoi(n):
    limit = 2**n-1
    arr = [x for x in range(n,0,-1)]
    arr2 = []
    arr3 = []
    if n%2==0:
        target, aux = arr2,arr3
    else:
        target,aux = arr3,arr2
    capture = f'{arr} {arr2} {arr3}'
    def move(arr,target):
        if not arr:
            arr.append(target.pop())
        elif not target:
            target.append(arr.pop())
        elif arr[-1]<target[-1]:
            target.append(arr.pop())
        else:
            arr.append(target.pop())

    for x in range(1,limit+1):
        if x%3 == 1:
            move(arr,target)
        if x%3 == 2:
            move(arr,aux)
        if x%3 == 0:
            move(aux,target)
        capture += f'\n{arr} {arr2} {arr3}'
    return capture
        

print(hanoi(2))