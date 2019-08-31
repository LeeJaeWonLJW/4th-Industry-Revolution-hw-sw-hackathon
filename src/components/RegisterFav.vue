<template>
  <div class="register_fav">
    <div class="menu-text">
      <p>신체정보입력</p>
    </div>
    <div class="title">
      <h2>좋아하는 음식 10가지를 선택해 주세요</h2>
      <p>{{this.count}}/10</p>
    </div>

    <div class="fav-select-box">
      <div class="row">
        <FoodSelectItem
          :label="1"
          @send-count="addCount"
          :image="require('../assets/food_receipts/1_그래놀라바.png')"
          food="그래놀라바"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="2"
          @send-count="addCount"
          :image="require('../assets/food_receipts/2_강된장비빔밥.jpg')"
          food="강된장 비빔밥"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="3"
          @send-count="addCount"
          :image="require('../assets/food_receipts/3_해물솥밥.jpg')"
          food="해물솥밥"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="4"
          @send-count="addCount"
          :image="require('../assets/food_receipts/4_닭가슴살샐러드.jpg')"
          food="닭가슴살 샐러드"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="5"
          @send-count="addCount"
          :image="require('../assets/food_receipts/5_분짜.jpg')"
          food="분짜"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="6"
          @send-count="addCount"
          :image="require('../assets/food_receipts/6_봉골레파스타.jpg')"
          food="봉골레 파스타"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="7"
          @send-count="addCount"
          :image="require('../assets/food_receipts/7_열무국수.jpg')"
          food="열무국수"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="8"
          @send-count="addCount"
          :image="require('../assets/food_receipts/8_명란두부찌개.jpg')"
          food="명란두부찌개"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="9"
          @send-count="addCount"
          :image="require('../assets/food_receipts/9_삼겹살김치말이찜.jpg')"
          food="삼겹살 김치말이찜"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="10"
          @send-count="addCount"
          :image="require('../assets/food_receipts/10_차슈덮밥.jpg')"
          food="차슈덮밥"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="11"
          @send-count="addCount"
          :image="require('../assets/food_receipts/11_콩나물불고기.jpg')"
          food="콩나물 불고기"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="12"
          @send-count="addCount"
          :image="require('../assets/food_receipts/12_닭고기양배추롤.jpg')"
          food="닭고기양배추롤"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="13"
          @send-count="addCount"
          :image="require('../assets/food_receipts/13_돼지고기오징어쌈밥.jpg')"
          food="돼지고기오징어쌈밥"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="14"
          @send-count="addCount"
          :image="require('../assets/food_receipts/14_콩샐러드.jpg')"
          food="콩샐러드"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="15"
          @send-count="addCount"
          :image="require('../assets/food_receipts/15_부추전.jpg')"
          food="부추전"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="16"
          @send-count="addCount"
          :image="require('../assets/food_receipts/16_전복황태삼계탕.jpg')"
          food="전복황태삼계탕"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="17"
          @send-count="addCount"
          :image="require('../assets/food_receipts/17_로스트치킨.jpg')"
          food="로스트치킨"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="18"
          @send-count="addCount"
          :image="require('../assets/food_receipts/18_가지말이구이.jpg')"
          food="가지말이구이"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="19"
          @send-count="addCount"
          :image="require('../assets/food_receipts/19_더덕구이.jpg')"
          food="더덕구이"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="20"
          @send-count="addCount"
          :image="require('../assets/food_receipts/20_떡꼬치구이.jpg')"
          food="떡꼬치구이"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="21"
          @send-count="addCount"
          :image="require('../assets/food_receipts/21_무화과베이컨말이구이.jpg')"
          food="무화과베이컨말이구이"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="22"
          @send-count="addCount"
          :image="require('../assets/food_receipts/22_감자샐러드.jpg')"
          food="감자샐러드"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="23"
          @send-count="addCount"
          :image="require('../assets/food_receipts/23_쇠고기카레.jpg')"
          food="쇠고기카레"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="24"
          @send-count="addCount"
          :image="require('../assets/food_receipts/24_찹스테이크.jpg')"
          food="찹스테이크"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="25"
          @send-count="addCount"
          :image="require('../assets/food_receipts/25_두부스테이크.jpg')"
          food="두부스테이크"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="26"
          @send-count="addCount"
          :image="require('../assets/food_receipts/26_두부과자.jpg')"
          food="두부과자"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="27"
          @send-count="addCount"
          :image="require('../assets/food_receipts/27_애호박찌개.jpg')"
          food="애호박찌개"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="28"
          @send-count="addCount"
          :image="require('../assets/food_receipts/28_봄동된장국.jpg')"
          food="봄동된장국"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="29"
          @send-count="addCount"
          :image="require('../assets/food_receipts/29_백합탕.jpg')"
          food="백합탕"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="30"
          @send-count="addCount"
          :image="require('../assets/food_receipts/30_두부버섯전골.jpg')"
          food="두부버섯전골"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="31"
          @send-count="addCount"
          :image="require('../assets/food_receipts/31_무굴밥.jpg')"
          food="무굴밥"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="32"
          @send-count="addCount"
          :image="require('../assets/food_receipts/32_콩나물밥.jpg')"
          food="콩나물밥"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="33"
          @send-count="addCount"
          :image="require('../assets/food_receipts/33_단호박영양밥찜.jpg')"
          food="단호박영양밥찜"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="34"
          @send-count="addCount"
          :image="require('../assets/food_receipts/34_단호박샐러드.jpg')"
          food="단호박샐러드"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="35"
          @send-count="addCount"
          :image="require('../assets/food_receipts/35_매운순대볶음.jpg')"
          food="로스트치킨"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="36"
          :image="require('../assets/food_receipts/36_돼지고기김치찌개.jpg')"
          food="돼지고기김치찌개"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="37"
          @send-count="addCount"
          :image="require('../assets/food_receipts/37_굴떡국.jpg')"
          food="굴떡국"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="38"
          @send-count="addCount"
          :image="require('../assets/food_receipts/38_감자고추장찌개.jpg')"
          food="감자고추장찌개"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="39"
          @send-count="addCount"
          :image="require('../assets/food_receipts/39_삼치간장조림.jpg')"
          food="삼치간장조림"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="40"
          @send-count="addCount"
          :image="require('../assets/food_receipts/40_삼겹살간장조림.jpg')"
          food="삼겹살간장조림"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="41"
          @send-count="addCount"
          :image="require('../assets/food_receipts/41_해물파전.jpg')"
          food="해물파전"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="42"
          @send-count="addCount"
          :image="require('../assets/food_receipts/42_쭈꾸미볶음.jpg')"
          food="쭈꾸미볶음"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="43"
          @send-count="addCount"
          :image="require('../assets/food_receipts/43_바지락칼국수.jpg')"
          food="바지락칼국수"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="44"
          @send-count="addCount"
          :image="require('../assets/food_receipts/44_토마토홍합찜.jpg')"
          food="토마토홍합"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="45"
          @send-count="addCount"
          :image="require('../assets/food_receipts/45_쇠고기미역국.jpg')"
          food="쇠고기미역국"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="46"
          @send-count="addCount"
          :image="require('../assets/food_receipts/46_묵은지닭볶음탕.jpg')"
          food="묵은지닭볶음탕"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="47"
          @send-count="addCount"
          :image="require('../assets/food_receipts/47_갈낙탕.jpg')"
          food="갈낙탕"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="48"
          @send-count="addCount"
          :image="require('../assets/food_receipts/48_해신탕.jpg')"
          food="해신탕"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="49"
          @send-count="addCount"
          :image="require('../assets/food_receipts/49_뚝배기불고기.jpg')"
          food="뚝배기불고기"
        ></FoodSelectItem>
        <FoodSelectItem
          :label="50"
          @send-count="addCount"
          :image="require('../assets/food_receipts/50_차돌박이된장찌개.jpg')"
          food="차돌밖이된장찌개"
        ></FoodSelectItem>
      </div>
    </div>
  </div>
