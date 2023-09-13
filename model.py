# HERE I IN THIS IN THIS DATABASE MODELS FOR BOOKS, MEMBERS AND TRANSCATION.

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    stock = db.Column(db.Integer, default=0)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    outstanding_debt = db.Column(db.Float, default=0)

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    return_date = db.Column(db.Date, nullable=True)
    fee = db.Column(db.Float, default=0)
