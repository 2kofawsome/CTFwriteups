Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> string1 = "unprrntvvr"
>>> strign2 = "haceeagiie"
>>> finals = []
>>> finals.append("")
>>> newfinals = [""]
>>> for n in range(len(string1)):
	finals = newfinals[:]
	newfinals = []
	for x in finals:
		newfinals.append(x+string1[n])
		newfinals.append(x+strign2[n])

		
>>> print(finals)
['unprrntvv', 'unprrntvi', 'unprrntiv', 'unprrntii', 'unprrngvv', 'unprrngvi', 'unprrngiv', 'unprrngii', 'unprratvv', 'unprratvi', 'unprrativ', 'unprratii', 'unprragvv', 'unprragvi', 'unprragiv', 'unprragii', 'unprentvv', 'unprentvi', 'unprentiv', 'unprentii', 'unprengvv', 'unprengvi', 'unprengiv', 'unprengii', 'unpreatvv', 'unpreatvi', 'unpreativ', 'unpreatii', 'unpreagvv', 'unpreagvi', 'unpreagiv', 'unpreagii', 'unperntvv', 'unperntvi', 'unperntiv', 'unperntii', 'unperngvv', 'unperngvi', 'unperngiv', 'unperngii', 'unperatvv', 'unperatvi', 'unperativ', 'unperatii', 'unperagvv', 'unperagvi', 'unperagiv', 'unperagii', 'unpeentvv', 'unpeentvi', 'unpeentiv', 'unpeentii', 'unpeengvv', 'unpeengvi', 'unpeengiv', 'unpeengii', 'unpeeatvv', 'unpeeatvi', 'unpeeativ', 'unpeeatii', 'unpeeagvv', 'unpeeagvi', 'unpeeagiv', 'unpeeagii', 'uncrrntvv', 'uncrrntvi', 'uncrrntiv', 'uncrrntii', 'uncrrngvv', 'uncrrngvi', 'uncrrngiv', 'uncrrngii', 'uncrratvv', 'uncrratvi', 'uncrrativ', 'uncrratii', 'uncrragvv', 'uncrragvi', 'uncrragiv', 'uncrragii', 'uncrentvv', 'uncrentvi', 'uncrentiv', 'uncrentii', 'uncrengvv', 'uncrengvi', 'uncrengiv', 'uncrengii', 'uncreatvv', 'uncreatvi', 'uncreativ', 'uncreatii', 'uncreagvv', 'uncreagvi', 'uncreagiv', 'uncreagii', 'uncerntvv', 'uncerntvi', 'uncerntiv', 'uncerntii', 'uncerngvv', 'uncerngvi', 'uncerngiv', 'uncerngii', 'unceratvv', 'unceratvi', 'uncerativ', 'unceratii', 'unceragvv', 'unceragvi', 'unceragiv', 'unceragii', 'unceentvv', 'unceentvi', 'unceentiv', 'unceentii', 'unceengvv', 'unceengvi', 'unceengiv', 'unceengii', 'unceeatvv', 'unceeatvi', 'unceeativ', 'unceeatii', 'unceeagvv', 'unceeagvi', 'unceeagiv', 'unceeagii', 'uaprrntvv', 'uaprrntvi', 'uaprrntiv', 'uaprrntii', 'uaprrngvv', 'uaprrngvi', 'uaprrngiv', 'uaprrngii', 'uaprratvv', 'uaprratvi', 'uaprrativ', 'uaprratii', 'uaprragvv', 'uaprragvi', 'uaprragiv', 'uaprragii', 'uaprentvv', 'uaprentvi', 'uaprentiv', 'uaprentii', 'uaprengvv', 'uaprengvi', 'uaprengiv', 'uaprengii', 'uapreatvv', 'uapreatvi', 'uapreativ', 'uapreatii', 'uapreagvv', 'uapreagvi', 'uapreagiv', 'uapreagii', 'uaperntvv', 'uaperntvi', 'uaperntiv', 'uaperntii', 'uaperngvv', 'uaperngvi', 'uaperngiv', 'uaperngii', 'uaperatvv', 'uaperatvi', 'uaperativ', 'uaperatii', 'uaperagvv', 'uaperagvi', 'uaperagiv', 'uaperagii', 'uapeentvv', 'uapeentvi', 'uapeentiv', 'uapeentii', 'uapeengvv', 'uapeengvi', 'uapeengiv', 'uapeengii', 'uapeeatvv', 'uapeeatvi', 'uapeeativ', 'uapeeatii', 'uapeeagvv', 'uapeeagvi', 'uapeeagiv', 'uapeeagii', 'uacrrntvv', 'uacrrntvi', 'uacrrntiv', 'uacrrntii', 'uacrrngvv', 'uacrrngvi', 'uacrrngiv', 'uacrrngii', 'uacrratvv', 'uacrratvi', 'uacrrativ', 'uacrratii', 'uacrragvv', 'uacrragvi', 'uacrragiv', 'uacrragii', 'uacrentvv', 'uacrentvi', 'uacrentiv', 'uacrentii', 'uacrengvv', 'uacrengvi', 'uacrengiv', 'uacrengii', 'uacreatvv', 'uacreatvi', 'uacreativ', 'uacreatii', 'uacreagvv', 'uacreagvi', 'uacreagiv', 'uacreagii', 'uacerntvv', 'uacerntvi', 'uacerntiv', 'uacerntii', 'uacerngvv', 'uacerngvi', 'uacerngiv', 'uacerngii', 'uaceratvv', 'uaceratvi', 'uacerativ', 'uaceratii', 'uaceragvv', 'uaceragvi', 'uaceragiv', 'uaceragii', 'uaceentvv', 'uaceentvi', 'uaceentiv', 'uaceentii', 'uaceengvv', 'uaceengvi', 'uaceengiv', 'uaceengii', 'uaceeatvv', 'uaceeatvi', 'uaceeativ', 'uaceeatii', 'uaceeagvv', 'uaceeagvi', 'uaceeagiv', 'uaceeagii', 'hnprrntvv', 'hnprrntvi', 'hnprrntiv', 'hnprrntii', 'hnprrngvv', 'hnprrngvi', 'hnprrngiv', 'hnprrngii', 'hnprratvv', 'hnprratvi', 'hnprrativ', 'hnprratii', 'hnprragvv', 'hnprragvi', 'hnprragiv', 'hnprragii', 'hnprentvv', 'hnprentvi', 'hnprentiv', 'hnprentii', 'hnprengvv', 'hnprengvi', 'hnprengiv', 'hnprengii', 'hnpreatvv', 'hnpreatvi', 'hnpreativ', 'hnpreatii', 'hnpreagvv', 'hnpreagvi', 'hnpreagiv', 'hnpreagii', 'hnperntvv', 'hnperntvi', 'hnperntiv', 'hnperntii', 'hnperngvv', 'hnperngvi', 'hnperngiv', 'hnperngii', 'hnperatvv', 'hnperatvi', 'hnperativ', 'hnperatii', 'hnperagvv', 'hnperagvi', 'hnperagiv', 'hnperagii', 'hnpeentvv', 'hnpeentvi', 'hnpeentiv', 'hnpeentii', 'hnpeengvv', 'hnpeengvi', 'hnpeengiv', 'hnpeengii', 'hnpeeatvv', 'hnpeeatvi', 'hnpeeativ', 'hnpeeatii', 'hnpeeagvv', 'hnpeeagvi', 'hnpeeagiv', 'hnpeeagii', 'hncrrntvv', 'hncrrntvi', 'hncrrntiv', 'hncrrntii', 'hncrrngvv', 'hncrrngvi', 'hncrrngiv', 'hncrrngii', 'hncrratvv', 'hncrratvi', 'hncrrativ', 'hncrratii', 'hncrragvv', 'hncrragvi', 'hncrragiv', 'hncrragii', 'hncrentvv', 'hncrentvi', 'hncrentiv', 'hncrentii', 'hncrengvv', 'hncrengvi', 'hncrengiv', 'hncrengii', 'hncreatvv', 'hncreatvi', 'hncreativ', 'hncreatii', 'hncreagvv', 'hncreagvi', 'hncreagiv', 'hncreagii', 'hncerntvv', 'hncerntvi', 'hncerntiv', 'hncerntii', 'hncerngvv', 'hncerngvi', 'hncerngiv', 'hncerngii', 'hnceratvv', 'hnceratvi', 'hncerativ', 'hnceratii', 'hnceragvv', 'hnceragvi', 'hnceragiv', 'hnceragii', 'hnceentvv', 'hnceentvi', 'hnceentiv', 'hnceentii', 'hnceengvv', 'hnceengvi', 'hnceengiv', 'hnceengii', 'hnceeatvv', 'hnceeatvi', 'hnceeativ', 'hnceeatii', 'hnceeagvv', 'hnceeagvi', 'hnceeagiv', 'hnceeagii', 'haprrntvv', 'haprrntvi', 'haprrntiv', 'haprrntii', 'haprrngvv', 'haprrngvi', 'haprrngiv', 'haprrngii', 'haprratvv', 'haprratvi', 'haprrativ', 'haprratii', 'haprragvv', 'haprragvi', 'haprragiv', 'haprragii', 'haprentvv', 'haprentvi', 'haprentiv', 'haprentii', 'haprengvv', 'haprengvi', 'haprengiv', 'haprengii', 'hapreatvv', 'hapreatvi', 'hapreativ', 'hapreatii', 'hapreagvv', 'hapreagvi', 'hapreagiv', 'hapreagii', 'haperntvv', 'haperntvi', 'haperntiv', 'haperntii', 'haperngvv', 'haperngvi', 'haperngiv', 'haperngii', 'haperatvv', 'haperatvi', 'haperativ', 'haperatii', 'haperagvv', 'haperagvi', 'haperagiv', 'haperagii', 'hapeentvv', 'hapeentvi', 'hapeentiv', 'hapeentii', 'hapeengvv', 'hapeengvi', 'hapeengiv', 'hapeengii', 'hapeeatvv', 'hapeeatvi', 'hapeeativ', 'hapeeatii', 'hapeeagvv', 'hapeeagvi', 'hapeeagiv', 'hapeeagii', 'hacrrntvv', 'hacrrntvi', 'hacrrntiv', 'hacrrntii', 'hacrrngvv', 'hacrrngvi', 'hacrrngiv', 'hacrrngii', 'hacrratvv', 'hacrratvi', 'hacrrativ', 'hacrratii', 'hacrragvv', 'hacrragvi', 'hacrragiv', 'hacrragii', 'hacrentvv', 'hacrentvi', 'hacrentiv', 'hacrentii', 'hacrengvv', 'hacrengvi', 'hacrengiv', 'hacrengii', 'hacreatvv', 'hacreatvi', 'hacreativ', 'hacreatii', 'hacreagvv', 'hacreagvi', 'hacreagiv', 'hacreagii', 'hacerntvv', 'hacerntvi', 'hacerntiv', 'hacerntii', 'hacerngvv', 'hacerngvi', 'hacerngiv', 'hacerngii', 'haceratvv', 'haceratvi', 'hacerativ', 'haceratii', 'haceragvv', 'haceragvi', 'haceragiv', 'haceragii', 'haceentvv', 'haceentvi', 'haceentiv', 'haceentii', 'haceengvv', 'haceengvi', 'haceengiv', 'haceengii', 'haceeatvv', 'haceeatvi', 'haceeativ', 'haceeatii', 'haceeagvv', 'haceeagvi', 'haceeagiv', 'haceeagii']
>>> import time
>>> for n in finals:
	print(n)
	time.sleep(.5)

	
