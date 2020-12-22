class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item_quality()


def create_item(name, sell_in, quality):
    if "Aged Brie" in name:
        item = AgedBrie(name, sell_in, quality)
    elif "Sulfuras" in name:
        item = Sulfuras(name, sell_in, quality)
    elif "Backstage pass" in name:
        item = BackstagePass(name, sell_in, quality)
    else:
        item = Normal(name, sell_in, quality)
    return item

class RawItem:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class Normal(RawItem):
    def update_item_quality(self):
        if 0 < self.quality:
            self.quality = self.quality - 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0 and 0 < self.quality:
            self.quality = self.quality - 1


class AgedBrie(RawItem):
    def update_item_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            if self.quality < 50:
                self.quality = self.quality + 1


class Sulfuras(RawItem):
    def update_item_quality(self):
        pass


class BackstagePass(RawItem):
    def update_item_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
            if self.sell_in < 11:
                if self.quality < 50:
                    self.quality = self.quality + 1
            if self.sell_in < 6:
                if self.quality < 50:
                    self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1
        if self.sell_in < 0:
            self.quality = self.quality - self.quality
