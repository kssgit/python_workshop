from service.product_service import ProductService
from view.view import input_display, update_display, message_display
from view.view import list_display, delete_display


class ProductController:

    def register(self):
        product = input_display()
        service = ProductService()
        message_display(service.register(product))

    def getAllProduct(self):
        service = ProductService()
        list_display(service.getAllProduct())

    def delete(self):
        p_id = delete_display()
        service = ProductService()
        message_display(service.delete(p_id))

    def update(self):
        p_id, p_name, price = update_display()
        service = ProductService()
        message_display(service.update(p_id, p_name, price))

    def file_read(self):
        service = ProductService()
        service.file_read()

    def file_write(self):
        service = ProductService()
        service.file_write()