unprrntvv
unprrntvi
unprrntiv
unprrntii
unprrngvv
unprrngvi
unprrngiv
unprrngii
unprratvv
unprratvi
unprrativ
unprratii
Traceback (most recent call last):
  File "<pyshell#29>", line 2, in <module>
    print(n)
KeyboardInterrupt
>>> for n in finals:
	print(n)
	time.sleep(.25)

	
unprrntvv
unprrntvi
unprrntiv
unprrntii
unprrngvv
unprrngvi
unprrngiv
unprrngii
unprratvv
unprratvi
unprrativ
unprratii
unprragvv
unprragvi
unprragiv
unprragii
unprentvv
unprentvi
unprentiv
unprentii
unprengvv
unprengvi
unprengiv
unprengii
unpreatvv
unpreatvi
unpreativ
unpreatii
unpreagvv
unpreagvi
unpreagiv
unpreagii
unperntvv
unperntvi
unperntiv
unperntii
unperngvv
unperngvi
unperngiv
unperngii
unperatvv
unperatvi
unperativ
unperatii
unperagvv
unperagvi
unperagiv
unperagii
unpeentvv
unpeentvi
unpeentiv
unpeentii
unpeengvv
unpeengvi
unpeengiv
unpeengii
unpeeatvv
unpeeatvi
unpeeativ
unpeeatii
unpeeagvv
unpeeagvi
unpeeagiv
unpeeagii
uncrrntvv
uncrrntvi
uncrrntiv
uncrrntii
uncrrngvv
uncrrngvi
uncrrngiv
uncrrngii
uncrratvv
uncrratvi
uncrrativ
uncrratii
uncrragvv
uncrragvi
uncrragiv
uncrragii
uncrentvv
uncrentvi
uncrentiv
uncrentii
uncrengvv
uncrengvi
uncrengiv
uncrengii
uncreatvv
uncreatvi
uncreativ
