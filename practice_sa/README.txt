使用python完成一个情感分类程序。

方法是：基于情感词表的方法
即：给定一个句子，如果句子中包含若干个情感词，查情感词表，记录褒义词为+1，贬义词为-1，计算这些词相加的结果，结果大于0则是褒义，小于0是贬义，等于0是中性。

需要考虑特殊情况，这里只举一个否定词的例子。
如：这个桌子不结实，“结实”在情感词典中是“+1”，这个句子需要将其翻转。