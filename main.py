print("Lista zakupów")
shops = {
    "piekarnia": ["bułki", "chleb", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
shops = {k:[x.capitalize() for x in v] for k,v in shops.items()}
for shop in shops:
    print("Idę do", shop.capitalize(),"i kupuję tu następujące rzeczy:", shops[shop],".")
amount = 0
for am in shops.values():
    amount = amount + len(am)
print("W sumie kupuję", amount, "produktów.")