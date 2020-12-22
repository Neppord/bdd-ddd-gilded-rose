from gilded_rose import GildedRose, create_item


def test_it_decreases_sell_in_by_normal_rate():
    aged_brie = create_item("Aged Brie", 2, 10)
    items = [aged_brie]
    GildedRose(items).update_quality()
    assert aged_brie.sell_in == 1


def test_it_increases_in_quality_at_normal_rate():
    aged_brie = create_item("Aged Brie", 2, 10)
    items = [aged_brie]
    GildedRose(items).update_quality()
    assert aged_brie.quality == 11


def test_it_increases_in_quality_at_double_rate_when_sell_date_has_passed():
    aged_brie = create_item("Aged Brie", 0, 10)
    items = [aged_brie]
    GildedRose(items).update_quality()
    assert aged_brie.quality == 12
