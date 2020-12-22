from gilded_rose import GildedRose, Normal


def test_it_decreases_sell_in_by_normal_rate():
    normal_item = Normal("normal", 2, 10)
    items = [normal_item]
    GildedRose(items).update_quality()
    assert normal_item.sell_in == 1


def test_it_decrease_quality_by_normal_rate():
    normal_item = Normal("normal", 2, 10)
    items = [normal_item]
    GildedRose(items).update_quality()
    assert normal_item.quality == 9


def test_it_decrease_quality_by_double_rate_when_sell_date_has_passed():
    normal_item = Normal("normal", 0, 10)
    items = [normal_item]
    GildedRose(items).update_quality()
    assert normal_item.quality == 8


def test_it_never_have_to_high_quality():
    normal_item = Normal("normal", 2, 51)
    items = [normal_item]
    GildedRose(items).update_quality()
    assert normal_item.quality == 50
