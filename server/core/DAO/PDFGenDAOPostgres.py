import pg8000


class PDFGenDAOPostgres:
    _connect = None

    def __init__(self, user, password, database):
        # conn = pg8000.connect(user="postgres", password="smith620695", database="form")
        self.conn = pg8000.connect(user=user, password=password, database=database)

    def __del__(self):
        self.conn.close()

    def get_question(self, id_meeting):
        cursor = self.conn.cursor()
        cursor.execute("select sequence_no, question  from question where id_meeting = " + str(id_meeting) + " order by question asc")
        result = cursor.fetchall()
        cursor.close()

        return result