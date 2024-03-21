shopp_list = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
    "mięsny" : ["kurczak", "wołowina", "kabanosy"]
}
print("Lista zakupów") 
sum_produkt = 0
for sklep, produkty in shopp_list.items():
    sklep1 = sklep.capitalize()
    produkty1 = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep1}, kupuję tu następujące rzeczy: {', '.join(produkty1)}.")
    sum_produkt += len(produkty1) 
print(f"W sumię kupię {sum_produkt} produktów.")
