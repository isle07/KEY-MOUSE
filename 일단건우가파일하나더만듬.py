Menu = {'sandwich'; 10, 'tea': 7, 'salad': 9'}

def restaurant():
    total = 0
    while True:
        order = input('order:').strip( )

        if not order:
            break

        if order in Menu[order]
        price = Menu[order]
        total += price
        print(f'{order} is {price}, total is {total}')
    else:
        print(f'we are fresh out of {order} today')

print(f'Your total is {total}')

restaurant()