<template>
  <div>
    <div class="header">
      <div class="info info-circle bg-blgn-gra-1 box-shadow">
        <span class="title">핫식스</span>
      </div>
    </div>
    
    <div class="contents">
      <div>
        <input class="fd-input" type="text" placeholder="1">
        <input class="fd-input volume" type="text" placeholder="355ml">
      </div>
      <div class="fd-btn fd-btn-lg">Diary에 담기</div>

      <p class="title">14Kcal</p>
      <div class="pigure">
        <div class="pull-left">당 적음</div>
        <div class="pull-right">비타민 많음 고카페인</div>
      </div>

      <p class="title">영양정보</p>
      <ul class="nut">
        <li class="bold">
          <span class="nut-name">탄수화물</span>
          <span class="nut-val">4g</span>
        </li>
        <li>
          <span class="nut-name">섬유질</span>
          <span class="nut-val">0g</span>
        </li>
        <li>
          <span class="nut-name">설탕</span>
          <span class="nut-val">29g</span>
        </li>
        <li class="bold">
          <span class="nut-name">단백질</span>
          <span class="nut-val">1g</span>
        </li>
        <li class="bold">
          <span class="nut-name">지방</span>
          <span class="nut-val">0.4g</span>
        </li>
        <li>
          <span class="nut-name">불포화지방</span>
          <span class="nut-val">0g</span>
        </li>
        <li>
          <span class="nut-name">포화지방</span>
          <span class="nut-val">0g</span>
        </li>
        <li class="bold">
          <span class="nut-name">기타</span>
          <span class="nut-val">0g</span>
        </li>
        <li>
          <span class="nut-name">칼륨</span>
          <span class="nut-val">0g</span>
        </li>
        <li>
          <span class="nut-name">콜레스트롤</span>
          <span class="nut-val">0g</span>
        </li>
        <li>
          <span class="nut-name">나트륨</span>
          <span class="nut-val">275mg</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<style scoped>
.fd-input {
  margin: auto 13px;
  width: 58px;
  height: 34px;
  border-radius: 8px;
  border: solid 1px #808080;
}
.fd-input.volume {
  padding-right: 8px;
  text-align: right;
  width: 142px;
}
.contents .title {
  font-family: SofiaPro;
  font-size: 16px;
  font-weight: bold;
  text-align: left;
  margin: 14px 0 6px 28px;
  color: #808080;
}

.pigure {
  margin: 8px auto;
  padding: 16px 8px;
  border-top: 1px solid #94b2ef;
  border-bottom: 1px solid #94b2ef;
}
.pigure:after {
  position: relative;
  display: block;
  height: 15px;
  left: 50%;
  border-left: 1px solid #94b2ef;
  content: '';
}
.pigure > div {
  position: relative;
  display: block;
  width: 50%;
}
.pigure > div:first-child {
  font-size: 12px;
  color: #94b2ef;
}
.pigure > div:last-child {
  font-size: 12px;
  color: #ff7676;
}

ul.nut {
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0;

  color: #808080;
}
ul.nut li {
  position: relative;
  display: inline-block;
  width: 80%;
  margin: 2px auto;
}
ul.nut li span.nut-name {
  width: 48px;
  float: left;
  text-align: right;
}
ul.nut li span.nut-val {
  min-width: 48px;
  float: right;
  text-align: left;
}
ul.nut li:after {
  position: absolute;

  width: 55%;
  height: 1px;
  margin: 7px auto;
  left: 0;
  right: 0;

  border-top: 1px dashed #808080;
  content: '';
}

ul.nut li.bold {
  color: #505050
}
ul.nut li.bold:after {
  border-top: 1px solid #909090;
}

ul.nut li.bold {
  padding-top: 4px;
  border-top: 2px solid #eff4fd;

}


</style>