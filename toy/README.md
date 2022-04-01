## src/string_similarity.py
### sample codes using a few methods.
- 文字列の類似度を評価するために，以下の3つの手法を用いた
  - ゲシュタルトアプローチによる類似度評価
  - zlib compressによる圧縮した文字列データの類似度評価
  - レーベンシュタイン距離による類似度評価

```python
# サンプル文字列
str1 = 'How to train a deep neural network (DNN) using PyTorch or Tensorflow.'
str2 = 'How to train a convolutional neural network (CNN) using PyTorch or Tensorflow.'

# 文字列の類似度
gestalt_value = gestalt_approach_matcher(sx=str1, sy=str2)
compress_value = zlib_compress_matcher(sx=str1, sy=str2)
levenshtein_value = levenshtein_distance_matcher(sx=str1, sy=str2)

print('ゲシュタルトアプローチによる類似度評価: ', gestalt_value)
> ゲシュタルトアプローチによる類似度評価:  0.8707482993197279

print('圧縮した文字列データの類似度評価: ', compress_value)
> 圧縮した文字列データの類似度評価:  0.7625

print('レーベンシュタイン距離による類似度評価: ', levenshtein_value)
> レーベンシュタイン距離による類似度評価:  0.8205128205128205
```
