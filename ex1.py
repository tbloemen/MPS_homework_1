from cpmpy import Model, intvar


def sendmoremoney(s, e, n, d, m, o, r, y):
    model = Model(
        s * e * n * d + m * o * r * e == m * o * n * e * y
    )

    print(model)
    model.solve()
    for letter in [s, e, n, d, m, o, r, y]:
        print(letter.name, letter.value())


def sendmostmoney(s, e, n, d, m, o, t, y):
    model = Model(
        s * e * n * d + m * o * s * t == m * o * n * e * y
    )

    money = intvar(0, 1000, name="money")
    model += (
        money == sum([m, o, n, e, y])
    )
    model.maximize(money)

    print(model)
    model.solve()
    for letter in [s, e, n, d, m, o, s, t, y, money]:
        print(letter.name, letter.value())


def main():
    """
    Exercise 1
    """
    s = intvar(1, 9, name="S")
    e = intvar(0, 9, name="E")
    n = intvar(0, 9, name="N")
    d = intvar(0, 9, name="D")
    m = intvar(1, 9, name="M")
    o = intvar(0, 9, name="O")
    r = intvar(0, 9, name="R")
    y = intvar(0, 9, name="Y")
    t = intvar(0, 9, name="T")

    sendmoremoney(s, e, n, d, m, o, r, y)
    sendmostmoney(s, e, n, d, m, o, t, y)


if __name__ == "__main__":
    main()
