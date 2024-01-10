m = {
    'movie':{
        'ml' : ['1.액션', '2.공포', '3.로맨스'],
        'mp' : [10000,8000,9000]
    },
    'popcorn':{
        'pl': ['1.카라멜', '2.치즈', '3.소금'],
        'pp': [5000,4000,4000]
    }
}
movie_choice = int(input(f"영화를 고르세요[{m['movie']['ml']}]:")) - 1
popcorn_choice = int(input(f"팝콘을 고르세요[{m['popcorn']['pl']}]:")) - 1

print(f"선택한영화:{m['movie']['ml'][movie_choice]} / 선택한 팝콘:{m['popcorn']['pl'][popcorn_choice]} / 전체 가격:{m['movie']['mp'][movie_choice] + m['popcorn']['pp'][popcorn_choice]}")