</template>


<script>
import FoodSelectItem from "@/components/FoodSelectItem";
import { APIService } from "../api/APIService";
const apiService = new APIService();

export default {
  name: "register_favorite",
  data: () => ({
    count: 0
  }),
  components: {
    FoodSelectItem
  },
  methods: {
    addCount: function() {
      this.count++;
    }
  },
  async mounted() {
    let foodData = await window.localStorage.getItem("foodData");
    if (foodData !== null) {
      foodData = await JSON.parse(foodData);
      this.count = await Object.keys(foodData).length;
    }
  },
  watch: {
    count: async function(val) {
      if (val === 10) {
        try {
          let data = await JSON.parse(window.localStorage.getItem("data"));
          let gender = await window.localStorage.getItem("gender");
          let info = await JSON.parse(window.localStorage.getItem("info"));
          let foodData = await JSON.parse(
            window.localStorage.getItem("foodData")
          );

          let token = await apiService.register(
            data.phone,
            data.password,
            data.name,
            gender,
            info.age,
            info.height,
            info.weight,
            info.purpose,
            info.duration,
            data.profile_ing
          );

          if (token.success === true) {
            await window.localStorage.setItem("accessToken", token.accessToken);
            let end = await apiService.setFlavor(foodData, token.accessToken);

            if (end.success === true) {
              this.$router.push('/tab/index');
            }
          }
        } catch (e) {
          window.alert(e);
        }
      }
    }
  }
};
</script>

<style scoped>
.menu-text {
  width: 100%;
  height: 53.28px;
}

.menu-text p {
  margin: 0;
  padding-top: 18px;
  font-size: 16px;
  color: #505050;
  line-height: 1.43;
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