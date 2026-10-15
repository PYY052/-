class Book:
    def __init__(self,title,author,isbn,publisher,publication_data,page_count,category,stock,price,description):
        self.title=title
        self.author=author
        self.isbn=isbn
        self.publisher=publisher
        self.publication_data=publication_data
        self.page_count=page_count
        self.category=category
        self.stock=stock
        self.price=price
        self.description=description

    def book_dict(self):
        return{"Title":self.title,"Author":self.author,"ISBN":self.isbn,"Publisher":self.publisher,
                "Publication_data":self.publication_data,"Page_count":self.page_count,"Category":self.category,
                "Stock":self.stock,"Price":self.price,"Description":self.description}


class Manage:
    def __init__(self,book_list):
        self.book_list=book_list

    def add_book(self,book):
        self.book_list.append(book.book_dict())
        return self.book_list

    def remove_book(self,isbn):
        self.book_list=[book for book in self.book_list if book["ISBN"]!=isbn]
        return self.book_list

    def search_books(self,query):
        outcome=[]
        for book in self.book_list:
            if query in book:
                outcome.append(book)
        return outcome

    def update_book(self,isbn,updates):
        for i in range(len(self.book_list)):
            if self.book_list[i]["ISBN"]==isbn:
                self.book_list[i]=updates
        return self.book_list

    def display_books(self):
        print(self.book_list)

if __name__ == "__main__":
    book1=Book("西游记","吴承恩","1","慎海雄","中国古籍出版社",668,"小说",12,99.5,"四大名著之一，讲述唐僧师徒四人西天取经的故事")
    book2=Book("水浒传","施耐庵","2","慎海雄","中国古籍出版社",987,"小说",10,102.3,"四大名著之一，讲述108好汉被逼上梁山的故事")
    book3=Book("三国演义","罗贯中","3","慎海雄","中国古籍出版社",888,"小说",20,99.1,"讲述东汉末年天下打乱，诸侯混战，形成三国鼎立之势的兴衰故事")
    book4=Book("红楼梦","曹雪芹","4","慎海雄","中国古籍出版社",1003,"小说",32,100,"讲述宝黛爱情和四大家族兴衰的故事")
    #print(book1.book_dict())
    book_list=[]
    M1=Manage(book_list)

    M1.add_book(book1)
    M1.add_book(book2)
    M1.add_book(book3)
    M1.add_book(book4)
    M1.display_books()

    M1.remove_book("2")
    M1.display_books()

    M1.update_book("4",{'Title': '西游记', 'Author': '吴承恩', 'ISBN': '1', 'Publisher': '慎海雄', 'Publication_data': '中国古籍出版社', 'Page_count': 668, 'Category': '小说', 'Stock': 12, 'Price': 99.5, 'Description': '四大名著之一，讲述唐僧师徒四人西天取经的故事'})
    M1.display_books()

    #print(M1.search_books("西游记"))




