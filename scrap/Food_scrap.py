from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

food_category_list = ['닭가슴살','다이어트식단도시락']
food_category_pages = {}


for food_category in food_category_list:
    url = f'https://www.coupang.com/np/search?component=&q={food_category}&channel=user'
    res = requests.get(url)
    text = res.text
    soup = BeautifulSoup(text, 'html.parser')
    all_page = soup.find('a', {'class':'btn-last disabled'}).text
    food_category_pages[food_category] = all_page


food_pages = []
for food_category, pages in food_category_pages.items():
    for page in range(1,int(pages)+1):
        url = f'https://www.coupang.com/np/search?component=&q={food_category}&channel=user&listSize=72&page={page}'
        res = requests.get(url)
        text = res.text
        soup = BeautifulSoup(text, 'html.parser')
        ul  = soup.find("ul", {"id":"productList"})
        food_pages.append(ul.select('li.search-product'))


#이름, 이미지소스, 정가, 할인가, 할인율, 평점, 리뷰수, 링크

for  food_page in food_pages:

    index = food_pages.index(food_page)

    category = food_category_list[index//27]



    for food in food_page:
        
        # 종류 
        print(category)


        #링크
        list_url = food.find('a', {'class':'search-product-link'})['href']
        link = f'coupang.com/{list_url}'
        print(link)

        #상품 이름
        name = food.find('div', {'class':'name'}).text.strip()
        print(name)
        
        #이미지 소스
        img = food.find('img', {'class':'search-product-wrap-img'})['src']
        
        #정가,할인가,할인율
        base_price = food.find('del', {'class':'base-price'})
        discount_rate = food.find('span', {'class':'instant-discount-rate'})
        final_price = food.find('strong', {'class':'price-value'}).text

        if discount_rate != None:

            discount_rate = discount_rate.text.replace('%','')
            base_price = base_price.text.strip()

            print(base_price)
            print(f'할인율 : {discount_rate}%')
            print(final_price)
        
        else:

            print(final_price)
            print(f'할인율 : 0%')
        
        #리뷰개수
        bracket = str.maketrans('()','  ')
        review_count = food.find('span', {'class':'rating-total-count'})
        if review_count == None :
            print('리뷰 : 0')
        else:
            review_count = review_count.text.translate(bracket).strip()
            product_reviews = review_count

            print(f'리뷰: {review_count}')
        #평점
        rate = food.find('em', {'class':'rating'})

        if rate == None:

            product_rate = 0
            
            print('평점 : 0')

        else:

            rate = rate.text
            product_rate = rate

            print(f'평점 : {rate}')
        print('-------------------------------------')
        print('-------------------------------------')

