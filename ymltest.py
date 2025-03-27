from ymlpylib import YML

a = YML()
a.shop('Test','test','http://test.com')
pictures = ['http://boyard.biz/pict1.jpg', 'http://boyard.biz/pict2.jpg']
params = {'param_name':"param value", 'param_name2':"param2 value value"}
offer = {'ID0':{'vendor':"Boyard", 'vendorCode':"ST000", 'pictures': pictures, 'params': params}}
a.add_offer(offer)
a.print()