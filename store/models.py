from django.db import models
from django.db import connection


class Product(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()

    def my_custom_sql(self):
        with connection.cursor() as cursor:
            cursor.execute("UPDATE bar SET foo = 1 WHERE name = %s", [self.name])
            cursor.execute("SELECT foo FROM bar WHERE name = %s", [self.name])
            row = cursor.fetchone()

        return row

'''
cursor = connection.cursor()
try:
    cursor.callproc('[dbo].[uspDoesSomething]', [5, 'blah'])

    if cursor.return_value == 1:
        result_set = cursor.fetchall()
finally:
    cursor.close()


def my_custom_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("SELECT foo FROM bar WHERE baz = %s", [self.baz])
        row = cursor.fetchone()

    return row
'''
