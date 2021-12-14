#!/usr/local/bin/python
import sys
import sqlite3
import subprocess

DEBUG = False
IN_DB = "DB"
OUT_DB = sys.argv[1]
in_con = sqlite3.connect(IN_DB)
out_con = sqlite3.connect(OUT_DB)
in_cur = in_con.cursor()
out_cur = out_con.cursor()
idx = {
    "id": 0,
    "url": 1,
    "title": 2,
    "visit_count": 3,
    "typed_count": 4,
    "last_visit_time": 5,
    "hidden": 6,
}
cnt = 0


def _log_debug(msg):
    if DEBUG:
        print(msg)


def _log_info(msg):
    print(msg)


def exec_cmd(cmd):
    result = subprocess.check_output(cmd, shell=True)
    result = str(result, "utf-8")
    return result.strip("\n")


def update_item(fields):
    in_cur.execute(
        "update urls set title=?, visit_count=?, typed_count=?, last_visit_time=?, hidden=? where url=?",
        (
            fields[idx["title"]],
            1720,
            fields[idx["typed_count"]],
            fields[idx["last_visit_time"]],
            fields[idx["hidden"]],
            fields[idx["url"]],
        ),
    )


def insert_item(fields):
    in_cur.execute(
        "insert into urls (url, title, visit_count, typed_count, last_visit_time, hidden) values (?, ?, ?, ?, ?, ?)",
        (
            fields[idx["url"]],
            fields[idx["title"]],
            fields[idx["visit_count"]],
            fields[idx["typed_count"]],
            fields[idx["last_visit_time"]],
            fields[idx["hidden"]],
        ),
    )


def dispose_rows(rows):
    global cnt
    for row in rows:
        cnt = cnt + 1
        in_cur.execute("select * from urls where url=:url", {"url": row[idx["url"]]})
        fields = in_cur.fetchone()
        if fields != None and len(fields) > 0:
            update_item(row)
            if cnt % 100 == 0:
                print("u", end="", flush=True)
        else:
            insert_item(row)
            if cnt % 100 == 0:
                print("i", end="")


if __name__ == "__main__":
    batch = 100
    offset = 0
    while True:
        rows = out_cur.execute(
            "select * from urls limit ?, ?", (offset, batch)
        ).fetchall()
        dispose_rows(rows)
        offset = offset + batch
        if len(rows) < batch:
            break
    in_con.commit()
