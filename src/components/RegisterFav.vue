<template>
  <div class="register_fav">
    <div class="title">
      <h2>좋아하는 음식 10가지를 선택해 주세요</h2>
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
.title {
  position: relative;
  margin-top: 40px;
  margin-bottom: 20px;
  width: 100%;
  height: 79px;
  line-height: 79px;
  vertical-align: middle;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.16);
  background-color: #91ffb3;
}
.title h2 {
  position: relative;
  margin: 0 auto;
  text-align: center;
  font-size: 18px;
  font-weight: bold;
  color: #ffffff;
}

.fav-select-box {
  padding: 0 8px;
}
</style>