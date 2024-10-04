import os
import sqlite3
import platform

db_path = 'label_studio.sqlite3'

windows_source_path = 'C:\\Users\\Administrator\\Desktop\\code\\coconut-annotations\\storage\\dataset'
linux_source_path = '/home/adrianne/Desktop/code/coconut-annotations/storage/dataset'

windows_target_path = 'C:\\Users\\Administrator\\Desktop\\code\\coconut-annotations\\storage\\export'
linux_target_path = '/home/adrianne/Desktop/code/coconut-annotations/storage/export'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

current_os = platform.system()

try:
    if current_os == 'Windows':
        print("Detected OS: Windows. Updating paths for Windows.")
        
        cursor.execute(
            """
            UPDATE io_storages_localfilesmixin
            SET path = ?
            WHERE id = 3;
            """,
            (windows_source_path,)
        )
        cursor.execute(
            """
            UPDATE io_storages_localfilesmixin
            SET path = ?
            WHERE id = 4;
            """,
            (windows_target_path,)
        )

    elif current_os == 'Linux':
        print("Detected OS: Linux. Updating paths for Linux.")
        
        cursor.execute(
            """
            UPDATE io_storages_localfilesmixin
            SET path = ?
            WHERE id = 3;
            """,
            (linux_source_path,)
        )
        cursor.execute(
            """
            UPDATE io_storages_localfilesmixin
            SET path = ?
            WHERE id = 4;
            """,
            (linux_target_path,)
        )

    conn.commit()
    print("Paths updated successfully.")

except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    conn.close()
