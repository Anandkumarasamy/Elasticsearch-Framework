from faker import Faker
from operations.product.mongo_search import Mongoose


# def main():
#     _helper = ElasticSearch(host="localhost", index="test_data", doc_type="details")
#
#     _record = {
#         "product_id": "trail_36",
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
#         "delivery_charge":{
#             "local_delivery_charge" : "50",
#             "zonal_delivery_charge" : "100",
#             "national_delivery_charge" : "150"
#         },
#         "product_status": "Approved/Pending/Rejected",
#         "search_keyword": "Pickle, Mango, Andhra"
#     }
#     res = _helper.insert.insert_one(record=_record)
#     print(res)


def main():
    _helper = Mongoose(host="mongodb://localhost:27017", dbname="testing_database", collection_name="person")

    # fake = Faker()

    # _record = {
    #     "product_id": "trail_40",
    #     "product_name": "Halva",
    #     "product_type": "General/Instant",
    #     "product_category_id": "HJK123",
    #     "product_menutype_id": "OPI456",
    #     "product_category": "Pickles",
    #     "product_subcategory": "Mango Pickle",
    #     "product_description": "Lorem Ipsum is simply dummy text of the printing and typesetting industry.",
    #     "product_sellers": [{
    #         "seller_id": "vendor123",
    #         "product_info": {
    #             "product_version": "pinfo_1_1",
    #             "product_brand_name": "Amrutha Foods",
    #             "product_certificate": "Yes/No",
    #             "number_of_products": 20,
    #             "product_quantity": "100g",
    #             "product_MRP": 25,
    #             "product_price": 22.60,
    #             "discount_offer": 0,
    #             "container_type": "glass",
    #             "food_preference": "Non Veg/Veg",
    #             "made_in_country": "Indian",
    #             "reginal_speciality": "Andhra, Karnataka",
    #             "manufactured_by": "Paakashala",
    #             "manufacture_date": "22-10-2020",
    #             "max_self_life": "5 months",
    #             "taste": "spicy",
    #             "organic": "Yes/No",
    #             "product_hsn": "ABC456",
    #             "product_tax": "12%",
    #             "product EANean_or_upc": "EAN-13",
    #             "ingredents": {
    #                 "base_ingredents": "mango pieces, salt",
    #                 "ingredents": "mango, masala"
    #             },
    #             "dietary_preference": "Yes/No",
    #             "preservation_process": "Store in warm place",
    #             "nutritional_facts": {
    #                 "Energy": "78 cal",
    #                 "Protein": "0.2 g",
    #                 "Carbohydrates": "18.5 g",
    #                 "Fat": "5.0 g",
    #                 "Fiber": "0.3 g",
    #                 "Sugar": "0 g"
    #             },
    #             "product_images": ["jwgwf.jpg", "jbgkrj.png", "krbf.jpg"],
    #             "video_url": " http://amrutha.com"
    #         }
    #     }
    #     ],
    #     "delivery_charge": {
    #         "local_delivery_charge": "50",
    #         "zonal_delivery_charge": "100",
    #         "national_delivery_charge": "150"
    #     },
    #     "product_status": "Approved/Pending/Rejected",
    #     "search_keyword": "Pickle, Mango, Andhra"
    # }
    _record = {
        "product_id": "trail_43",
        "seller_id": "vendor123",
        "product_version": "pinfo_1_1",
        "number_of_products": 10
    }

    res = _helper.update.update_quantity(record=_record)
    print(res)


if __name__ == "__main__":
    main()
