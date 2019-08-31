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
            :style="{backgroundImage: 'url('+require('../assets/diet_card_2.png')+')'}">  
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
      <div class="btn fd-btn">제가 직접 고를게요!</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'dietList'
}
</script>

<style scoped>
.text-left {
  text-align: left;
}

body {
  font-family: SourceHanSansK;
}

.slider {
  display: flex;
  overflow-x: scroll;
  -webkit-overflow-scrolling: touch;
  scroll-snap-type: x mandatory;
  transition: 1s;
  scroll-behavior: smooth;
}
.slider::-webkit-scrollbar,
.slider::-webkit-scrollbar-thumb {
  display: none;
}

.slider > .item {
  flex-shrink: 0;
  margin-right: 30px;
}
.slider .item > h3,
.slider .item > p {
  margin-left: 4px;
}

.header {
  position: relative;
}
.header .menu-title {
  position: relative;
  height: 20px;
  padding: 10px 0;

  background-color: #ffffff;

  font-size: 14px;
  text-align: center;
  color: #505050;

  z-index: 99;
}
.header .info {
  position: relative;
  padding: 50px 16px 36px 16px;

  font-size: 12px;
  text-align: center;
  color: #ffffff;

  box-shadow: 0 0 14px 0 rgba(0, 0, 0, 0.16);
}
.header .info .title {
  font-size: 18px;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.16);
}

.contents {
  padding: 0 16px;
  margin-top: 44px;
  font-size: 10px;
  color: #505050;
}
.contents p {
  margin: 0;
}
.contents h3 {
  font-size: 16px;
  margin: 4px 0;
}

.item {
  width: 258px;
  
}
.diet-card {
  position: relative;
  margin: 8px 0;

  width: 100%;
  height: 160px;
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.16);

  background-size: cover;
  background-repeat: no-repeat;
}
.diet-card:after {
  width: auto;
  height: 100%;
  background-image: linear-gradient(to bottom, #a7ffa3, #91a2ff, #9e77e8, #8bffd3);
  background-size: 40%;
  right: 0;
}


.footer {
  position: absolute;
  width: 100%;
  bottom: 0;
  margin-bottom: 16px;
}


.info-circle {
  border-bottom-left-radius: 50% 54px;
  border-bottom-right-radius: 50% 54px;
}
.bg-green-gra-1 {
  background-image: linear-gradient(to top, #a7ffa3, #a1ffae, #8cffd1, #8bffd3);
}

.btn {
  width: 100%;
  height: 40px;
  border-radius: 20px;
}
.fd-btn {
  width: 100%;
  max-width: 280px;

  margin: 16px auto;

  font-size: 14px;
  line-height: 40px;
  text-align: center;
  vertical-align: middle;
  color: #ffffff;
  background-color: #91ffb3;
}
</style>
