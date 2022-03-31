import scrapy

class ScratchQuotes(scrapy.Spider):
    name = 'sure'
    start_urls = [
        'https://www.sure.com.bo/categoria/portatiles-y-computadoras/',
    ]

    def parse(self,response):
        for div in response.css('.product-wrapper'):
            cssName =  div.css('.product-title a::text').get().strip()
            cssPrice1 = div.css('ins bdi::text').get()
            cssPrice2=div.css('bdi::text').get()

            cssImage = div.css('.product-image-link img::attr(src)').get().strip()
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
