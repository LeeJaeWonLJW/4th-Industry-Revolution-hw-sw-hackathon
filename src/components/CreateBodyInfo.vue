<template>
  <div>
    <div class="titlebar">
      <p>신체정보</p>
    </div>

    <div class="jumbotron">
      <h2>어떤 몸으로 변하고 싶으신가요?</h2>
      <div class="setting">
        <p>설정하기</p>
      </div>
    </div>

    <div class="input-container">
      <fieldset class="create-input">
        <input placeholder="나이가 어떻게 되시나요?" />
        <!-- <span class="label">kg</span> -->
      </fieldset>
      <fieldset style="padding-top: 10px;" class="create-input">
        <input placeholder="키가 어떻게 되시나요?" />
        <span class="label">Cm</span>
      </fieldset>
      <fieldset style="padding-top: 10px;" class="create-input">
        <input placeholder="몸무게가 어떻게 되시나요?" />
        <span class="label">Kg</span>
      </fieldset>
      <fieldset style="padding-top: 10px;" class="create-input">
        <input placeholder="목표 몸무게가 어떻게 되시나요?" />
        <span class="label">Kg</span>
      </fieldset>
    </div>

    <div class="btn">
      <p>다음</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "create-body-info"
};
</script>

<style scoped>
.titlebar {
  width: 100%;
  height: 40px;
  /* background-color: black; */
}

.titlebar p {
  margin: 0;
  padding-top: 18px;
  font-size: 16px;
  line-height: 1.43;
}

.jumbotron {
  width: 100%;
  height: 109px;
  background-image: linear-gradient(to bottom, #a7ffa3, #8bffd3);
}

.jumbotron h2 {
  color: white;
  font-size: 16px;
  font-weight: normal;
  padding-top: 25px;
  font-weight: bold;
  font-style: normal;
  /* font-family: source-han-sans-korean, sans-serif; */
}

.setting {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  border-radius: 22px;
  border: solid 1px #ffffff;
  width: 77px;
}

.setting p {
  color: white;
  margin: 0;
  font-weight: normal;
  font-size: 13px;
  padding-top: 3px;
  padding-bottom: 3px;
  padding-right: 10px;
  padding-left: 10px;
}

.input-container {
  padding-top: 10px;
  width: 98%;
  margin-left: auto;
  margin-right: auto;
}

fieldset.create-input {
  position: relative;
  border: 0;
  overflow: hidden;
}
fieldset.create-input span {
  position: absolute;
  bottom: 15px;
  width: 160px;
  height: 21px;
  /* font-family: SourceHanSansK; */
  font-size: 15px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  letter-spacing: normal;
  text-align: right;
  color: #60fd91;
}
fieldset.create-input input {
  width: 100%;
  padding: 7px 0 7px 0px;

  color: #6a6a6a;
  font-size: 15px;

  border: 0;
  outline: 0;
  border-bottom: 1px solid #60fd91;

  cursor: pointer;
  caret-color: #adadad;
}

fieldset.create-input input::placeholder {
  color: #d5d5d5;
}

.btn {
  bottom: 35px;
  background-color: #91ffb3;
  width: 280px;
  height: 40px;

  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  border-radius: 20px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.16);
}

.btn p {
  color: white;
  margin-top: 10px;
  margin-bottom: 9px;
  font-weight: 500;
}
</style>