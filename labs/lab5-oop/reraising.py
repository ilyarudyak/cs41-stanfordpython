try:
    print("in try")
    # (A)
    # raise Exception()
except Exception as exc:
    print("in except")
    # (B)
    # raise Exception()
else:
    print("in else")
    # (C)
    # raise Exception()
finally:
    print("in finally")
    # (D)
    raise Exception()