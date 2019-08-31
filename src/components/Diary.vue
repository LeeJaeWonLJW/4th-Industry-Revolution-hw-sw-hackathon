<template>
  <div>
    <div class="top">
      <p class="date">2019.08.31 토요일</p>

      <div class="daily-purpose-progress">
        <div class="today-kcal">
          <p class="h3">1991</p>
          <p class="h4">오늘 먹은 칼로리</p>
        </div>
        
        <div class="now-kcal">
          <p class="h3">1991</p>
          <p class="h4">남은 칼로리</p>
        </div>

        <div class="now-percent">
          <p class="h3">35%</p>
          <p class="h4">현재 수행률</p>
        </div>
      </div>

      <div class="nutrient">
        <div class="item dan">
          <p class="gram">98g남음</p>
          <p class="explain">단백질</p>
        </div>

        <div class="item tan">
          <p class="gram">232g남음</p>
          <p class="explain">탄수화물</p>
        </div>

        <div class="item ji">
          <p class="gram">66g남음</p>
          <p class="explain">지방</p>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="diary-kg">
        <div class="pull-left">
          <p class="kg">79.8KG</p>
          <p>현재 체중</p>
        </div>
        <div class="pull-right">
          <p class="kg">75KG</p>
          <p>목표 체중</p>
        </div>
      </div>

      <div class="diary-update">
        <div class="btn-kg-update">
          오늘 몸무게 업데이트하기
        </div>

        <div class="meal-update">
          <div class="item">
            <img src="../assets/breakfast_1.png">
            <div class="info">
              <p>아침 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus"></a>
          </div>

          <div class="item">
            <img src="../assets/breakfast.png">
            <div class="info">
              <p>점심 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus"></a>
          </div>

          <div class="item">
            <img src="../assets/bell-covering-hot-dish.png">
            <div class="info">
              <p>저녁 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus"></a>
          </div>

          <div class="item">
            <img src="../assets/chocolate.png">
            <div class="info">
              <p>간식 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus"></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'diary'
}
</script>

<style scoped>
.pull-left { float: left; }
.pull-right { float: right; }

.top {
  position: relative;
  display: inline-block;

  width: 100%;
  height: 276px;
  padding-top: 12px;
  box-shadow: 0 0 14px 0 rgba(0, 0, 0, 0.16);
  background-image: linear-gradient(to bottom, #91a2ff, #91ffc9);
  border-bottom-left-radius: 50% 86px;
  border-bottom-right-radius: 50% 86px;

  font-family: SofiaPro;
  text-align: center;
  color: #ffffff;
}

.top .h3 {
  font-size: 20px;
  margin: 0;
}
.top .h4 {
  font-size: 10px;
  margin: 0;
}

.top .date {
  font-family: SofiaPro;
  font-size: 14px;
}

.top .daily-purpose-progress {
  position: relative;
  height: 93px;
  padding: 0 32px 0 22px;
}
.top .daily-purpose-progress > div {
  position: relative;
  display: inline-block;
  text-align: center;
}

.top .daily-purpose-progress .now-kcal {
  position: absolute;
  width: 93px;
  height: 100%;
  border: 1px solid #ffffff;
  border-radius: 50%;

  margin-right: auto;
  margin-left: auto;
  left: 0;
  right: 0;
}
.now-kcal p.h3 {
  margin-top: 18px;
}
.now-kcal p.h4 {
  margin-top: 2px;
}

.top .today-kcal {
  position: absolute;
  float: left;
  height: 100%;
  margin-top: 18px;
}

.top .now-percent {
  position: absolute;
  float: right;
  height: 100%;
  margin-top: 18px;
}


.top .nutrient {
  position: relative;
  min-height: 48px;
  padding: 20px 56px;

  font-size: 10px;
}
.nutrient .item {
  position: relative;
  display: inline-block;
}

.nutrient .item p {
  margin: 0;
}
.nutrient .item p.explain {
  margin-top: 4px;
  padding-top: 4px;
  border-top: 1px solid #ffffff;
}

.nutrient .item.dan {
  float: left;
}
.nutrient .item.ji {
  float: right;
}
.nutrient .item.tan {
  margin-right: auto;
  margin-left: auto;
  left: 0;
  right: 0;
}


.diary-kg {
  position: relative;
  padding: 25px 24px;
  color: #91b1f6;
  font-size: 12px;
}
.diary-kg > div {
  position: relative;
  display: inline-block;
}
.diary-kg p {
  margin: 0;
}
.diary-kg .kg {
  font-size: 18px;
}


.diary-update {
  padding: 25px 30px;
  margin-top: 10px;
}
.diary-update .btn-kg-update {
  min-width: 262px;
  height: 46px;
  line-height: 46px;
  border-radius: 23px;
  background-color: #91b5f3;

  vertical-align: middle;
  font-size: 12px;
  color: #ffffff;
}

.diary-update .meal-update {
  color: #808080;
  font-size: 12px;
}
.meal-update p {
  margin: 0;
}
.meal-update .item {
  position: relative;
  display: inline-block;
  width: 100%;
  height: 36px;
  margin-top: 24px;
  text-align: left;
}
.meal-update .item img {
  width: 40px;
  max-height: 36px;
}
.meal-update .item .info {
  display: inline-block;
  height: 100%;
  margin-left: 20px;
}
.meal-update .item .info p:first-child {
  font-size: 14px;
  font-weight: bold;
}
.meal-update .btn-plus {
  float: right;
  margin-top: 6px;
  width: 24px;
  height: 24px;
  background-color: #91b1f6;
  border-radius: 50%;
}

.view-type {
  margin: 25px 0 10px 0;
}

ul.view-purpose-type {
  color: #d5d5d5;
  list-style: none;
  padding: 0;
  margin: 0;

  font-size: 12px;
  font-family: SourceHanSansK;
}
ul.view-purpose-type li {
  float: left;
  margin-right: 8px;
  padding-right: 8px;
  border-right: 1px solid #d5d5d5;
  cursor: pointer;
}
ul.view-purpose-type li:last-child {
  margin-right: 0px;
  padding-right: 0px;
  border: 0;
}
ul.view-purpose-type li.active {
  color: #505050;
}

select.view-data-type {
  background: none;
  border: none;
  
  height: 17px;
  font-family: SourceHanSansK;
  font-size: 12px;
  color: #91a2ff;
}

.triangle_under {
  position: absolute;
  width: 0px;
  height: 0px;
  top: 60%;
  border-top: 6px solid #9d9d9d;
  border-bottom: 6px solid none;
  border-right: 5px solid transparent;
  border-left: 5px solid  transparent;
}

@-webkit-keyframes rotating /* Safari and Chrome */ {
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes rotating {
  from {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
.rotating {
  -webkit-animation: rotating 2s linear infinite;
  -moz-animation: rotating 2s linear infinite;
  -ms-animation: rotating 2s linear infinite;
  -o-animation: rotating 2s linear infinite;
  animation: rotating 2s linear infinite;
}
</style>
