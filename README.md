# DataMiningOnlineShoppingReviews
##########################################################################################################################
##															##
##					Measurement of Customer Satisfaction Using				 	##
##					User Comments of Products on Shopping Sites					##
##							Kagan Yavuz							##
##															##
##########################################################################################################################

***	Proje için C# dilinde basit bir arayüz tasarlanmıştır. "DataMiningOnlineShoppingReviews" klasörü içinden
***	"DataMiningOnlineShoppingReviews.exe" uygulaması açılarak sırayla "Get Dataset" - "Sentiment Analysis" ve 
***	"Keyword Analysis" butonlarına tıklayarak program çalıştırılabilir, sonuçlar ekranda görülebilir.

***	Projeyi arayüz olmadan çalıştırmak için :

Proje 3 aşamadan oluşmaktadır:
	1) Python Selenium ile Amazon.com sitesinden kullanıcı yorumlarını alıp bir .txt dosyasına kaydetmek
	2) Oluşturulan .txt dosyası kullanılarak Python TextBlob kütüphanesi ile sentiment analysis yapmak
	3) Oluşturulan .txt dosyası kullanılarak Python NLTK kütüphanesi ile datasetteki gereksiz kelimeler
	   ve bağlaçlar çıkarıldıktan sonra Python TextBlob kütüphanesi kullanılarak keyword analysis yapmak

1) Python Selenium ile Amazon.com sitesinden kullanıcı yorumlarını alıp bir .txt dosyasına kaydetmek :
	1.aşamada kodun çalıştırılacağı bilgisayarda python, selenium ve chromedriver yüklendikten sonra 
	"SeleniumProjectToGetData" projesi açılmalıdır. İlgili projenin main.py kodunun 10.satırında bilgisayara daha 
	önce yüklenmiş olan chromedriver'ın executable path'i verilmelidir.
	
	Sonra ilgili projenin main.py kodu çalıştırıldığında projenin ana dizininde "user_reviews.txt" isimli dosyanın 
	oluştuğu görülecektir. Bu dosya, "main.py" kodunun 17.satırında verilmiş olan Amazon.com linkindeki ürünün 
	kullanıcı yorumlarıdır.
	
	"user_reviews.txt" dosyası bu adımlar izlenerek oluşturulduktan sonra 2.aşamaya geçilebilir.

2) Oluşturulan .txt dosyası kullanılarak Python TextBlob kütüphanesi ile sentiment analysis yapmak :
	Projenin 2.aşamasında duygu analizi yapılmaktadır. 1.aşamada oluşturulan "user_reviews.txt" dosyası, 
	"TextBlobProjectToSentimentAnalysis" projesinin ana dizinine kopyalanarak "TextBlobProjectToSentimentAnalysis" 
	projesinin main.py kodu doğrudan çalıştırılabilir. 
	
	Bu projenin output'u olarak
		Duygu Skoru (polarity)
		Duygu Etiketi
		Konu Duyarlılık
	değerleri bulunacaktır.

3) Oluşturulan .txt dosyası kullanılarak Python NLTK kütüphanesi ile datasetteki gereksiz kelimeler ve bağlaçlar 
çıkarıldıktan sonra Python TextBlob kütüphanesi kullanılarak keyword analysis yapmak :
	Projenin 3.aşamasında ise keyword analysis yapılmaktadır. 1.aşamada oluşturulan "user_reviews.txt" dosyası, 
	"TextBlobProjectToKeywordAnalysis" projesinin ana dizinine kopyalanarak "TextBlobProjectToKeywordAnalysis" 
	projesinin main.py kodu doğrudan çalıştırılabilir.
	
	Bu projenin output'u olarak
		dataset'te en çok kullanılan kelimeler
		dataset'te en çok kullanılan 2'li kelime grupları
		dataset'te en çok kullanılan 3'lü kelime grupları
	değerleri bulunacaktır.

													Teşekkür ederim
												  Kağan Yavuz
