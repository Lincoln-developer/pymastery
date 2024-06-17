import contextlib

def start_db():
    print("systectl start postgresql.servive")

def stop_db():
    print("systemctl stop postgresql.service")

def back_up():
    print("pg_dump_database")

@contextlib.contextmanager
def database_handler():
    try:
        stop_db()
        yield
    finally:
        start_db()

with database_handler():
    back_up()


