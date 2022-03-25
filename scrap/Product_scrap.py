from bs4 import BeautifulSoup
import requests

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

categorys = [329251,329226,329240,329279,329294,329323]
category_list = ['근력운동','요가/필라테스','요가복','유산소운동','스트레칭/균형','헬스소품/보호대']

''' 카테고리
근력운동 : 329251
요가/필라테스 : 329226
요가복 : 329240
유산소운동 : 329279
스트레칭/균형 : 329294
헬스소품/보호대 : 329323
'''


all_product_page = []
product_data = []


for category in categorys:
    for i in range(1,22):
        url = f'https://www.coupang.com/np/categories/{category}?page={i}&listSize=120'
        res = requests.get(url)
        text = res.text
        soup = BeautifulSoup(text)
        product_check = soup.find('p', {'class':'no-list-item'})
        if product_check == None:
            ul  = soup.find("ul", {"id":"productList"})
            all_product_page.append(ul.select('li.renew-badge'))
        else:
            break


# 상품이름 , 종류 , 링크 , 할인 , 정상가 , 할인가 , 리뷰개수 , 평점 , 이미지 소스



for page_list in all_product_page:
    index = all_product_page.index(page_list)//17
    
    for page in page_list:
        #링크
        list_url = list.find('a', {'class':'baby-product-link'})['href']
        link = f'coupang.com/{list_url}'
        print(link)

        #상품 이름
        product_name = list.find('div', {'class':'name'}).text.strip().replace(' ','')
        print(product_name)

        # 가격과 할인율
        base_price = list.find('del', {'class':'base-price'})
        final_price = list.find('strong', {'class':'price-value'}).text
        discount_rate = list.find('span', {'class':'discount-percentage'})

        if discount_rate != None:

            discount_rate = discount_rate.text.replace('%','')
            base_price = base_price.text.strip()

            product_base_price = base_price
            product_discount_rate = discount_rate
            product_final_price = final_price

            print(base_price)
            print(f'할인율 : {discount_rate}%')

        else:

            product_base_price = final_price
            product_final_price = final_price
            product_discount_rate = 0

            print(final_price)
            print('할인율 : 0%')

        #리뷰개수
        bracket = str.maketrans('()','  ')
        review_count = list.find('span', {'class':'rating-total-count'})
        if review_count == None :
            product_reviews = 0
            print('리뷰: 0')

        else:
            review_count = review_count.text.translate(bracket).strip()
            product_reviews = review_count

            print(f'리뷰: {review_count}')
        #평점
        rate = list.find('em', {'class':'rating'})

        if rate == None:

            product_rate = 0
            
            print('평점 : 0')

        else:

            rate = rate.text
            product_rate = rate

            print(f'평점 : {rate}')
            
        #종류
        product_category = category_list[index]
        print(category_list[index])
        
        #이미지 소스
        product_img = list.find('dt',{'class':'image'})
        product_img = product_img.select_one('img')['src']
        print(product_img)

        # 상품이름 , 이미지 소스 , 종류 , 출처 , 링크 , 할인 , 정상가 , 할인가 , 리뷰개수 , 평점
        product_data.append([product_name, product_img, product_category, link, product_base_price , product_discount_rate , product_final_price, product_reviews, product_rate])
        print('-------------------------------------------')