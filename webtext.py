import requests
from bs4 import BeautifulSoup
def extract_text(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取网页中的所有文本内容
    text = soup.get_text()
    
    # 去除文本内容中的空白字符和换行符
    text = text.strip().replace('\n', ' ')
    
    return text

def extract_text(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 提取网页中的所有文本内容
    text = soup.get_text()
    
    # 去除文本内容中的空白字符和换行符
    text = text.strip().replace('\n', ' ')
    
    # 对文本进行分词
    words = text.split()
    
    # 删除停用词和标点符号
    stopwords = ['a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'in', 'on', 'at', 'to', 'from', 'with', 'by', 'about', 'like', 'as', 'into', 'of', 'for', 'inherent']
    filtered_words = [word for word in words if word not in stopwords]
    
    # 将文本转换为小写并连接成字符串
    filtered_text = ' '.join(filtered_words).lower()
    
    return filtered_text

def extract_text(url):
    # 发送HTTP请求获取网页内容
    response = requests.get(url)
    # 使用BeautifulSoup解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')
    # 提取网页中的所有文本内容
    text = soup.get_text()
    # 去除文本内容中的空白字符和换行符
    text = text.strip().replace('\n', ' ')
    # 对文本进行分词
    words = text.split()
    # 删除停用词和标点符号
    stopwords = ['a', 'an', 'the', 'and', 'or', 'but', 'is', 'are', 'in', 'on', 'at', 'to', 'from', 'with', 'by', 'about', 'like', 'as', 'into', 'of', 'for', 'inherent']
    filtered_words = [word for word in words if word not in stopwords]
    # 将文本转换为小写并连接成字符串
    filtered_text = ' '.join(filtered_words).lower()
    # 进行词干提取和词形还原
    from nltk.stem import WordNetLemmatizer, SnowballStemmer
    from nltk.tokenize import word_tokenize
    stemmer = SnowballStemmer("english")
    lemmatizer = WordNetLemmatizer()
    stemmed_words = [stemmer.stem(word) for word in word_tokenize(filtered_text)]
    lemmatized_words = [lemmatizer.lemmatize(word) for word in stemmed_words]
    # 构建关键词词典
    keywords = {}
    for word in lemmatized_words:
        if word not in keywords:
            keywords[word] = 1
        else:
            keywords[word] += 1
    # 提取关键词并返回结果
    top_keywords = sorted(keywords.items(), key=lambda x: x[1], reverse=True)
    result = ', '.join([keyword[0] for keyword in top_keywords[:10]])
    return result
