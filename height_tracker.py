from sqlite_database import Database


class HeightTracker:

    def __init__(self):
        self.db = Database()

    def add_height(self, name, height):
        """Use postgres sql syntax if inserting into postgres database
        sql = "insert into height_tracker(added_by,height) values(%s, %s)"
        """
        sql = "insert into height_tracker(added_by,height) values(?, ?)"
        params = [str(name).capitalize(), height]
        result = self.db.alter_data(sql=sql, parm=params)
        return result

    def average_height(self):
        sql = "select avg(height) from height_tracker"
        result = float(self.db.select_one(sql=sql))
        average = f"Average height: {round(result,2)} inches"
        return average

    def count_of_respondents(self):
        sql = "select count(added_by) from height_tracker"
        result = int(self.db.select_one(sql=sql))
        respondents = f"{result} respondents"
        return respondents


if __name__ == '__main__':
    h = HeightTracker()
    rows_inserted = h.add_height(name='Seth', height=61)
    print(f"{rows_inserted} rows inserted")
    rows_inserted = h.add_height(name='Tony', height=75)
    print(f"{rows_inserted} rows inserted")
    rows_inserted = h.add_height(name='Beth', height=73)
    print(f"{rows_inserted} rows inserted")
    print(h.average_height())
    print(h.count_of_respondents())
