"""
from  make.db import make_db
mdb = make_db()
# All = mdb.get_all(table='cities')
# add = mdb.insert_dict_into_table(to_work)
# del = mdb.delete_cat(cat)

"""

import sqlite3
import os
from pathlib import Path
import json
from newapi.except_err import exception_err

# ---
from .. import printe

Dir = Path(__file__).parent
print_t = {1: False}


def printt(x):
    if print_t[1]:
        print(x)


class make_db:

    def __init__(self):
        self.database_path = os.path.join(Dir, "db.db")
        # ---
        if not os.path.exists(self.database_path):
            with open(self.database_path, "w", encoding="utf-8") as f:
                f.write("")
        # ---
        self.conn = sqlite3.connect(self.database_path)
        # ---
        self.conn.row_factory = sqlite3.Row
        # ---
        self.cursor = self.conn.cursor()
        # ---
        # self.create_database_table()

    def do_query(self, query, get_data=False):
        # ---
        data = []
        # ---
        try:
            self.cursor.execute(query)
            if get_data:
                data = self.cursor.fetchall()
            else:
                self.conn.commit()
            # ---
        except Exception as e:
            exception_err(e)
            if get_data:
                return []
            else:
                return False
        finally:
            if get_data:
                # data = { x: v for x, v in data }
                list_accumulator = []
                for item in data:
                    list_accumulator.append({k: item[k] for k in item.keys()})
                return list_accumulator
        # ---
        return True

    def create_database_table(self):
        # ---
        self.do_query(
            """
            CREATE TABLE IF NOT EXISTS cities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                en TEXT,
                ar TEXT
            )
            """
        )

    def get_all(self, table="cities"):
        qua = f"""SELECT en, ar FROM {table}"""
        # ---
        data = self.do_query(qua, get_data=True)
        # ---
        return data

    def insert_dict(self, table, lento=100):
        # ---
        done = 0
        # ---
        for i in range(0, len(table), lento):
            # ---
            tab = dict(list(table.items())[i : i + lento])
            # ---
            values = []
            # ---
            for k, c in tab.items():
                values.append((k, c))
            # ---
            qua = """
                INSERT INTO cities (en, ar)
                values (?, ?)
                """
            # ---
            try:
                self.cursor.executemany(qua, values)
                self.conn.commit()
            except Exception as e:
                exception_err(e)
            finally:
                done += int(len(values))
                print(f"not_in_db.py insert_dict() {done} done, from {len(table)}.")

    def update_table(self, table, lento=100):
        # ---
        done = 0
        # ---
        for i in range(0, len(table.keys()), lento):
            # ---
            tab = dict(list(table.items())[i : i + lento])
            # ---
            lenth = int(len(tab.keys()))
            # ---
            when = ""
            # ---
            for en, ar in tab.items():
                en = en.strip().replace("_", " ")
                when += f"\tWHEN '{en}' THEN '{ar}'\n"
            # ---
            when_list = "', '".join(tab.keys())
            # ---
            qua = f"""UPDATE cities SET ar = CASE en\n{when} \n ELSE ar END \nWHERE en IN ('{when_list}');"""
            # ---
            printt(qua)
            # ---
            aa = self.do_query(qua)
            # ---
            if aa:
                done += lenth
                print(f"not_in_db.py update_table() {done} done, from {len(table.keys())}.")

    def insert_dict_into_table(self, table):
        # ---
        printt(f"insert_dict_into_table: len:{len(table.keys())}")
        # ---
        insert = {}
        update = {}
        # ---
        already_in = {x["en"]: x["ar"] for x in self.get_all()}
        # ---
        for k, c in table.items():
            en = k.strip().replace("_", " ")
            c = c.strip().replace("_", " ")
            # ---
            c_in = already_in.get(en)
            # ---
            if c_in:
                if c != c_in:
                    update[en] = c
                # ---
            else:
                insert[en] = c
        # ---
        printt(f"\t insert: {len(insert.keys())}")
        printt(f"\t update: {len(update.keys())}")
        # ---
        self.insert_dict(insert)
        self.update_table(update)

    def delete_cat(self, en):
        # ---
        qua = f"""DELETE FROM cities WHERE en = '{en}';"""
        # ---
        aa = self.do_query(qua)
        if aa:
            printe.output(f"<<green>> delete_cat({en}) done.")


# ---
mdb = make_db()
# create_database_table
mdb.create_database_table()


def main():
    # ---
    mdb = make_db()
    # ---
    taba = {
        "Sana'a": "صنعاء",
    }
    # ---
    from ..ma_lists_bots import N_cit_ies_s_lower

    # ---
    print(f"len(N_cit_ies_s_lower): {len(N_cit_ies_s_lower)}")
    mdb.insert_dict_into_table(N_cit_ies_s_lower)
    # ---
    All = mdb.get_all(table="cities")
    print(f"len(All): {len(All)}")
    # ---
    data = {x["en"]: x["ar"] for x in All}
    # ---
    with open(f"{Dir}/All.txt", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    print_t[1] = True
    main()
