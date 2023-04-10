from psycopg_pool import ConnectionPool
import os
import json
import re

class Db:

  def __init__(self):
    self.init_pool()
  
  def init_pool(self):
    connection_url = os.getenv("CONNECTION_URL")
    self.pool = ConnectionPool(connection_url)
  
  def query_commit(self,sql,params):
    print("SQL STATEMENT [commit with returning ID]---------------")
    print(sql)
    pattern = r"\bRETURNING\b"
    is_returning_id = re.search(pattern, sql)

    try:
      with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql,params)
          if is_returning_id:
            returning_id = cur.fetchone()[0]
            conn.commit()
          if is_returning_id:
            print("returning_id -----------------------------")
            print(returning_id)
            return returning_id
    except Exception as error:
      self.print_sql_err(error)
      #conn.rollback()
    finally:
      if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')


  def query_commit1(self,sql):
    print("SQL STATEMENT---------------")
    print(sql)
    try:
      with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(sql)
          conn.commit()
    except Exception as error:
      self.print_sql_err(error)
      #conn.rollback()
    finally:
      if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')
  
  def query_object_json(self,sql):
    print("SQL STATEMENT---[Object]------------")
    print(sql)
    wrapped_sql = self.query_wrap_object(sql)
    try:
      conn = self.pool.connection() 
      cur = conn.cursor() 
      cur.execute(wrapped_sql)
      json = cur.fetchone()
      return json[0]
    except Exception as error:
      self.print_sql_err(error)
      #conn.rollback()
    finally:
      if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')
    
  
  def query_array_json(self,sql):
    print("SQL STATEMENT---[Array]------------")
    print(sql)
    wrapped_sql = self.query_wrap_array(sql)
    try:
      with self.pool.connection() as conn:
        with conn.cursor() as cur:
          cur.execute(wrapped_sql)
          json = cur.fetchone()
          return json[0]
    except Exception as error:
      self.print_sql_err(error)
      #conn.rollback()
    finally:
      if conn is not None:
        cur.close()
        conn.close()
        print('Database connection closed.')
    
  def print_sql_err(self,err):
    # get details about the exception
    err_type, err_obj, traceback = sys.exc_info()

    # get the line number when exception occured
    line_num = traceback.tb_lineno

    # print the connect() error
    print ("\npsycopg ERROR:", err, "on line number:", line_num)
    print ("psycopg traceback:", traceback, "-- type:", err_type)

    # print the pgcode and pgerror exceptions
    print ("pgerror:", err.pgerror)
    print ("pgcode:", err.pgcode, "\n")

  def query_wrap_object(self,template):
    sql = f"""
    (SELECT COALESCE(row_to_json(object_row),'{{}}'::json) FROM (
    {template}
    ) object_row);
    """
    return sql

  def query_wrap_array(self,template):
    sql = f"""
    (SELECT COALESCE(array_to_json(array_agg(row_to_json(array_row))),'[]'::json) FROM (
    {template}
    ) array_row);
    """
    return sql
    
db = Db()