from flask import Flask, render_template, request, redirect
from models import db, BooksModel

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://sergey:98432412@localhost:5432/books"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Получить главную страницу
@app.route('/')
def home():
    return render_template('home.html', title="Homepage - CRUD books")

# Получить список всех книг
@app.route('/books')
def books():
    bookList = db.session.query(BooksModel).all()
    return render_template('index.html', title="Book list - CRUD books", books=bookList)

# Получить книгу по её Id
@app.route('/book/<int:bookId>')
def getBook(bookId):
    bookQuery = db.session.query(BooksModel).filter(BooksModel.id == bookId).first()
    return render_template('show.html', title="Book " + bookQuery.name + " - CRUD books", book=bookQuery)

# Показать форму создания новой книги
@app.route('/book/create')
def showFormCreateBook():
    return render_template('create.html', title="Create book - CRUD books")

# Создать новую книгу
@app.route('/book', methods=['POST'])
def createBook():
    newBook = BooksModel(request.form['isbn'], request.form['name'], request.form['author'], request.form['pages'], request.form['year'])
    db.session.add(newBook)
    db.session.commit()
    return redirect("/books")

@app.route('/book/update/<int:bookId>')
def showFormUpdateBook(bookId):
    bookQuery = db.session.query(BooksModel).filter(BooksModel.id == bookId).first()
    return render_template('update.html', title="Update book - CRUD books", book=bookQuery)

@app.route('/book/delete/<int:bookId>', methods=['POST'])
def deleteBook(bookId):
    query = db.session.query(BooksModel).filter(BooksModel.id == bookId).first()
    db.session.delete(query)
    db.session.commit()

    return redirect("/books")

@app.route('/book/update/<int:bookId>', methods=['POST'])
def updateBook(bookId):
    book = db.session.query(BooksModel).filter(BooksModel.id == bookId).first()

    book.isbn = request.form['isbn']
    book.name = request.form['name']
    book.author = request.form['author']
    book.pages = request.form['pages']
    book.year = request.form['year']

    db.session.add(book)
    db.session.commit()

    return redirect("/books")

if __name__ == '__main__':
    app.run(debug=True)