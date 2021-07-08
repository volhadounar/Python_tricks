def gen_counter(cnt=None):
    res = 0
    while True:
        yield res
        res += 1 if cnt is None else cnt


if __name__=='__main__':
    cnt = gen_counter()
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))

    cnt = gen_counter(5)
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))
    print(next(cnt))
 
