from itertools import zip_longest


def version_compare_eq(v1, v2):
    v1 = v1.split('.')
    v2 = v2.split('.')
    try:
        for a, b in zip_longest(v1, v2, fillvalue='0'):
        # second value = case for versions like 1.4.0 and 1.4
            if int(a) != int(b):
                return False
        return True
    except Exception as e:
        return False


def version_compare_lt(v1, v2):
    if version_compare_eq(v1, v2):
        return False
    v1 = v1.split('.')
    v2 = v2.split('.')
    try:
        for a, b in zip_longest(v1, v2, fillvalue='0'):
            if int(a) > int(b):
                return False
        return True
    except Exception as e:
        return False


def version_compare_gt(v1, v2):
    return not version_compare_lt(v1, v2) and not version_compare_eq(v1, v2)


def version_to_sortkey(v):
    """
    Version limits:
        'a.b.c.d' , where a < 2^5
    """
    MAX_SIZE = 4
    MAX_VERSION_SIZE_2_POW = 5
    v = v.split('.')
    res = 0
    for (ind, val) in enumerate(v):
        res += int(val) << ((MAX_SIZE - ind) * MAX_VERSION_SIZE_2_POW)
    return res
