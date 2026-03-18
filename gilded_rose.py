# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_price(self):
        for item in self.items:
            match item.name:
                case "Aged Brie":
                    AgedBrie_and_Backstage_passes.update_price(item)
                case "Backstage passes to a TAFKAL80ETC concert":
                    AgedBrie_and_Backstage_passes.update_price(item)
                case "Elixir of the Mongoose":
                    Elixir_of_the_Mongoose_and_Dexterity_Vest.update_price(item)
                case "+5 Dexterity Vest":
                    Elixir_of_the_Mongoose_and_Dexterity_Vest.update_price(item)
                case "Conjured Mana Cake":
                    Conjured_Mana_Cake.update_price(item)

            

                
class AgedBrie_and_Backstage_passes(GildedRose):
    @staticmethod
    def update_price(item):
        if item.price < 50:
            if item.sell_in < 50 and item.sell_in >= 10:
                item.price += 1
                item.sell_in -= 1

            elif item.sell_in < 10 and item.sell_in >= 5:
                item.price += 2
                item.sell_in -= 1

            elif item.sell_in < 5 and item.sell_in >= 0:
                item.sell_in -= 1
                item.price += 3

            else:
                item.price = 0

        return item.price, item.sell_in
    
class Elixir_of_the_Mongoose_and_Dexterity_Vest(GildedRose):
    @staticmethod
    def update_price(item):
        if item.sell_in > 0:
            item.sell_in -= 1
            item.price -= 1
        
        else:
            item.price -= 2
        return item.price, item.sell_in

class Conjured_Mana_Cake(GildedRose):
    @staticmethod
    def update_price(item):
        if item.sell_in > 0:
            item.sell_in -= 1
            item.price -= 2
        
        else:
            item.price -= 4
        return item.price, item.sell_in

class Item:
    def __init__(self, name, sell_in, price):
        self.name = name
        self.sell_in = sell_in
        self.price = price

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.price)



        