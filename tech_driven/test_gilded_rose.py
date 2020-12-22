from gilded_rose import GildedRose, Item


def test_update_sell_in():
    normal_item = Item("normal", 2, 10)
    aged_brie = Item("Aged Brie", 2, 10)
    sulfuras_item = Item("Sulfuras, Hand of Ragnaros", 2, 10)
    backstage_pass_item = Item("Backstage passes to a TAFKAL80ETC concert", 2, 10)
    items = [
        normal_item,
        aged_brie,
        sulfuras_item,
        backstage_pass_item
    ]
    GildedRose(items).update_quality()
    assert normal_item.sell_in == 1
    assert aged_brie.sell_in == 1
    assert sulfuras_item.sell_in == 2
    assert backstage_pass_item.sell_in == 1


def test_update_quality():
    normal_item = Item("normal", 2, 10)
    aged_brie = Item("Aged Brie", 2, 10)
    sulfuras_item = Item("Sulfuras, Hand of Ragnaros", 2, 10)
    early_backstage_pass_item = Item("Backstage passes to a TAFKAL80ETC concert", 10, 10)
    backstage_pass_item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)
    late_backstage_pass_item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 10)
    items = [
        normal_item,
        aged_brie,
        sulfuras_item,
        early_backstage_pass_item,
        backstage_pass_item,
        late_backstage_pass_item,
    ]
    GildedRose(items).update_quality()
    assert normal_item.quality == 9
    assert aged_brie.quality == 11
    assert sulfuras_item.quality == 10
    assert early_backstage_pass_item.quality == 12
    assert backstage_pass_item.quality == 13
    assert late_backstage_pass_item.quality == 0


def test_edges():
    normal_item = Item("normal", 2, 51)
    normal_item2 = Item("normal", 0, 51)
    aged_brie = Item("Aged Brie", 0, 0)
    items = [
        normal_item,
        normal_item2,
        aged_brie,
    ]
    GildedRose(items).update_quality()
    assert normal_item.quality == 50
    assert normal_item2.quality == 49
    assert aged_brie.quality == 2
