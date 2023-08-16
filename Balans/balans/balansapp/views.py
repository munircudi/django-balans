from django.http import HttpResponse
from django.shortcuts import render

data = {
    "brands":[
        {
            "title": "Fleetguard",
            "imageUrl": "service_img1.png",
            "description": "Fleetguard, dünya genelinde tanınan bir filtrasyon çözümleri sağlayıcısıdır. Şirket, özellikle ağır hizmet araçları, kamyonlar, otobüsler, inşaat makineleri, tarım ekipmanları ve jeneratörler gibi motorlu araçlar için filtreleme ve emisyon kontrol sistemleri üretmektedir.Fleetguard, 1963 yılında kurulmuş olup, Cummins Filtration'ın bir markasıdır. Cummins Filtration, dünya çapında bir lider olan Cummins Inc.'in bir yan kuruluşudur. Fleetguard, motor yağı filtreleri, yakıt filtreleri, hava filtreleri, hidrolik filtreler, soğutma sıvısı filtreleri ve egzoz sistemi filtreleri gibi çeşitli filtreleme çözümleri sunar. Fleetguard, yüksek kaliteli ve dayanıklı filtrelerin yanı sıra, motor performansını artırmak, yakıt verimliliğini artırmak ve emisyonları azaltmak için yenilikçi teknolojiler geliştirmektedir. Ayrıca, müşterilere ürünlerinin optimum performansını korumak ve araçların ömrünü uzatmak için teknik destek ve hizmetler sunmaktadır. Müşterilerine kaliteli filtrasyon çözümleri sağlama konusunda güvenilir bir markadır.",
            "slug": "Fleetguard",

        },
        {
            "title": "Donaldson Company",
            "imageUrl": "service_img2.png",
            "description": "Donaldson Company, dünya çapında bir filtrasyon çözümleri sağlayıcısıdır. Şirket, hava, yağ, yakıt, hidrolik ve emisyon sistemleri için filtrelerin tasarımı, üretimi ve dağıtımı konusunda uzmanlaşmıştır. Donaldson, 1915 yılında Amerika Birleşik Devletleri'nde kurulmuştur ve uzun bir geçmişe sahiptir. Şirket, çeşitli endüstrilerdeki müşterilerine çevre dostu, yüksek kaliteli ve dayanıklı filtrasyon çözümleri sunar. Bu endüstriler arasında otomotiv, inşaat, tarım, madencilik, enerji, denizcilik, havacılık ve sanayi gibi çeşitli sektörler bulunur.Donaldson filtreleri, partikül, su, yağ ve diğer kirleticileri etkin bir şekilde tutmak ve motorların performansını artırmak için tasarlanmıştır. Ayrıca, emisyon düzenlemelerine uyum sağlamak ve çevresel etkileri azaltmak için özel emisyon kontrol filtreleri de üretmektedir. Donaldson, müşteri ihtiyaçlarına yönelik geniş bir ürün yelpazesine sahiptir ve dünya genelindeki müşterilere hizmet veren bir küresel ağa sahiptir. Ayrıca, teknik destek, eğitim ve satış sonrası hizmetler gibi konularda müşterilerine destek sağlamaktadır. Donaldson, inovasyon ve teknolojik gelişmelerde sürekli olarak ilerlemeyi hedefler. Yenilikçi ürünler ve çözümler geliştirmek için AR-GE çalışmalarına büyük önem verir. Müşterilerine daha verimli, güvenilir ve çevre dostu filtrasyon çözümleri sunma konusunda taahhütte bulunur. Donaldson Company, filtrasyon endüstrisinde güvenilir bir marka olarak bilinir ve müşterilere çeşitli uygulamalar için kaliteli ve güvenilir filtreler sunar.",
            "slug": "Donaldson-Company",

        },
        {
            "title": "Mann Hummel",
            "imageUrl": "service_img3.png",
            "description":"Mann+Hummel, otomotiv ve endüstriyel uygulamalar için filtreleme çözümleri sağlayan bir şirkettir. 1941 yılında Almanya'da kurulan Mann+Hummel, dünya çapında tanınmış ve önde gelen bir filtre üreticisidir. Şirket, hava, yağ, yakıt, iç mekan ve endüstriyel filtreler gibi çeşitli filtre türlerinin tasarımı, üretimi ve dağıtımı konusunda uzmanlaşmıştır. Bu filtreler, otomobiller, kamyonlar, inşaat makineleri, endüstriyel makineler ve diğer birçok uygulama için kullanılır. Mann+Hummel, yüksek kaliteli filtrelerin yanı sıra emme sistemleri, sıvı yönetimi teknolojileri, plastik bileşenler ve kabin hava kalitesi ürünleri gibi çeşitli otomotiv bileşenleri de üretir. Şirket, müşterilerinin ihtiyaçlarına yönelik özelleştirilmiş çözümler sunar ve kalite, performans ve sürdürülebilirlik konularında ön planda olan yenilikçi ürünler geliştirir. Mann+Hummel, dünya genelinde birçok ülkede üretim tesislerine ve satış ofislerine sahiptir. Ayrıca, otomobil üreticilerine (OEM'ler), yedek parça pazarına ve satış sonrası servis sektörüne filtreler ve bileşenler sağlar. Sürdürülebilirlik, Mann+Hummel'in iş faaliyetlerinin önemli bir parçasıdır. Şirket, çevresel etkisini azaltmaya odaklanarak enerji verimliliğini artırır, atıkları azaltır ve sürdürülebilir üretim süreçlerini benimser. Mann+Hummel, uzun bir geçmişe ve otomotiv endüstrisindeki güçlü bir varlığa sahip bir filtre firmasıdır. Kaliteli ürünleri ve yenilikçi çözümleriyle müşterilerin beklentilerini karşılamayı hedefler. ",
            "slug": "Mann-Hummel",

        },
        {
            "title": "Jungheinrich",
            "imageUrl": "service_img4.png",
            "description":"Jungheinrich, Almanya merkezli bir endüstriyel araç ve depolama sistemleri üreticisidir. 1953 yılında kurulan şirket, dünya çapında tanınmış bir marka haline gelmiştir.Jungheinrich, malzeme taşıma ekipmanları ve depolama sistemleri konusunda uzmandır. Forkliftler, depolama ve istifleme sistemleri, palet taşıma sistemleri, otomatik depolama çözümleri, lojistik yazılımlar ve hizmetler gibi çeşitli ürün ve hizmetleri sunar.Şirket, yüksek kaliteli ve yenilikçi ürünler üretmeye odaklanır. Forkliftlerde elektrikli, LPG ve dizel motorlu seçenekler sunar ve geniş bir model yelpazesine sahiptir. Ayrıca, otomatik yönetim sistemleri ve depolama raf sistemleri gibi depolama ve lojistik çözümlerinde de liderdir. Jungheinrich, müşterilerine geniş bir endüstriyel sektöre hitap eden çözümler sunar. Üretim tesislerinden lojistik merkezlerine, perakende sektöründen gıda endüstrisine kadar birçok sektörde faaliyet gösteren şirketlerle işbirliği yapar. Sürdürülebilirlik, Jungheinrich'in iş faaliyetlerinin önemli bir parçasıdır. Şirket, enerji verimliliğini artıran çözümler sunar, atıkları azaltır ve geri dönüşüme odaklanır. Ayrıca, elektrikli forkliftler ve diğer elektrikli araçlarla çevresel etkisini azaltmayı hedefler. Jungheinrich, müşterilere satış öncesi danışmanlık, satış sonrası destek, yedek parça ve servis hizmetleri sunarak güçlü bir müşteri ağına sahiptir. Ayrıca, dünya genelindeki birçok ülkede üretim tesislerine, satış ofislerine ve hizmet noktalarına sahiptir. Özetlemek gerekirse, Jungheinrich, endüstriyel araçlar ve depolama sistemleri konusunda lider bir şirkettir. Yüksek kaliteli ürünleri, yenilikçi çözümleri ve müşteri odaklı hizmetleriyle tanınır.",
            "slug": "Jungheinrich",

        },
        {
            "title": "Hyster",
            "imageUrl": "service_img5.png",
            "description": "Hyster, malzeme taşıma ekipmanları alanında faaliyet gösteren köklü bir şirkettir. Şirket, 1929 yılında Amerika Birleşik Devletleri'nde kurulmuş olup, dünya genelinde tanınmış bir markadır.Hyster, çeşitli endüstrilerde malzeme taşıma ekipmanları üretmektedir. Ürün yelpazesi arasında forkliftler, elleçleme makineleri, istifleme makineleri, palet kamyonları, römorklar ve ağır yük ekipmanları gibi çeşitli ekipmanlar bulunmaktadır. Bu ekipmanlar, depolama, lojistik, dağıtım merkezleri, üretim tesisleri ve diğer endüstriyel alanlarda malzeme taşıma ihtiyaçlarını karşılamak için kullanılmaktadır.Hyster, dayanıklılık, güvenilirlik ve performans konusunda bilinir. Şirket, müşterilere verimlilik, emniyet ve kullanıcı dostu çözümler sunmayı hedefler. İnovasyon ve mühendislik mükemmeliyetine odaklanarak, müşteri ihtiyaçlarına uygun ekipmanlar geliştirmektedir.Hyster ayrıca satış sonrası hizmetler ve müşteri desteği konusunda da güçlü bir altyapıya sahiptir. Bakım, onarım, yedek parça tedariki ve eğitim gibi konularda müşterilere kapsamlı destek sunmaktadır. Hyster'in küresel bir bayi ağı bulunmaktadır, böylece müşterilerin ihtiyaçlarına hızlı ve etkili bir şekilde yanıt verebilmektedir.Hyster, dünya genelinde faaliyet gösteren bir şirkettir ve müşterilere uluslararası pazarda geniş bir erişim sağlamaktadır. Şirket, birçok endüstrideki müşterilerin malzeme taşıma ihtiyaçlarını karşılayan güvenilir bir marka olarak tanınmaktadır.Hyster, malzeme taşıma ekipmanları konusunda uzmanlaşmış köklü bir şirkettir. Geniş ürün yelpazesi, dayanıklılık ve güvenilirlik ile bilinir. Müşteri odaklı çözümler sunmayı hedefler ve satış sonrası hizmetler konusunda kapsamlı bir destek sağlar. Dünya genelindeki müşterilere malzeme taşıma konusunda çözümler sunan önde gelen bir markadır.",
            "slug": "Hyster",

        },
        {
            "title": "Linde Material Handling",
            "imageUrl": "service_img6.png",
            "description":" Linde Material Handling, malzeme taşıma ekipmanları alanında dünya çapında tanınan bir şirkettir. İşletmelerin depolama, lojistik ve malzeme taşıma ihtiyaçlarını karşılamak için geniş bir ürün ve hizmet yelpazesi sunmaktadır. Linde Material Handling, Alman kökenli bir şirkettir ve 1904 yılında kurulmuştur. Şirket, forkliftler, palet kamyonları, elleçleme makineleri, istifleme makineleri ve depolama sistemleri gibi çeşitli malzeme taşıma ekipmanları üretmektedir. Bu ekipmanlar, fabrikalar, depolama tesisleri, dağıtım merkezleri ve diğer endüstriyel alanlarda kullanılmaktadır. Linde Material Handling, yenilikçi teknolojileri ve ergonomik tasarımlarıyla dikkat çeker. Ürünlerindeki ileri teknolojiler, enerji verimliliği, operasyonel güvenlik ve kullanıcı dostu özellikler sağlar. Linde, müşterilere daha yüksek verimlilik, daha az enerji tüketimi ve daha iyi işçi performansı gibi avantajlar sunmayı hedefler. Şirket ayrıca dijitalleşme ve akıllı lojistik çözümleri konusunda da öncüdür. Linde Connected Solutions adı altında, ekipmanların izlenmesi, verimlilik analizi, bakım yönetimi ve operasyonel verimlilik gibi alanlarda dijital çözümler sunmaktadır. Bu sayede müşteriler, operasyonlarını optimize etme ve maliyetleri düşürme imkanına sahip olurlar. Linde Material Handling, müşteri memnuniyetine büyük önem verir ve satış sonrası hizmetlere odaklanır. Küresel bir servis ağı ile bakım, onarım, yedek parça tedariki ve eğitim gibi konularda müşterilere kapsamlı destek sunmaktadır. Ayrıca, müşterilerin ihtiyaçlarına özel çözümler ve danışmanlık hizmetleri de sağlamaktadır. Linde Material Handling, dünya genelinde geniş bir müşteri tabanına sahiptir ve çeşitli endüstrilerde kullanılan ekipmanlar sağlamaktadır. Otomotiv, lojistik, perakende, gıda, kimya ve enerji sektörleri gibi birçok sektörde faaliyet gösteren müşterilere hizmet vermektedir. Linde Material Handling, malzeme taşıma ekipmanları alanında önde gelen bir şirkettir. Geniş ürün yelpazesi, yenilikçi teknolojiler ve müşteri odaklı hizmetleri ile tanınır. Dijital çözümler ve akıllı lojistik çözümleri konusunda da öncüdür. Müşteri memnuniyetine önem veren Linde, endüstrilerin malzeme taşıma ihtiyaçlarını karşılamak için güvenilir ve verimli çözümler sunar.",
            "slug": "Linde-Material-Handling",
        },
        {
            "title": "STILL GmbH",
            "imageUrl": "service_img7.png",
            "description": " STILL GmbH, malzeme taşıma ekipmanları alanında faaliyet gösteren bir Alman şirketidir. 1920 yılında kurulmuş olan STILL, dünya çapında tanınmış bir markadır. STILL, geniş bir ürün yelpazesine sahiptir ve forkliftler, istifleme makineleri, elleçleme makineleri, depolama sistemleri ve lojistik çözümleri gibi çeşitli malzeme taşıma ekipmanları üretmektedir. Bu ekipmanlar, endüstriyel tesislerde, depolama alanlarında, lojistik merkezlerinde ve dağıtım ağlarında kullanılmaktadır.Şirket, yenilikçilik ve teknolojik gelişmelere odaklanarak müşterilerine verimli ve güvenilir çözümler sunmayı hedeflemektedir. STILL'in ürünleri, operasyonel verimlilik, ergonomi, enerji tasarrufu ve işçi güvenliği gibi konularda üstün performans gösterir. Ayrıca, dijitalleşme ve akıllı lojistik çözümleri de sunarak müşterilere daha iyi kontrol ve verimlilik sağlamaktadır. STILL, müşteri memnuniyetine büyük önem verir ve satış sonrası hizmetler konusunda kapsamlı bir destek sunar. Bakım, onarım, yedek parça tedariki ve eğitim gibi alanlarda müşterilere güvenilir bir hizmet ağı sağlar. Ayrıca, müşterilerin ihtiyaçlarına özel çözümler sunmak için danışmanlık hizmetleri de sunmaktadır.STILL, küresel bir şirket olup dünya genelinde birçok ülkede üretim tesisleri, satış ofisleri ve bayileri bulunmaktadır. Müşteri tabanı çeşitli sektörlerden gelmektedir ve otomotiv, lojistik, perakende, gıda, kimya ve enerji gibi sektörlerde faaliyet gösteren şirketlere hizmet vermektedir. STILL GmbH, malzeme taşıma ekipmanları konusunda köklü bir Alman şirketidir. Geniş ürün yelpazesi, yenilikçi teknolojiler ve müşteri odaklı hizmetleriyle tanınır. Müşterilerine verimli ve güvenilir çözümler sunarak operasyonel verimliliği artırmayı hedefler. STILL, güçlü bir satış sonrası hizmet ağıyla müşteri memnuniyetini ön planda tutar ve dünya genelinde geniş bir müşteri tabanına hizmet verir.",
            "slug": "STILL-GmbH",
        },
        {
            "title": "Michelin",
            "imageUrl": "service_img8.png",
            "description":" Michelin, dünya çapında bilinen bir lastik üreticisidir ve endüstriyel sektörlerde kullanılan çeşitli lastiklerin yanı sıra otomobil lastikleriyle de tanınmıştır. Michelin, 1889 yılında Fransa'da kurulmuştur. Şirket, otomobil lastikleri, kamyon ve ticari araç lastikleri, tarım makineleri lastikleri, inşaat ekipmanı lastikleri, hava taşıtları lastikleri, endüstriyel ekipman lastikleri ve diğer özel uygulama lastikleri gibi geniş bir ürün yelpazesine sahiptir. Endüstriyel sektörlerde kullanılan Michelin lastikleri, dayanıklılık, performans ve güvenlik özellikleriyle tanınır. Bu lastikler, inşaat, madencilik, tarım, liman ve taşımacılık gibi ağır hizmet uygulamalarında kullanılmak üzere tasarlanmıştır. Michelin, yüksek kalite standartlarına bağlı kalarak inovasyon ve teknolojiye önem verir. Araştırma ve geliştirme çalışmalarına büyük yatırımlar yaparak lastiklerin performansını, yakıt verimliliğini ve sürüş konforunu artırmak için sürekli olarak yeni teknolojiler geliştirir. Sürdürülebilirlik, Michelin'in iş felsefesinin önemli bir parçasıdır. Şirket, lastiklerin daha uzun ömürlü olmasını ve yakıt tüketimini azaltmasını sağlamak için yenilikçi tasarımlar ve sürdürülebilir malzemeler kullanır. Ayrıca, geri dönüşüm ve atık yönetimi konularında da çevresel sorumluluk alır. Michelin, müşterilere satış sonrası destek, teknik danışmanlık ve hizmetler gibi kapsamlı çözümler sunar. Ayrıca, dünya genelinde birçok ülkede üretim tesislerine, satış ofislerine ve servis noktalarına sahip olan uluslararası bir şirkettir. Özetlemek gerekirse, Michelin, endüstriyel sektörlerde kullanılan çeşitli lastiklerin yanı sıra otomobil lastikleri konusunda da önde gelen bir markadır. Yüksek kalite, performans, sürdürülebilirlik ve müşteri odaklı hizmetler Michelin'in temel değerleridir.",
            "slug": "Michelin",
         },
        {
            "title": "Trelleborg",
            "imageUrl": "service_img9.png",
            "description":" Trelleborg, İsveç merkezli bir endüstriyel lastik üreticisidir. Şirket, geniş bir ürün yelpazesine sahip olan ve çeşitli sektörlerde kullanılan lastiklerin üretiminde uzmanlaşmıştır. Trelleborg, tarım, inşaat, madencilik, malzeme taşıma, denizcilik, havacılık ve diğer endüstriyel uygulamalar için lastikler sunar. Bu lastikler, araçlar, makineler ve ekipmanlar için dayanıklılık, performans ve güvenlik sağlar. Tarım lastikleri, Trelleborg'un önemli bir uzmanlık alanıdır. Şirket, traktörler, biçerdöverler, tarım makineleri ve diğer tarımsal araçlar için özel olarak tasarlanmış lastikler üretir. Bu lastikler, tarım faaliyetlerinde çekiş gücü, toprak koruması ve iş verimliliği sağlamak üzere optimize edilmiştir. Trelleborg, yenilikçi tasarım ve teknolojilere önem verir. Araştırma ve geliştirme çalışmalarıyla sürekli olarak yeni lastik çözümleri geliştirir ve müşterilere en son teknolojileri sunar. Ayrıca, yakıt verimliliğini artırmak ve çevresel etkisini azaltmak için sürdürülebilirlik konularında da çalışmalar yapar. Müşterilere satış öncesi danışmanlık, teknik destek, servis hizmetleri ve yedek parçalar gibi kapsamlı çözümler sunan Trelleborg, müşteri memnuniyetine büyük önem verir. Şirket, uluslararası bir varlığa sahip olup dünya genelindeki birçok ülkede üretim tesislerine, satış ofislerine ve hizmet noktalarına sahiptir. Özetlemek gerekirse, Trelleborg, endüstriyel sektörlerde kullanılan geniş bir lastik ürün yelpazesine sahip olan bir şirkettir. Dayanıklılık, performans, inovasyon ve müşteri odaklı hizmetler Trelleborg'un iş felsefesinin önemli bir parçasıdır.",
            "slug": "Trelleborg",
         }

    ]
}


# Create your views here.
def index(request):
    marka = data["brands"]

    return render(request, 'index.html', {
        "marka": marka
    })


def balansapp(request):
    return render(request, 'markalar.html' ,data)


def balansapp_details(request,name):
    tmp_data = {};
    for brand in data['brands']:
        if brand["slug"] == name:
            tmp_data = brand
    return render(request, 'markalar-details.html', {'brand': tmp_data})


def about(request):
    return render(request, 'about.html')
