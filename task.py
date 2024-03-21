shopp_list = {
    "piekarnia" : ["chleb", "pączek", "bułki"],
    "warzywniak" : ["marchew", "seler", "rukola"]
}
for sklep, produkty in shopp_list.items():
    sklep1 = sklep.capitalize()
    produkty1 = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep1}, kupuję tu następujące rzeczy: {', '.join(produkty1)}.")