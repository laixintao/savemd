from  extractor import Extractor

if __name__ == '__main__':
    ext = Extractor()
    text = ext.getPlainText("http://news.ifeng.com/a/20160819/49807163_0.shtml")
    print(text)