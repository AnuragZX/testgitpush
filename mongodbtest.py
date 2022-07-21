import pymongo

client = pymongo.MongoClient("mongodb+srv://anurag:Anurag15@cluster0.4ysrk.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {'name':"anurag",
     'email':"anurag.ineuron.ai",
     'surname':"shukla"}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)