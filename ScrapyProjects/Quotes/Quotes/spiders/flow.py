import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'flow'
    start_urls = [
        'https://www.flow.bo/electronicos-bolivia.html',
    ]

    def parse(self,response):
        for div in response.css('li[class="item product product-item"]'):
            cssName =  div.css('.product-item-link::text').get().strip()
            cssPrice = div.css('.price::text').get().strip()
            cssImage = div.css('.product-image-photo::attr(src)').get().strip()
            yield{
                'Nombre':cssName,
                'Precio':cssPrice,
                'ImageUrl':cssImage
            }
            print('Producto----------------------------------')
        print("Termina for----------------")
        cssNextPage = response.css('a[title="Siguiente"]::attr(href)').get()

        if cssNextPage:
            print('----------Encuentra PAgina--------------')
            yield response.follow(cssNextPage,callback=self.parse)