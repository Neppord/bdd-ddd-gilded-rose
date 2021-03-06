from gilded_rose import GildedRose, Sulfuras


def test_update_sell_in():
    sulfuras_item = Sulfuras("Sulfuras, Hand of Ragnaros", 2, 10)
    items = [sulfuras_item]
    GildedRose(items).update_quality()
    assert sulfuras_item.sell_in == 2


def test_update_quality():
    sulfuras_item = Sulfuras("Sulfuras, Hand of Ragnaros", 2, 80)
    items = [sulfuras_item]
    GildedRose(items).update_quality()
    assert sulfuras_item.quality == 80

