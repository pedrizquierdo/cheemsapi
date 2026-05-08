from persistence.db import get_connection

class Trip:

    def __init__(self, name: str, city: str, latitude: float, longitude: float):
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude


    def get_all():
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, name, city, latitude, longitude FROM trip")
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            connection.close()

    def save(self):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = "INSERT INTO trip (name, city, latitude, longitude) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.name, self.city, self.latitude, self.longitude))
            connection.commit()
            return cursor.lastrowid
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            connection.close()

    def update(id, name, city, latitude, longitude):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = "UPDATE trip SET name=%s, city=%s, latitude=%s, longitude=%s WHERE id=%s"
            cursor.execute(sql, (name, city, latitude, longitude, id))
            connection.commit()
            return True
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            connection.close()

    def delete(id):
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM trip WHERE id=%s", (id,))
            connection.commit()
            return True
        except Exception as ex:
            print(ex)
        finally:
            cursor.close()
            connection.close()
