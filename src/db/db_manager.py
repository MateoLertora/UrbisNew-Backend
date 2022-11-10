import csv
import json

def read_orders():
    with open('src/db/ordenes.csv', 'r') as orders_file:
        with open('src/db/getOrdenes.csv', 'a') as f:
            rows = csv.DictReader(orders_file)
            for row in rows:
                linea = str(row)
                f.write(linea)






def load_orders():
    orders = []
    with open('src/db/ordenes.csv', 'r') as orders_file:
        rows = csv.DictReader(orders_file)

        for row in rows:
            orders.append(row)

        return orders


def save_new_order(order):
    with open('src/db/ordenes.csv', 'a') as orders_file:
        header = ["cliente", "telefono", "entrega", "horario", "pedido"]

        writer = csv.DictWriter(orders_file, fieldnames=header)

        if orders_file.tell() == 0:
            writer.writeheader()

        writer.writerow(order)
