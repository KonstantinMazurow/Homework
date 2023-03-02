from database import Database
from dates import clients_list, services_list, orders_list


def main():

    db1 = Database('orders_clients.db')
    db1.create_table_clients()
    db1.insert_table_clients(clients_list)
    db1.create_table_services()
    db1.insert_table_services(services_list)
    db1.create_table_orders()
    db1.insert_table_orders(orders_list)

if __name__ == '__main__':
    main()