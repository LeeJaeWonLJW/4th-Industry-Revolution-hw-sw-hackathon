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

      <p class="kcal">14Kcal</p>
      <div class="pigure">
        <div class="pull-left">당 적음</div>
        <div class="pull-right">비타민 많음 고카페인</div>
      </div>

      
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
.kcal {
  font-family: SofiaPro;
  font-size: 14px;
  font-weight: 500;
  font-style: normal;
  font-stretch: normal;
  line-height: 2;
  letter-spacing: normal;
  text-align: left;
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
</style>