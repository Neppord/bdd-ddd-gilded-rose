from gilded_rose import GildedRose, BackstagePass


def test_update_sell_in():
    backstage_pass_item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 2, 10)
    items = [backstage_pass_item]
    GildedRose(items).update_quality()
    assert backstage_pass_item.sell_in == 1


def test_it_increase_in_quality_at_normal_rate():
    backstage_pass_item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 11, 10)
    items = [backstage_pass_item]
    GildedRose(items).update_quality()
    assert backstage_pass_item.quality == 11


def test_it_increase_in_quality_at_double_rate_when_there_is_10_days_left():
    backstage_pass_item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 10, 10)
    items = [backstage_pass_item]
    GildedRose(items).update_quality()
    assert backstage_pass_item.quality == 12


def test_it_increase_in_quality_at_triple_rate_when_there_is_5_days_left():
    backstage_pass_item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 5, 10)
    items = [backstage_pass_item]
    GildedRose(items).update_quality()
    assert backstage_pass_item.quality == 13


def test_it_has_no_quality_after_its_sell_date():
    backstage_pass_item = BackstagePass("Backstage passes to a TAFKAL80ETC concert", 0, 10)
    items = [backstage_pass_item]
    GildedRose(items).update_quality()
    assert backstage_pass_item.quality == 0
