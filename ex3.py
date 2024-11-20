from cpmpy import Model, boolvar


def main():
    """
    Exercise 1
    """
    values = [6000, 4000, 1000, 1500, 800, 1200, 2000, 2200, 900, 3800, 2900, 1300, 800, 2700, 2800]
    budget = [35, 34, 26, 12, 10, 18, 32, 11, 10, 22, 27, 28, 16, 29, 22]
    personnel = [5, 3, 4, 2, 2, 2, 4, 1, 1, 5, 3, 2, 2, 4, 3]
    assert len(values) == len(budget) == len(personnel)
    N = len(values)

    projects = boolvar(shape=N, name="projects")

    model = Model(
        sum(projects) <= 9,
        sum(projects * budget) <= 225,
        sum(projects * personnel) <= 28
    )

    # not_with = [10, None, None, None, 6, 5, None, None, None, 1, 15, None, None, None, 11]
    # require = [None, None, 15, 15, None, None, None, 7, None, None, None, None, 2, 2, None]
    # assert len(not_with) == len(require) == N
    #
    # for i in range(N):
    #     if not_with[i] is not None:
    #         model += projects[i].implies(~projects[not_with[i]-1])
    #     if require[i] is not None:
    #         model += projects[i].implies(projects[require[i]-1])

    print(model)
    model.maximize(sum(projects * values))
    if not model.solve():
        raise
    print("Use project: ", projects.value())
    print("Final value: ", sum(projects.value() * values))


if __name__ == "__main__":
    main()
