# ルートから順に親要素が子要素以下か確認していく。
def is_min_heap(array):
    # 葉は子ノードをもたないからチェックする必要がない。つまり、(配列の要素数)/2を切り捨てた整数までを走査する。
    i_max_range = len(array) // 2
    for i in range(i_max_range): #葉以外のノードにアクセスするイテレーター
        # iでアクセスしたノードの子ノードは左：2*i+1,右：2*i+2でアクセスできる。
        parent = array[i]
        left_child = array[2*i+1]
        # 要素数が奇数の時は最後の右の子ノードが存在しない。その時、存在しない子ノードの代わりに親要素を入れる。
        right_child = array[2*i+2] if 2*i+2 < len(array) else parent
        if parent > left_child or parent > right_child: #もし子ノードより大きい時はminヒープではない
            return False
    # 走査が全て終了するとminヒープであることが確認できる。
    return True

if __name__ == '__main__':
    array = [1,2,4,4,2,3]
    if is_min_heap(array):
        print('true')
    else:
        print('false')