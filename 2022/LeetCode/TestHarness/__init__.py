__BASE_MSG = "Expected `{0}` but got `{1}`"


def _run_solution(
    sf,
    args,
    expected=None,
    msg=__BASE_MSG,
    input_transform_func=None,
    output_transform_func=None,
    expected_transform_func=None,
):
    print(f"\n\n----- test: {sf.__name__}({', '.join(map(str, args))}) => {expected}")
    if input_transform_func is not None:
        args = input_transform_func(*args)

    res = sf(*args)

    if output_transform_func is not None:
        res = output_transform_func(res)

    return res


def _complete_test():
    print("Completed test case.")


def map_to_tuple_set(l):
    return set(map(tuple, l))


def map_to_set(l):
    return set(l)


def check_solution_simple(
    sf,
    args,
    expected=None,
    msg=__BASE_MSG,
    input_transform_func=None,
    output_transform_func=None,
    expected_transform_func=None,
):
    res = _run_solution(
        sf,
        args,
        expected,
        msg,
        input_transform_func,
        output_transform_func,
        expected_transform_func,
    )

    if expected_transform_func is not None:
        expected = expected_transform_func(expected)

    assert res == expected, msg.format(expected, res)

    _complete_test()


def check_solution_as_sets(
    sf,
    args,
    expected=None,
    msg=__BASE_MSG,
    input_transform_func=None,
    output_transform_func=None,
    expected_transform_func=None,
    output_set_transform=map_to_set,
    expected_set_transform=map_to_set,
):
    res = _run_solution(
        sf,
        args,
        expected,
        msg,
        input_transform_func,
        output_transform_func,
        expected_transform_func,
    )

    assert len(res) == len(
        expected
    ), f"Expected outut len {len(expected)} but got {len(res)}. Expected: {expected} Result: {res}"

    # https://stackoverflow.com/questions/6105777/how-to-compare-a-list-of-lists-sets-in-python
    rset = output_set_transform(res)
    eset = expected_set_transform(expected)

    diff = rset.symmetric_difference(eset)

    if len(diff) > 0:
        print(f"r: {rset} v e: {eset}")

    assert (
        len(diff) == 0
    ), f"Expected no differences, but got {len(diff)}:{diff} vs {len(eset)}:{eset}"

    _complete_test()
