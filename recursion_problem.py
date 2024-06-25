import matplotlib.pyplot as plt

def rec_calc_helper(x, n, iterations, arr, A, B, C, E):
    if n != iterations:
        result = round((A * x * x + B * x + C) / (x + E), 6)
        arr[n] = result
        return rec_calc_helper(result, n + 1, iterations, arr, A, B, C, E)

 
def rec_calc(x, iterations):
    arr = [None] * iterations
    arr[0] = x
    # input for a, b, c, d , e
    print('(A * x * x + B * x + C) / (x + E)')
    A = int(input('A = '))
    B = int(input('B = '))
    C = int(input('C = '))
    E = int(input('E = '))
    print(f'({A} * x * x + {B} * x + {C}) / (x + {E})')
    rec_calc_helper(x, 1, iterations, arr, A, B, C, E)
    return arr


#iterations = int(input('Enter amount of iterations: '))
iterations=20
starting_point = float(input('Enter starting point: '))



data = rec_calc(starting_point, iterations)
#print(data)
plt.plot(data, 'bo-', label='Data Points')


plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Plot of Given Data Array')

plt.grid(True)
plt.legend()
plt.show()
    