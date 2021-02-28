# FORMATIEVE OPDRACHT 2a
# Justin Klein - 1707815
# KLAS: V1B - PG1

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client.huwebshop
P_collection = db.products

def GetFirstItem(P_collection):
    return P_collection.find_one()

#print(GetFirstItem(P_collection))


def GetFirstItemR(P_collection): # returns een 'none'. Klopt dit wel?
    query = {"name": {"$regex": '/R/' }}
    doc = P_collection.find_one(query)
    return doc

#print(GetFirstItemR(P_collection))


def GetAveragePriceAll(P_collection): # Werkt niet zoals verwacht, sommige items hebben geen prijs!
    prices = []
    doc = P_collection.find()
    for i in doc:
        if i["price"] == "":
            pass
        else:
            prices.append(i["price"])
    return prices

#print(GetAveragePriceAll(P_collection))
