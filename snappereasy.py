print('\n'.join((lambda s: f'Case #{i+1}: {s}')((lambda n,k: 'ON' if k >= n and bin(k)[-n:] == '1'*n else 'OFF')(*map(int,input().split()))) for i in range(int(input()))))

