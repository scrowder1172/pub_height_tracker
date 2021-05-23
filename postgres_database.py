import sys
import psycopg2
import os


class PgDatabase:

    def _connect(self):
        """
        DATABASE_URL is an environment variable that points to the postgres instance
        example: postgres://username:password@host:port/database
        Additional error handling should be added in case DATABASE_URL does not exist
        """
        database_url = os.environ.get('DATABASE_URL')
        self.conn = psycopg2.connect(database_url)

    def alter_data(self, sql, parm):
        """
        Executes insert, update, delete commands against database
        :param sql: provide SQL statement in postgres format for parameters
        :param parm: provide parameters for SQL statement as list
        :return: report back if command fails or succeeds
        """
        self._connect()
        result = False
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql, parm)
            self.conn.commit()
            result = True
        except (Exception, psycopg2.DatabaseError) as error:
            sys.stderr.write(f"DATABASE ERROR: {str(error)}")
        except:
            error = sys.exc_info()[0]
            sys.stderr.write(f"DATABASE ERROR: {str(error)}")
        return result

    def select_one(self, sql, parm=None):
        """
        Reads the database and returns one value
        :param sql: provide SQL statement in postgres format for parameters
        :param parm: provide parameters for SQL statement as list
        :return: results from query
        """
        self._connect()
        search_results = ""
        try:
            cursor = self.conn.cursor()
            if parm:
                cursor.execute(sql, parm)
            else:
                cursor.execute(sql)
            result = cursor.fetchone()
            if result:
                search_results = result[0]
        except (Exception, psycopg2.DatabaseError) as error:
            sys.stderr.write(f"DATABASE ERROR: {str(error)}")
        except:
            error = sys.exc_info()[0]
            sys.stderr.write(f"DATABASE ERROR: {str(error)}")
        return search_results

    def select_all(self, sql, parm=None):
        """
        Reads the database and returns all values
        :param sql: provide SQL statement in postgres format for parameters
        :param parm: provide parameters for SQL statement as list
        :return: results from query
        """
        self._connect()
        search_results = ""
        try:
            cursor = self.conn.cursor()
            if parm:
                cursor.execute(sql, parm)
            else:
                cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                search_results = f"{search_results}{row}\n"
        except (Exception, psycopg2.DatabaseError) as error:
            sys.stderr.write(f"DATABASE ERROR: {str(error)}")
        except:
            error = sys.exc_info()[0]
            sys.stderr.write(f"DATABASE ERROR: {str(error)}")
        return search_results


if __name__ == '__main__':
    db = PgDatabase()
    insert_sql = "insert into height_tracker(added_by,height) values(%s, %s)"
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
    select_sql = "select added_by,height from height_tracker where added_by like %s"
    inputs = ['B%']
    print(db.select_all(sql=select_sql, parm=inputs))
