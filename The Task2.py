def my_func(name, surname, year, city, email, telephone):
    return ' '.join([name, surname, year, city, email, telephone])


print(my_func(surname='Likanov', name='Mikhail', year='1996', city='Kazan', email='Mikhail.Likanov@mail.ru',
              telephone='8-000-300-00-00'))