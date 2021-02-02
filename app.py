from fake_data import Faker
from operations.product.mongo_search import Mongoose
from operations.product.elastic_search import ElasticSearch


def main():
    _helper = ElasticSearch(host="localhost", index="test_data", doc_type="details")

    # _record = [
    #     {
    #         "product_id": "trail_bulk_41",
    #         "product_name": "Pickle",
    #         "product_type": "General/Instant",
    #         "product_category": "Pickles",
    #         "product_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    #         "product_sellers": [{
    #             "seller_id": "vendor123",
    #             "product_info": {
    #                 "product_version": "pinfo_1_1",
    #                 "product_brand_name": "Amrutha Foods",
    #                 "subcategory": "Mango Pickle",
    #                 "product_certificate": "Yes/No",
    #                 "number_of_products": 20,
    #                 "product_quantity": "100g",
    #                 "product_MRP": 25,
    #                 "product_price": 22.60,
    #                 "discount_offer": 0,
    #                 "container_type": "glass",
    #                 "food_preference": "Non Veg/Veg",
    #                 "made_in_country": "Indian",
    #                 "reginal_speciality": "Andhra, Karnataka",
    #                 "manufactured_by": "Paakashala",
    #                 "manufacture_date": "22-10-2020",
    #                 "max_self_life": "5 months",
    #                 "taste": "spicy",
    #                 "organic": "Yes/No",
    #                 "product_hsn": "ABC456",
    #                 "product_tax": "12%",
    #                 "product EANean_or_upc": "EAN-13",
    #                 "ingredents": {
    #                     "base_ingredents": "mango pieces, salt",
    #                     "ingredents": "mango, masala"
    #                 },
    #                 "dietary_preference": "Yes/No",
    #                 "preservation_process": "Store in warm place",
    #                 "nutritional_facts": {
    #                     "Energy": "78 cal",
    #                     "Protein": "0.2 g",
    #                     "Carbohydrates": "18.5 g",
    #                     "Fat": "5.0 g",
    #                     "Fiber": "0.3 g",
    #                     "Sugar": "0 g"
    #                 },
    #                 "product_images": ["jwgwf.jpg", "jbgkrj.png", "krbf.jpg"],
    #                 "video_url": " http://amrutha.com"
    #             }
    #         }
    #         ],
    #         "delivery_charge": {
    #             "local_delivery_charge": "50",
    #             "zonal_delivery_charge": "100",
    #             "national_delivery_charge": "150"
    #         },
    #         "product_status": "Approved/Pending/Rejected",
    #         "search_keyword": "Pickle, Mango, Andhra"
    #     },
    #     {
    #         "product_id": "trail_bulk_42",
    #         "product_name": "Pickle",
    #         "product_type": "General/Instant",
    #         "product_category": "Pickles",
    #         "product_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    #         "product_sellers": [{
    #             "seller_id": "vendor123",
    #             "product_info": {
    #                 "product_version": "pinfo_1_1",
    #                 "product_brand_name": "Amrutha Foods",
    #                 "subcategory": "Mango Pickle",
    #                 "product_certificate": "Yes/No",
    #                 "number_of_products": 20,
    #                 "product_quantity": "100g",
    #                 "product_MRP": 25,
    #                 "product_price": 22.60,
    #                 "discount_offer": 0,
    #                 "container_type": "glass",
    #                 "food_preference": "Non Veg/Veg",
    #                 "made_in_country": "Indian",
    #                 "reginal_speciality": "Andhra, Karnataka",
    #                 "manufactured_by": "Paakashala",
    #                 "manufacture_date": "22-10-2020",
    #                 "max_self_life": "5 months",
    #                 "taste": "spicy",
    #                 "organic": "Yes/No",
    #                 "product_hsn": "ABC456",
    #                 "product_tax": "12%",
    #                 "product EANean_or_upc": "EAN-13",
    #                 "ingredents": {
    #                     "base_ingredents": "mango pieces, salt",
    #                     "ingredents": "mango, masala"
    #                 },
    #                 "dietary_preference": "Yes/No",
    #                 "preservation_process": "Store in warm place",
    #                 "nutritional_facts": {
    #                     "Energy": "78 cal",
    #                     "Protein": "0.2 g",
    #                     "Carbohydrates": "18.5 g",
    #                     "Fat": "5.0 g",
    #                     "Fiber": "0.3 g",
    #                     "Sugar": "0 g"
    #                 },
    #                 "product_images": ["jwgwf.jpg", "jbgkrj.png", "krbf.jpg"],
    #                 "video_url": " http://amrutha.com"
    #             }
    #         }
    #         ],
    #         "delivery_charge": {
    #             "local_delivery_charge": "50",
    #             "zonal_delivery_charge": "100",
    #             "national_delivery_charge": "150"
    #         },
    #         "product_status": "Approved/Pending/Rejected",
    #         "search_keyword": "Pickle, Mango, Andhra"
    #     }
    # ]
    _record = [{"_id": "trail_24"}, {"_id": "trail_27"}]
    res = _helper.delete.delete_many(record=_record)
    print(res)


