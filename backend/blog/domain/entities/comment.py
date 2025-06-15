class Comment:
    def __init__(self, id: str, post_id: str, user_id: str, comment: str, date: str):
        self.id = id
        self.post_id = post_id
        self.user_id = user_id
        self.comment = comment
        self.date = date