기능            메서드            엔드포인트              설명
회원가입         post          /api/register           사용자 정보 DB 저장
로그인           post         /api/login              사용자 인증 및 세션관리
상품목록조회      get          /api/products           전체 상품 조회
상품등록         post         /api/products           관리자용 상품등록
장바구니 담기    post          /api/cart               사용자별 장바구니 추가
장바구니 조회    get           /api/cart?user_id=1     특정 사용자의 장바구니 조회
주문 요청       post          /api/order               장바구나 상품 주문 처리
주문 목록 조회  get            /api/order?user_id=1     사요자 주문 내역