from database import Database
from datas import animals_list, ages_list, gender_list


def main():
    db1 = Database('Animals_database.db')
    db1.create_table_animals()
    db1.insert_table_animals(animals_list)
    db1.create_table_age()
    db1.insert_table_age(ages_list)
    db1.create_table_gender()
    db1.insert_table_gender(gender_list)
    db1.select_older_value_left_join(2)
    db1.select_older_value_inner_join(3)
    db1.select_gender_animals('male')
    db1.close()

if __name__ == '__main__':
    main()