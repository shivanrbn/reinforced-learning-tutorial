# define start values
x, v, a = 0, 0, 0
def step(input):
    a = input
    v = v + a
    x = x + v
while True:
    input = get_input()
    step(input)