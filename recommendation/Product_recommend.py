import pandas as pd
import numpy as np


'''
현재 페이지 상품의 카테고리 내에서
리뷰개수와 평점 상위 10가지
상품을 추천
'''

def category_recommend(category):

    products = pd.read_csv('product_data.csv', names = ['name' , '종류' ,'링크' , '할인' , '정상가' , '할인가' , '리뷰개수' , '평점'])

    products = products.set_index('name', inplace= True)

    ratings = products[products['종류']== category][['리뷰개수','평점']]

    ratings_recom = ratings.sort_values(['평점','리뷰개수'],ascending=False).index[:10]

    return [ratings_recom[i] for i in range(len(ratings_recom))]


