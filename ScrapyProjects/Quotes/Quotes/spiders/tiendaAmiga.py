import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'tiendaAmiga'
    start_urls = [
        'https://www.tiendaamiga.com.bo/tecnologia.html',
    ]

    def parse(self,response):
        for div in response.css('.product-item-info'):
            cssName = '"' + div.css('.product-item-link::text').get().strip() + '"'
            cssPrice = div.css('.price::text').get().strip()
            cssImage = div.css('.product-image-photo::attr(src)').get().strip()
            yield{
                'Nombre':cssName,
                'Precio':cssPrice,
                'ImageUrl':cssImage
            }

        cssNextPage = response.css('a[title="Siguiente"]::attr(href)').get()
        if cssNextPage:
            yield response.follow(cssNextPage,callback=self.parse)
        else:
            print("No se encontro el elemento=======")
