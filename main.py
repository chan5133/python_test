def in_autotests_we_trust(a, b):
    if a == b:
        print('YES')
    else:
        print('NO')

in_autotests_we_trust(10, '10')

in_autotests_we_trust(0, False)