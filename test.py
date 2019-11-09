def test(fun, *args):
    print("".join(['-' for i in range(40)]))
    print(fun.__name__[:-1].upper()+" "+fun.__name__[-1])
    res = fun(*args[:-1])
    if isinstance(args[0], str):
        decoded = "".join([chr(i) for i in args[-1]])
        if res == decoded:
            print("Yes, "+decoded.replace("my","your"))
        else:
            print("No, "+decoded.replace("my","your").replace("has","has not")+" yet")
    else:
        print("Is correct? "+ str(res == args[-1]))
    print( "".join(['-' for i in range(40)]))
