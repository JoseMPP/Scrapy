import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'dismac'
    start_urls = [
        'https://www.dismac.com.bo/categorias/51-tecnologia.html',
    ]

    def parse(self,response):
        for div in response.css('.recent-container'):
            cssName =  div.css('.product-item-link::text').get().strip()
            cssPrice1 = div.css('.bundle-price::text').get()
            cssPrice2=div.css('.int::text').get()

            cssImage = div.css('.img-product img::attr(src)').get().strip()
            if cssPrice1:
                precio=cssPrice1.strip()
            else:
                precio=cssPrice2.strip()
            yield{
                'Nombre':cssName,
                'Precio':precio,
                'ImageUrl':cssImage
            }
            print('Producto----------------------------------')
        print("Termina for----------------")
        cssNextPage = response.css('.next::attr(href)').get()

        if cssNextPage:
            print('----------Encuentra PAgina--------------')
            yield response.follow(cssNextPage,callback=self.parse)