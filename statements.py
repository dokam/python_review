x = int(input("Please an integer:"))

if x < 0:
    x = 0
    print("When negative it's changed to zero.")
elif x == 0:
    print('Zero.')
elif x == 1:
    print('Single.')
else:
    print('More.')

print('\n')

words = ['Cats', 'Dogs', 'Horses']
for w in words:
    print(w, len(w))

print('\n')

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print(users)

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
print(active_users)

# the range function
for i in range(5):
    print(i)

print(list(range(5, 10)))
print(list(range(1, 10, 2)))
print('\n')

a = ['Fusca', 'Polo', 'Golf', 'Passat']
for i in range(len(a)):
    print(i, a[i])

print('\n')
# iterable
print(sum(range(4)))
