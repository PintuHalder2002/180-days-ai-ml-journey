products = ["iphone", "ipad", "Macbook"]
regions = ["USA", "China", "India"]
revenue = [20, 23, 45, 18, 17, 12, 9, 5]

i = 0

for product in products:
    for region in regions:
        # rev = revenue[i]
        # i += 1
        for rev in revenue:
            print(f"{product} -> {region} and revenue: ", rev)

