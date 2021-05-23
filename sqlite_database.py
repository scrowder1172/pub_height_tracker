import sqlite3
import sys
import traceback


class Database:

    def __init__(self):
        """Initialize the database in memory
        """
        self.database_location = 'height_tracker.db'
        self.db = sqlite3.connect(self.database_location)
        self._create_table()

    def _create_table(self):
        """Create the HEIGHT_TRACKER table in the database
        Error handling has been added to track SQL errors
        """
        try:
            self.db.execute("CREATE TABLE height_tracker (added_by text, height int); ")
        except sqlite3.Error as er:
            if ' '.join(er.args) != "table height_tracker already exists":
                print('SQLite error: %s' % (' '.join(er.args)))
                print("Exception class is: ", er.__class__)
                print('SQLite traceback: ')
                exc_type, exc_value, exc_tb = sys.exc_info()
                print(traceback.format_exception(exc_type, exc_value, exc_tb))
            else:
                print("Table exists. Moving on...")
        except:
            print("Unexpected error:", sys.exc_info()[0])

    def alter_data(self, sql, parm):
        """Adds new data to the table based off supplied parameters
        :param sql: provide SQL statement in postgres format for parameters
        :param parm: provide parameters for SQL statement as list
        :return: number of rows altered
        """
        # function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        # print(f"Starting: {function_name}")
        try:
            cursor = self.db.cursor()
            cursor.execute(sql, parm)
            self.db.commit()
            rows_altered = cursor.rowcount
        except sqlite3.Error as er:
            rows_altered = 0
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        except:
            rows_altered = 0
            print("Unexpected error:", sys.exc_info()[0])

        return rows_altered

    def select_one(self, sql, parm=None):
        """
        Reads the database and returns one value
        :param sql: provide SQL statement in postgres format for parameters
        :param parm: provide parameters for SQL statement as list
        :return: results from query
        """
        # function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        # print(f"Starting: {function_name}")
        search_results = ""
        try:
            cursor = self.db.cursor()
            if parm:
                cursor.execute(sql, parm)
            else:
                cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                search_results = result[0]
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        except:
            search_results = 0
            print("Unexpected error:", sys.exc_info()[0])
        return search_results

    def select_all(self, sql, parm=None):
        """
        Reads the database and returns all values
        :param sql: provide SQL statement in postgres format for parameters
        :param parm: provide parameters for SQL statement as list
        :return: results from query
        """
        # function_name = cast(types.FrameType, inspect.currentframe()).f_code.co_name
        # print(f"Starting: {function_name}")
        search_results = ""
        try:
            cursor = self.db.cursor()
            if parm:
                cursor.execute(sql, parm)
            else:
                cursor.execute(sql)
            result = cursor.fetchone()
            for row in result:
                search_results = f"{search_results}{row}\n"
        except sqlite3.Error as er:
            print('SQLite error: %s' % (' '.join(er.args)))
            print("Exception class is: ", er.__class__)
            print('SQLite traceback: ')
            exc_type, exc_value, exc_tb = sys.exc_info()
            print(traceback.format_exception(exc_type, exc_value, exc_tb))
        except:
            search_results = 0
            print("Unexpected error:", sys.exc_info()[0])
        return search_results


if __name__ == '__main__':
    db = Database()
    insert_sql = "insert into height_tracker(added_by,height) values(?, ?)"
    inputs = ['Eric', 61]
    db.alter_data(sql=insert_sql, parm=inputs)
    inputs = ['Mary', 67]
    db.alter_data(sql=insert_sql, parm=inputs)
    inputs = ['Lucas', 75]
    db.alter_data(sql=insert_sql, parm=inputs)
    inputs = ['Brandon', 49]
    db.alter_data(sql=insert_sql, parm=inputs)
    inputs = ['Barry', 68]
    db.alter_data(sql=insert_sql, parm=inputs)
    select_sql = "select avg(height) from height_tracker"
    print(db.select_one(sql=select_sql))
    select_sql = "select added_by,height from height_tracker where added_by like ?"
    inputs = ['B%']
    print(db.select_all(sql=select_sql, parm=inputs))
