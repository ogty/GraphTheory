
# 定義1 : 集合とは

集合：異なるものの集まり  

Pythonには組み込み関数として`set()`が用意されている。これは集合という意味であり、データは`{}（波括弧）`に囲われて表現される。また`set()`されたデータは一意に扱われる。

```python
X = {"a", "b", "c"}
print(type(X))
# <class 'set'>

Y = ["a", "a", "b", "c"]
print(set(Y))
# {"a", "b", "c"}
```

上記のように配列`Y`に`a`が2つ含まれている、つまり重複している場合は`set()`により一意なデータとして変換される。ここで集合に格納された値のことを**要素**、あるいは**元**という。ここでは「`a`, `b`, `c`」が要素である。また、要素が一つもないことを**空集合**といい、要素数が有限の場合は**有限集合**、無限の場合は**無限集合**と呼ぶ。

集合は`X = {1, 2, 3, 4}`のように要素を表現することもあるが、要素の性質を用いて`X = {x|xは4以下の自然数}`と表すこともできる。Pythonで表すとおおよそ以下で正しいだろう。また**n元集合**とは要素数をnとした時の有限集合のことである。
```python
X = {1, 2, 3, 4}
X = lambda x: True if x <= 4 else False
```

### 用語
 - 集合
 - 要素 or 元
 - 空集合
 - 有限集合
 - 無限集合
 - n元集合 