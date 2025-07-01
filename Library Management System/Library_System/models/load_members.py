from models.member import Member
from utils.db import get_connection

def load_members(library):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT member_id, name, borrowed_books FROM members")
    rows = cursor.fetchall()
    for member_id, name, borrowed_books in rows:
        member = Member(member_id, name)
        if borrowed_books:
            member.borrowed_books = [int(b) for b in borrowed_books.split(",") if b]
        library.members.append(member)
    conn.close()
