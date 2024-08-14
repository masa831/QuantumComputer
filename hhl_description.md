# hhl

## メモ

正規化係数とHHLの成功率について  
HHLアルゴリズムでは、最終的に補助ビットの観測結果に応じた量子状態が求めるものとなります。

以下に測定前の最終的な量子状態の補助ビット部分を抜粋する。
$$
\sum^{n-1}_{i=0} \sqrt{1 - (\frac{C}{\lambda_i})^2} \ket{0} + \frac{C}{\lambda_i} \ket{1}
$$

この状態の$\ket{1}$の状態を観測できたときに、解となるので、$\frac{C}{\lambda}$の値がなるべく大きくとりたい。
ただし、$\lambda$は、行列Aの固有値なので、以下の条件が必要となる
$$
C < min(|\lambda|)
$$

参考：<https://qiita.com/notori48/items/9e0e7b89db9479f10eb2>

## TODO

行列Aのスパース性と計算量について、確認する

比較対象の共役勾配法を確認する。

QPE：固有値が複数ある場合、結果の確率はすべて同様のバランスなのか？ある条件でばらつくのか？

固有値逆回転の箇所を改良したい
→QPEの結果(プラス、マイナスどちらも考慮する)と行列Aから、固有値を確定させることが可能か？
→行列Aから最小固有値を特定できないか？

HHL原論文  
<https://arxiv.org/abs/0811.3171>

レビュー論文  
<https://arxiv.org/abs/1802.08227>

内容を把握する＋T=150の理由を確認する
<https://github.com/tybens/quantum-data-fitting-HHL>

qiskit_v0のaquaのgithubから固有値特定ロジックを確認する  
<https://github.com/qiskit-community/qiskit-aqua/blob/stable/0.9/qiskit/aqua/algorithms/linear_solvers/hhl.py>

## 参考URL

参考プログラムあり  
<https://github.com/tybens/quantum-data-fitting-HHL>

理論を細かく追ってくれている  
<https://wayama.io/rec/qiskit/hhl/>

<https://dojo.qulacs.org/ja/latest/notebooks/7.2_Harrow-Hassidim-Lloyd_algorithm.html#%E5%8F%82%E8%80%83%E6%96%87%E7%8C%AE>

スケーリング係数Cについての考察が参考になる  
<https://qiita.com/notori48/items/9e0e7b89db9479f10eb2>

qiskitのサンプルコード
<https://github.com/Qiskit/textbook/blob/main/translations/ja/ch-algorithms/quantum-phase-estimation.ipynb>

<https://github.com/Qiskit/textbook/blob/main/translations/ja/ch-applications/hhl_tutorial.ipynb>