# def main(number):
#     _helper = Mongoose(host="mongodb://localhost:27017", dbname="testing_database", collection_name="person")
#
#     fake = Faker()
#
#     for num in range(number):
#         _record = {
#             "product_id": fake.bothify(text='????-####', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
#             "product_name": "Pickles",
#             "product_category_id": [fake.bothify(text='category-###')],
#             "product_subcategory": fake.random_element(elements=(
#             "Andhra Avakaya", "Sweet Mango Pickle", "Mango Thokku", "Sweet Ginger Pickle", "Spicy Ginger Pickle",
#             "Amla Pickle", "Bitter Gourd Pickle", "Pudina Pickle", "Mixed Veg Pickle", "Red Chilly", "Coriender Pickle",
#             "Tamarind Pickle", "Lemon Pickle", "Amarnath Pickle", "Gogura Pickle", "Carrot Pickle",
#             "Cauliflower pickle", "Capsicum Pickle", "Garlic Pickle", "Chiken Pickle", "Ginger Garlic")),
#             "product_type_id": [fake.bothify(text='type-###')],
#             "product_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
#             "product_sellers": [{
#                 "seller_id": fake.bothify(text='vendor-###'),
#                 "product_info": {
#                     "product_version": fake.bothify(text='pinfo-###'),
#                     "product_brand_name": "Amrutha Foods",
#                     "product_certificate": fake.random_element(elements=("Yes", "No")),
#                     "number_of_products": fake.random_int(0, 100),
#                     "product_quantity": fake.random_element(elements=("100g", "200g", "500g", "1kg")),
#                     "product_MRP": fake.random_int(0, 100),
#                     "product_price": 22.60,
#                     "discount_offer": 0,
#                     "container_type": fake.random_element(elements=("glass", "polythene packet", "paper packet")),
#                     "food_preference": fake.random_element(elements=("Non Veg", "Veg")),
#                     "made_in_country": "Indian",
#                     "reginal_speciality": fake.city(),
#                     "manufactured_by": "Paakashala",
#                     "manufacture_date": fake.date(),
#                     "max_self_life": fake.month(),
#                     "taste": "spicy",
#                     "organic": fake.random_element(elements=("Yes", "No")),
#                     "product_hsn": fake.bothify(text='???-###', letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
#                     "product_tax": fake.random_element(elements=("5%", "10%", "12%", "18%")),
#                     "product EANean_or_upc": "EAN-13",
#                     "ingredents": {
#                         "base_ingredents": "mango pieces, salt",
#                         "ingredents": "mango, masala"
#                     },
#                     "dietary_preference": fake.random_element(elements=("Yes", "No")),
#                     "nutritional_facts": {
#                         "Energy": "78 cal",
#                         "Protein": "0.2 g",
#                         "Carbohydrates": "18.5 g",
#                         "Fat": "5.0 g",
#                         "Fiber": "0.3 g",
#                         "Sugar": "0 g"
#                     },
#                     "product_images": ["jwgwf.jpg", "jbgkrj.png", "krbf.jpg"],
#                     "video_url": " http://amrutha.com"
#                 }
#             }
#             ],
#             "delivery_charge": {
#                 "local_delivery_charge": "50",
#                 "zonal_delivery_charge": "100",
#                 "national_delivery_charge": "150"
#             },
#             "product_status": fake.random_element(elements=("Approved", "Pending", "Rejected")),
#             "search_keyword": "Pickle, Mango, Andhra"
#         }
#         # _record = {
#         #     "category_id": "AMCAT_fhrf3g",
#         #     "category_name": "fried food",
#         #     "category_description": "jhggyg"
#         # }
#         # _record = {
#         #     "type_id": "AMTY_bfr3b",
#         #     "product_type": "General/Instant",
#         #     "preservation measures": {
#         #         "status": "Active/Inactive",
#         #         "preservation_process": "Store in warm place"
#         #     },
#         #     "type_description": "description"
#         # }
#
#         res = _helper.insert.insert_one(record=_record)
#         print(res)


if __name__ == "__main__":
    main()
