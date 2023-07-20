// JSON 객체 vs JSON 배열
// JSON 을 많이 쓰는 이유 ===> 데이터 전달, 교환, 저장시 가볍고, 텍스트기반, JS기반

// [1] JOSN 객체 ===> 중괄호
// JSON에서 객체란 ===> Key와 Value 한 쌍으로 이루어진 정렬되지 않은 property들의 집합
// 콤마로 구분하여 여러개의 속성을 가질 수 있다.
// 문자열은 반드시 큰 따옴표 사용
{
    "namke": "홍길동",
    "age" : 15,
    "nationally" : "Korea"
    "hobby" : "영화감상"
}

// 객체안에 객체
{
    group1 : {
        "namke": "홍길동",
        "age" : 15,
        "nationality" : "Korea"
        "hobby" : "영화감상",
        "company": {
            "cname": "핵발전소"
            "cphone": "02-333-3333"
            "caddress": "경기도 용인시 "
        }
    }
}

// JSON 배열 : 대괄호 사용
// 콤마를 사용하여 여러 json 객체를 추가 및 구분할 수 있다.
// 배열이 이름이 person이고 3개의 json 객체를 이 배열의 요소로 가지는 json 배열을 만들어 보세요.

"person": [
    {"name": "홍길동", "age": 20, "nationality": "한국"},
    {"name": "성춘향", "age": 25, "nationality": "한국"},
    {"name": "변사또", "age": 30, "nationality": "러시아"}
]