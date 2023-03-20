class Book:
    def __init__(self, title, autor, price, stock, book_id):
        self.title = title
        self.autor = autor
        self._price = price
        self.stock = stock
        self.book_id = book_id
        
    def get_info(self):
        return f"Titulo: {self.title}\nAutor: {self.autor}\nPrecio: {self._price}\nStock: {self.stock}\nID: {self.book_id}\n"
    
    def get_title(self):
        return self.title
    def set_title(self, new_title):
        self.title = new_title
        
    def get_autor(self):
        return self.autor
    def set_autor(self, new_autor):
        self.autor = new_autor
        
    def get_price(self):
        return self._price
    def set_price(self, new_price):
        if new_price < 0:
            print("No puede ser un precio igual o menor a 0")
        else:
            self._price = new_price
    
    def get_stock(self):
        return self.stock
    def set_stock(self, new_stock):
        if new_stock < 0:
            print("No puede ser un stock igual o menor a 0")
        else:
            self._price = new_stock




# instanciar
bookOne = Book("IT", "Steven Spilberg", 500, 40, 117)
bookTwo = Book("Harry Potter", "J.K. Rowlling", 100, 10, 16)

# print(bookOne.title)
# print(bookOne.autor)
print(bookOne.get_info())

# print(bookTwo.title)
# print(bookTwo.autor)
print(bookTwo.get_info())
bookTwo.set_title("el señor de los anillos")
print(bookTwo.get_info())


# extiende/hereda de la clase book
class Comic(Book):
    def __init__(self, title, autor, price, stock, book_id, vol, ilustrador):
        super().__init__(title, autor, price, stock, book_id)
        self.vol = vol
        self.ilustrador = ilustrador
    
    def get_info(self):
        info = super().get_info()
        return f"{info}volumen: {self.vol}\nIlustradores: {self.ilustrador}"



comicOne = Comic("Batman", "Bill Finger", 1000, 30, 18, 1, "Ilustrador ilustre")
print(comicOne.get_info())