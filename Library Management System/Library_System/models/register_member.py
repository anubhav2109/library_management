from models.member import Member
from utils.logger import log
from utils.db import get_connection

def register_member(library, name):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO members (name, borrowed_books) VALUES (?, '')",
                       (name,))
        conn.commit()
        member_id = cursor.lastrowid
        conn.close()

        member = Member(member_id, name)
        library.members.append(member)
        log(f"Registered member: {name}")
    except Exception as e:
        log(f"Error registering member: {e}")
