import os
import sys
def fact(a: int, n: int):
    '''permutation factorial, pick n from a by order'''
    x = 1
    for i in range(n):
        x *= (a-i)
    return x

def comb(a: int, n: int):
    '''combination factorial, pick n from a'''
    return fact(a, n) / fact(n, n)


def xhit(deck: int, cx: int, damage: int):
    '''no cancel prob'''
    rest = deck - cx
    return comb(rest, damage) / comb(deck, damage)


def xtop(deck: int, cx: int, x: int, top: int):
    '''x cx in top n'''
    return comb(cx, x) * comb(deck-cx, top-x) / comb(deck, top)


def main():
    def cal(deck: int, cx: int, damage: int):
        a = xhit(deck, cx, 2)
        b = xhit(deck-2, cx, damage)
        c = xtop(deck-2, cx, 1, 2)
        d = xhit(deck-4, cx-1, damage-1)
        e = xtop(deck-2, cx, 2, 2)
        f = xhit(deck-4, cx-2, damage)
        g = xhit(deck-2, cx, 2)
        h = xhit(deck-4, cx, damage-2)
        i = xtop(deck, cx, 1, 1)
        j = xhit(deck-1, cx-1, damage)
        k = xtop(deck-1, cx-1, 1, 2)
        l = xhit(deck-3, cx-2, damage-1)
        p5 = a * (b + c * d + e * f)
        p2 = a * (c * (1-d) + e * (1-f) + g*(1-h))
        p3 = i*(j + k * l + xtop(deck-1, cx-1, 2, 2) * xhit(deck-3, cx-3, damage)) + (xtop(deck, cx, 1, 2)-i)*(b + c * d + e * f)
        '''
        p0 = xtop(deck, cx, 1, 1)* (xtop(deck-1, cx-1, 1, 2) * (1-xhit(deck-3, cx-2, damage-1)) 
                + xtop(deck-1, cx-1, 2, 2) * (1-xhit(deck-3, cx-3, damage)) + xhit(deck-1, cx-1, 2)*(1 - xhit(deck-3, cx-1, damage-2)))
                + (xtop(deck,cx,1,2)-xtop(deck,cx,1,1))*(xtop(deck-2, cx-1, 1, 2) * (1-xhit(deck-4, cx-2, damage-1)) 
                + xtop(deck-2, cx-1, 2, 2) * (1-xhit(deck-4, cx-3, damage)) + xhit(deck-2, cx-1, 2)*(1-xhit(deck-4, cx-1, damage-2)))
        '''
        p0 = 1-(p2+p3+p5)
        return p5,p2,p3,p0

    def cal2(deck: int, cx: int, damage: int):
        a = xtop(deck,cx,1,2)
        b = xhit(deck-3,cx-1,damage)
        c = xtop(deck,cx,2,2)
        d = xhit(deck-4,cx-2,damage)
        e = xtop(deck-2,cx-2,1,1)
        p5 = xhit(deck,cx,2+damage) + a * xhit(deck-2,cx-1, damage+1)+ c * xhit(deck-2, cx-2, 2+damage)

        p2 = xhit(deck,cx,2)*(1-xhit(deck-2,cx,damage)) + a*xhit(deck-2,cx-1,1)*(1-b) + c*xhit(deck-2,cx-2,2)*(1-d)
        p3 = a*xtop(deck-2,cx-1,1,1)*xhit(deck-3,cx-2,damage) + c*(e*xhit(deck-3,cx-3,damage)+(xtop(deck-2,cx-2,1,2)-e)*xhit(deck-4,cx-3,damage))
        p0 = 1-(p2+p3+p5)
        return p5,p2,p3,p0



    deck = input('Enter deck size: ')
    cx = input('Enter cx number: ')
    print('おまたせ！お兄ちゃん！')
    deck,cx = int(deck), int(cx)
    print('Mode: front (3 damage)')
    print('Option: burn 2 first')
    p5,p2,p3,p0 = cal(deck, cx, 3)
    print('P(5 damage): %.2f' % p5)
    print('P(2 damage): %.2f' % p2)
    print('P(3 damage): %.2f' % p3)
    print('P(0 damage): %.2f' % p0)
    total = p5*5+p2*2+p3*3
    print('Total damage: %.2f' % total)
    print('Option: check top first')
    p5,p2,p3,p0 = cal2(deck, cx, 3)
    print('P(5 damage): %.2f' % p5)
    print('P(2 damage): %.2f' % p2)
    print('P(3 damage): %.2f' % p3)
    print('P(0 damage): %.2f' % p0)
    total = p5*5+p2*2+p3*3
    print('Total damage: %.2f' % total)

    print('Mode: side2 (2 damage)')
    print('Option: burn 2 first')
    p5,p2,p3,p0 = cal(deck, cx, 2)
    p2 = p2+p3
    print('P(4 damage): %.2f' % p5)
    print('P(2 damage): %.2f' % p2)
    print('P(0 damage): %.2f' % p0)
    total = p5*4+p2*2
    print('Total damage: %.2f' % total)
    print('Option: check top first')
    p5,p2,p3,p0 = cal2(deck, cx, 2)
    p2 = p2+p3
    print('P(4 damage): %.2f' % p5)
    print('P(2 damage): %.2f' % p2)
    print('P(0 damage): %.2f' % p0)
    total = p5*4+p2*2
    print('Total damage: %.2f' % total)

    print('Mode: direct (4 damage)')
    print('Option: burn 2 first')
    p5,p2,p3,p0 = cal(deck, cx, 4)
    print('P(6 damage): %.2f' % p5)
    print('P(2 damage): %.2f' % p2)
    print('P(4 damage): %.2f' % p3)
    print('P(0 damage): %.2f' % p0)
    total = p5*6+p2*2+p3*4
    print('Total damage: %.2f' % total)
    print('Option: check top first')
    p5,p2,p3,p0 = cal2(deck, cx, 2)
    print('P(6 damage): %.2f' % p5)
    print('P(2 damage): %.2f' % p2)
    print('P(4 damage): %.2f' % p3)
    print('P(0 damage): %.2f' % p0)
    total = p5*6+p2*2+p3*4
    print('Total damage: %.2f' % total)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print("[STOP]", e)

