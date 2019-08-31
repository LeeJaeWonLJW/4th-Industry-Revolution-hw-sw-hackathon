<template>
  <div class="register_fav">
    <div class="menu-text">
    </div>
    <div class="title">
      <h2>좋아하는 음식 10가지를 선택해 주세요</h2>
      <p>0/10</p>
    </div>

    <div class="fav-select-box">
      <div class="row">
        <FoodSelectItem :image="require('../assets/food_receipts/1_그래놀라바.png')"
          food='그래놀라바'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/2_강된장비빔밥.jpg')"
          food='강된장 비빔밥'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/3_해물솥밥.jpg')"
          food='해물솥밥'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/4_닭가슴살샐러드.jpg')"
          food='닭가슴살 샐러드'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/5_분짜.jpg')"
          food='분짜'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/6_봉골레파스타.jpg')"
          food='봉골레 파스타'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/7_열무국수.jpg')"
          food='열무국수'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/8_명란두부찌개.jpg')"
          food='명란두부찌개'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/9_삼겹살김치말이찜.jpg')"
          food='삼겹살 김치말이찜'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/10_차슈덮밥.jpg')"
          food='차슈덮밥'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/11_콩나물불고기.jpg')"
          food='콩나물 불고기'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/12_닭고기양배추롤.jpg')"
          food='닭고기양배추롤'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/13_돼지고기오징어쌈밥.jpg')"
          food='돼지고기오징어쌈밥'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/14_콩샐러드.jpg')"
          food='콩샐러드'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/15_부추전.jpg')"
          food='부추전'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/16_전복황태삼계탕.jpg')"
          food='전복황태삼계탕'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/17_로스트치킨.jpg')"
          food='로스트치킨'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/18_가지말이구이.jpg')"
          food='가지말이구이'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/19_더덕구이.jpg')"
          food='더덕구이'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/20_떡꼬치구이.jpg')"
          food='떡꼬치구이'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/21_무화과베이컨말이구이.jpg')"
          food='무화과베이컨말이구이'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/22_감자샐러드.jpg')"
          food='감자샐러드'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/23_쇠고기카레.jpg')"
          food='쇠고기카레'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/24_찹스테이크.jpg')"
          food='찹스테이크'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/25_두부스테이크.jpg')"
          food='두부스테이크'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/26_두부과자.jpg')"
          food='두부과자'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/27_애호박찌개.jpg')"
          food='애호박찌개'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/28_봄동된장국.jpg')"
          food='봄동된장국'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/29_백합탕.jpg')"
          food='백합탕'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/30_두부버섯전골.jpg')"
          food='두부버섯전골'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/31_무굴밥.jpg')"
          food='무굴밥'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/32_콩나물밥.jpg')"
          food='콩나물밥'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/33_단호박영양밥찜.jpg')"
          food='단호박영양밥찜'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/34_단호박샐러드.jpg')"
          food='단호박샐러드'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/35_매운순대볶음.jpg')"
          food='로스트치킨'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/36_돼지고기김치찌개.jpg')"
          food='돼지고기김치찌개'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/37_굴떡국.jpg')"
          food='굴떡국'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/38_감자고추장찌개.jpg')"
          food='감자고추장찌개'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/39_삼치간장조림.jpg')"
          food='삼치간장조림'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/40_삼겹살간장조림.jpg')"
          food='삼겹살간장조림'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/41_해물파전.jpg')"
          food='해물파전'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/42_쭈꾸미볶음.jpg')"
          food='쭈꾸미볶음'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/43_바지락칼국수.jpg')"
          food='바지락칼국수'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/44_토마토홍합찜.jpg')"
          food='토마토홍합'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/45_쇠고기미역국.jpg')"
          food='쇠고기미역국'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/46_묵은지닭볶음탕.jpg')"
          food='묵은지닭볶음탕'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/47_갈낙탕.jpg')"
          food='갈낙탕'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/48_해신탕.jpg')"
          food='해신탕'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/49_뚝배기불고기.jpg')"
          food='뚝배기불고기'></FoodSelectItem>
        <FoodSelectItem :image="require('../assets/food_receipts/50_차돌박이된장찌개.jpg')"
          food='차돌밖이된장찌개'></FoodSelectItem>
        
      </div>
    </div>

  </div>
</template>


<script>
import FoodSelectItem from '@/components/FoodSElectItem'
export default {
  name: "register_favorite",
  components: {
    FoodSelectItem
  }
};
</script>

<style scoped>
.menu-text {
  width: 100%;
  height: 40px;
  background-color: #ffffff;

  font-family: SourceHanSansK;
  font-size: 14px;
  color: #505050;
}
.title {
  position: relative;
  margin-bottom: 20px;
  width: 100%;
  height: auto;
  padding: 26px 0;
  vertical-align: middle;

  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.16);
  background-image: linear-gradient(to bottom, #a7ffa3, #8bffd3);
}
.title h2 {
  position: relative;
  margin: 0 auto;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  color: #ffffff;
}
.title p {
  margin: 0;
  margin-top: 8px;
  font-family: SourceHanSansK;
  font-size: 14px;
  font-weight: 500;
  color: #ffffff;
}

.fav-select-box {
  padding: 0 8px;
}
</style>