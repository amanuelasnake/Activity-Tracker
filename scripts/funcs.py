def dbAdd(content):
    import sqlite3
    from datetime import datetime
    # Establishconnection
    conn = sqlite3.connect('/home/amanuel/AmanuelPersonal/project_ideas/Activity Tracker/database/local.db')
    cursor = conn.cursor()
    #  query
    sql_query = "INSERT INTO activities (activity, time) VALUES (?,?);"
    #time
    time = datetime.now().strftime('%m/%d %H:%M')
    # Insert
    cursor.execute(sql_query, (content,time,))
    # Save
    conn.commit()
    # Close
    conn.close()

def dbLimit():
    import sqlite3

    conn = sqlite3.connect('/home/amanuel/AmanuelPersonal/project_ideas/Activity Tracker/database/local.db')
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM activities")
    total_rows = cursor.fetchone()[0]

    conn.close()

    return total_rows

def dbPopOldest():
    import sqlite3
    conn = sqlite3.connect('/home/amanuel/AmanuelPersonal/project_ideas/Activity Tracker/database/local.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM activities WHERE id = (SELECT id FROM activities ORDER BY id ASC LIMIT 1);")
    conn.commit()
    conn.close()

def dbActivities():
    import sqlite3
    conn = sqlite3.connect('/home/amanuel/AmanuelPersonal/project_ideas/Activity Tracker/database/local.db')
    cursor = conn.cursor()
    cursor.execute("SELECT time, activity FROM activities ORDER BY id DESC LIMIT 720")
    rows = cursor.fetchall()
    conn.close()
    return [{'time': row[0], 'activity': row[1]} for row in rows]

