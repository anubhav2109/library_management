def list_members(library):
    try:
        for member in library.members:
            print(f"[{member.member_id}] {member.name} - Borrowed: {member.borrowed_books}")
    except Exception as e:
        from utils.logger import log
        log(f"Error listing members: {e}")
