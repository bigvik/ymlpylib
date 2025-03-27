

class YML:

	def __init__(self, filename=''):
		import xml.etree.ElementTree as ET
		from datetime import datetime as DT
		self.DT = DT
		self.ET = ET
		if filename:
			self.ymltree = ET.parse(filename)
			self.root = self.ymltree.getroot()
		else:
			self.root = self.ET.Element('yml_catalog')
		self.offerlist = []

	def __finally(self):
		if not self.offerlist:
			return
		self.root.set('date', self.DT.now().strftime('%Y-%m-%d %H:%M'))
		for el in self.offerlist:
			offer = self.ET.SubElement(self.offers, 'offer')
			offer_id = list(el.keys())[0]
			offer.set('id', offer_id)
			for key, value in el[offer_id].items():
				if key == 'pictures':
					for pict in value:
						p = self.ET.SubElement(offer, 'picture')
						p.text = pict
					continue
				if key == 'params':
					for name, text in value.items():
						p = self.ET.SubElement(offer, 'param')
						p.set('name', name)
						p.text = text
					continue
				k = self.ET.SubElement(offer, key)
				k.text = value
		self.ymltree = self.ET.ElementTree(self.root)

	def shop(self, name='', company='', url='http://'):
		"""

		"""
		self.shop = self.ET.SubElement(self.root, 'shop')
		self.name = self.ET.SubElement(self.shop, 'name')
		self.name.text = name
		self.company = self.ET.SubElement(self.shop, 'company')
		self.company.text = company
		self.url = self.ET.SubElement(self.shop, 'url')
		self.url.text = url
		self.offers = self.ET.SubElement(self.shop, 'offers')

	def add_offer(self, offer):
		self.offerlist.append(offer)

	def write(self, filename='offers.xml'):
		"""
		Write to file (default: offers.xml): .write(filename)
		"""
		self.__finally()
		self.ymltree.write(filename, encoding="utf-8", xml_declaration=True)

	def print(self):
		self.__finally()
		print(self.ET.tostring(self.root, encoding="utf-8", xml_declaration=True))


if __name__ == '__main__':
    pass