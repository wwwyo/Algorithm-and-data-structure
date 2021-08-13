# (2)(a)(i)より(n! mod p)を求める関数
def surplusFractorial(n, p):
    if n >= p:
        return 0
    ans = 1
    for x in range(2, n+1):
        ans = (ans * x) % p
    return ans

# 与えられた式より(a**k mod p)を求める関数
def surplusPower(a, k, p):
    if k == 0:
        return 1
    elif k % 2 == 0:
        d = surplusPower(a, k/2, p)
        return (d * d) % p
    elif k %2 != 0:
        return (a * surplusPower(a, k-1, p)) % p

# (nCr mod p)を求める関数
# n, rを引数に受け取る
def nCr_modP(n, r, p = 100_000_007):
    #  (n! mod p)
    a = surplusFractorial(n, p)
    #  (r! mod p)
    b = surplusFractorial(r, p)
    #  ((n-r)! mod p)
    c = surplusFractorial(n-r, p)

    # {(r! mod p) ((n-r)! mod p)} ** (p-2) mod p
    # つまり{(b) * (c)} ** (p-2) mod p
    d = surplusPower(b * c, p-2, p)

    # [(n! mod p) {(r! mod p) ((n-r)! mod p)} ** (p-2) mod p]をpで割ったあまり
    # つまり[(a) * (d)] % p
    ans = (a * d) % p
    return ans



if __name__ == '__main__':
    print(nCr_modP(1000, 400))


# https://qiita.com/derodero24/items/91b6468e66923a87f39f
# def cmb(n, r, mod):
#     if ( r<0 or r>n ):
#         return 0
#     r = min(r, n-r)
#     return g1[n] * g2[r] * g2[n-r] % mod

# mod = 10**8+7 #出力の制限
# N = 100000
# g1 = [1, 1] # 元テーブル
# g2 = [1, 1] #逆元テーブル
# inverse = [0, 1] #逆元テーブル計算用テーブル

# for i in range( 2, N + 1 ):
#     g1.append( ( g1[-1] * i ) % mod )
#     inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
#     g2.append( (g2[-1] * inverse[-1]) % mod )

# print(cmb(1000,400,mod))