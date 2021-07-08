def chocolate(bars, total):
    bars = sorted(bars, reverse=True)
    curr_cnt = 0
    for bar in bars:
        curr_cnt += bar
        if curr_cnt <= total:
            yield bar
        else:
            curr_cnt -= bar      



if __name__=='__main__':
    choco = chocolate(bars=[1, 2, 6, 7, 9, 3], total=12)
    print(next(choco))
    print(next(choco))
    print(next(choco))
