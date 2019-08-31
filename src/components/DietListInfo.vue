<template>
  <div>
    <div class="modal">
      
    </div>

    <div class="header">
      <div class="info info-circle"
        :style="{backgroundImage: 'url('+require('../assets/diet_card_1.png')+')'}">
        <p>Meal Plan</p>
        <span class="title">Keto Maintain</span>

        <div class="fd-btn-sm box-shadow bg-white fd-color"
          @click="e => e.target.closest('.modal').classList.toggle('show')">식단 시작하기</div>
      </div>
    </div>

    <div class="contents">
      <div class="meal-explain-box">
        <h4>Keto식단을 통해 균형잡힌 체중 감량을 해보세요</h4>
        <h4>기름진 음식을 먹으며 맛과 영양 모두를 챙기세요!</h4>
        <h4>식사 계획 및 영양을 큐레이팅 해드립니다.</h4>
      </div>

      <div class="meal-explain-box">
        <div class="title">
          <p>Keto Manintain</p>
          <p>식단 서비스 소개</p>
        </div>

        <ul class="checklist">
          <li>3주 다이어트 식단</li>
          <li>하루에 4끼를 먹자</li>
          <li>간단한 음식재료와 요리법</li>
          <li>순 탄수화물로 먹자</li>
        </ul>
      </div>

      <div class="nutrtionist meal-explain-box box-shadow">
        <img src="../assets/profile.png">
        <h2>전문가</h2>
        <h3>NUTRTIONIST</h3>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'dietList'
}
</script>

<style scoped>
.contents {
  padding: 0;
}
.meal-explain-box {
  margin-bottom: 28px;
  padding: 16px 0;
}
.meal-explain-box:nth-child(2n) {
  background-color: #fafafa;
}
.meal-explain-box .title,
.meal-explain-box .title > p {
  font-size: 20px;
  font-weight: bold;
  color: #91a2ff;
}
.meal-explain-box ul.checklist {
  position: relative;
  list-style: none;
  margin: 0;
  margin-top: 22px;
  padding: 0;
}
.meal-explain-box ul.checklist li {
  font-size: 12px;
  margin: 8px 0;
}
.meal-explain-box ul.checklist li:before {
  position: relative;
  display: inline;
  left: -12px;
  content: '√';
  color: #91a2ff;
}
.nutrtionist {
  position: relative;
  padding: 31px;
  padding-top: 54px;
}
.nutrtionist img {
  position: absolute;
  width: 80px;
  height: 80px;
  left: 50%;
  margin-left: -40px;
  top: -40px;
  border: solid 3px #ffffff;
}
.nutrtionist h2 {
  font-family: SourceHanSansK;
  font-size: 23px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.48;
  letter-spacing: normal;
  text-align: center;
  color: #505050;
}
.nutrtionist h3 {
  font-family: SofiaPro;
  font-size: 12px;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.17;
  letter-spacing: normal;
  text-align: left;
  color: #505050;
}
.nutrtionist p {
  font-family: SourceHanSansK;
  font-size: 18px;
  font-weight: 500;
  font-style: normal;
  font-stretch: normal;
  line-height: 1.78;
  letter-spacing: normal;
  text-align: center;
  color: #91a2ff;
}

.info .title {
  height: 32px;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.16);
  font-family: SofiaPro;
  font-size: 32px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  line-height: 0.81;
  letter-spacing: normal;
  text-align: left;
  color: #ffffff;
}
.info p {
  height: 17px;
  font-family: SourceHanSansK;
  font-size: 12px;
  font-weight: normal;
  font-style: normal;
  font-stretch: normal;
  line-height: 2.33;
  letter-spacing: normal;
  text-align: center;
  color: #ffffff;
}

.info .fd-btn-sm {
  margin: 0 auto;
  margin-top: 24px;

  color: #91a2ff;
}
</style>
