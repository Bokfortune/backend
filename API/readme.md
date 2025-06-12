| 기능           | 메서드 | 엔드포인트             | 설명                        |
| -------------- | ------ | ---------------------- | --------------------------- |
| 회원가입폼     | GET    | `/api/register`        | 회원가입 페이지 제공        |
| 회원가입       | POST   | `/api/register`        | 사용자 정보 DB 저장         |
| 로그인         | POST   | `/api/login`           | 사용자 인증 및 세션 관리    |
| 상품목록조회   | GET    | `/api/products`        | 전체 상품 조회              |
| 상품등록       | POST   | `/api/products`        | 관리자용 상품 등록          |
| 장바구니 담기  | POST   | `/api/cart`            | 사용자별 장바구니 추가      |
| 장바구니 조회  | GET    | `/api/cart?user_id=1`  | 특정 사용자의 장바구니 조회 |
| 주문 요청      | POST   | `/api/order`           | 장바구니 상품 주문 처리     |
| 주문 목록 조회 | GET    | `/api/order?user_id=1` | 사용자 주문 내역 조회       |


# FAST API 설치
```
pip install fastapi uvicorn sqlalchemy
```

# 통신 규칙
```
통신은 json 포맷으로 한다.
인증방식은 쿠키,세션 대신 단순 로그인 응답으로 user_id 유지(js변수에 저장)
응답메시지 {success:true, data: ..} 형식
에러처리   {success:true, error: '메시지'} 통일