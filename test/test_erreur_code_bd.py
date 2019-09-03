


try :
    pass
except mysql.Error as e:
    print("Error code:", e.errno)  # error number
    print("SQLSTATE value:", e.sqlstate) # SQLSTATE value
    print("Error message:", e.msg)  # error message
    print("Error:", e)  # errno, sqlstate, msg values
    s = str(e)
    print("Error:", s)  # errno, sqlstate, msg valu
