import numpy, json
transactionLog = [
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_10'},
    {'orderId': 1001, 'customerId': 'cust_Ahmed', 'productId': 'prod_12'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_10'},
    {'orderId': 1002, 'customerId': 'cust_Bisma', 'productId': 'prod_15'},
    {'orderId': 1003, 'customerId': 'cust_Ahmed', 'productId': 'prod_15'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_12'},
    {'orderId': 1004, 'customerId': 'cust_Faisal', 'productId': 'prod_10'},
]

productCatalog = {
    'prod_10': 'Wireless Mouse',
    'prod_12': 'Keyboard',
    'prod_15': 'USB-C Hub',
}
def processTransactions(transactionslist):
    data = {}
    for t in transactionslist:
        customer_id = t['customerId']
        product_id = t['productId']
        if customer_id not in data:
            data[customer_id] = set()
        data[customer_id].add(product_id)
    return data
print("Processing transactions")
data = processTransactions(transactionLog)
print("Customer data:", data)
def findFrequentPairs(custData):
    freqs = {}
    for CustID, product in custData.items():
        allproducts = list(product)
        allproducts.sort()

        for i in range(len(allproducts)):
            for j in range(1, len(allproducts)):

                sets = (allproducts[i], allproducts[j])

                if sets in freqs:
                    freqs[sets] += 1
                else:
                    freqs[sets] = 1
    return freqs

print("Finding frequent pairs")
pairs = findFrequentPairs(data)
print("Frequent pairs:", pairs)
def getRecommendation(targetId, freq):
    recommends = []
    for p in freq:
        count = freq[p]
        if targetId == p[0]:
            other = p[1]
            recommends.append((other, count))
        elif targetId == p[1]:
            other = p[0]
            recommends.append((other, count))

    recommends.sort()
    recommends.reverse()
    return recommends
def generateReport(target_id, recommendations, catalog):
    print("Report")

    target_name = catalog.get(target_id, "Unknown Product")
    print(f"Target Product: {target_id} ({target_name})")

    if not recommendations:
        print("No recommendations found.")
        return
    size = len(recommendations)
    print(f"Number of recommendations: {size}\n")
    print("Ranked Recommendations:\n")

    for i, (productId, count) in enumerate(recommendations, 1):
        name = catalog.get(productId, "Unknown Product")
        print(f"{i}. {productId} ({name}) - Co-purchased {count} time(s)")

testing = ['prod_10', 'prod_12', 'prod_15']

for product in testing:
    print("")
    recommendations = getRecommendation(product, pairs)
    generateReport(product, recommendations, productCatalog)