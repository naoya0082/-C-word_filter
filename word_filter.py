class WordFilter:
    def __init__(self, my_filter):
        self.my_filter = my_filter

    def detect(self, NG_word):
        return self.my_filter in NG_word

    def censor(self, NG_word):
        return NG_word.replace(self.my_filter, "<censored>")


if __name__ == "__main__":
    my_filter = WordFilter("アーセナル")

    # NGワードが含まれている場合
    my_filter.detect("昨日のアーセナルの試合アツかった！")  # Trueを返す ※出力されるわけではありません！
    # NGワードが含まれていない場合
    my_filter.detect("昨日のリバプールの試合アツかった！")  # Falseを返す ※出力されるわけではありません！

    my_filter.censor("昨日のアーセナルの試合アツかった！")  # "昨日の<censored>の試合アツかった！" を返す ※出力されるわけではありません！
    # NGワードが含まれていない場合
    my_filter.censor("昨日のリバプールの試合アツかった！")  # "昨日のリバプールの試合アツかった！" を返す ※出力されるわけではありません！
