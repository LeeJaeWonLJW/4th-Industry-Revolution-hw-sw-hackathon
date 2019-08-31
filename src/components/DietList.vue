<template>
  <div>
    <div class="header">
      <div class="menu-title">
        식단 선택
      </div>

      <div class="info info-circle bg-green-gra-1">
        <span class="title">어떤 식단을 먹어야 하는지 고민이신가요?</span>
        <p>나에게 맞는 식단을 이용해보세요!</p>
      </div>
    </div>

    <div class="contents">
      <div class="slider slider-hori">
        <div class="item">
          <h3 class="text-left">Keto and fating diets</h3>
          <p class="text-left">나에게 필요한 영양소와 입맛까지 고려한 식단</p>

          <div class="diet-card"
            :style="{backgroundImage: 'url('+require('../assets/diet_card_1.png')+')'}"
            @click="$router.push('/tab/dietlist/1')">
          </div>
        </div>

        <div class="item">
          <h3 class="text-left">Keto and fating diets</h3>
          <p class="text-left">나에게 필요한 영양소와 입맛까지 고려한 식단</p>

          <div class="diet-card"
            :style="{backgroundImage: 'url('+require('../assets/diet_card_2.png')+')'}">  
          </div>
        </div>
      </div>
    </div>

    <div class="footer">
      <div class="fd-btn fd-btn-lg">제가 직접 고를게요!</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'dietList'
}
</script>

<style scoped>
.slider .item {
  width: 285px;
  margin-right: 30px;
}
.text-left {
  text-align: left;
}
</style>
