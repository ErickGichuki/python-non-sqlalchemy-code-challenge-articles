class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        if not isinstance(title, str):
            raise Exception('The title must be of type str')
        if not(5<= len(title) <= 50):
            raise ValueError('It is a requirement that the title be between 5 and 50 characters')
        Article.all.append(self)
       
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception('The name should be of type str')
        if (len(name) <= 0):
            raise Exception('The length of the name should be greater than zero!')
        
        self._name = name
    @property
    def name(self):
        return self._name
    
    def articles(self):
        return [my_articles for my_articles in Article.all if my_articles.author == self]


    def magazines(self):
        return list(set(my_loshy.magazine for my_loshy in self.articles()))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
       return list(set(fay.category for fay in self.magazines())) if self.magazines() else None
               

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Names must be of type str")
        if not(2 <= len(name) <= 16):
            raise ValueError("names must be between 2 and 16 characters!")
        self._name =name
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise Exception('Must be a string')
        if (len(category) == 0):
            raise ValueError('not possible to have an empty category')
        self._category = category

    def articles(self):
        return [my_article for my_article in Article.all if my_article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in self.articles()))

    def article_titles(self):
        articles = self.articles()
        return [my_article.title for my_article in articles] if articles else None

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles():
            author = article.author
            if author not in author_counts:
                author_counts[author] = 1
            else:
                author_counts[author] += 1
        contributing_authors = [author for author, count in author_counts.items() if count > 2]
        return contributing_authors if contributing_authors else None