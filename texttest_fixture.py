# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *


def main():
    print("OMGHAI!")
    items = [
        Item(name="+5 Dexterity Vest", sell_in=10, price=20),
        Item(name="Aged Brie", sell_in=2, price=0),
        Item(name="Elixir of the Mongoose", sell_in=5, price=7),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, price=80),
        Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, price=80),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, price=20),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, price=49),
        Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, price=49),
        Item(name="Conjured Mana Cake", sell_in=3, price=6),  # <-- :O
    ]
    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, price")
        for item in items:
            print(item)
        print("")
        GildedRose(items).update_price()


if __name__ == "__main__":
    main()
