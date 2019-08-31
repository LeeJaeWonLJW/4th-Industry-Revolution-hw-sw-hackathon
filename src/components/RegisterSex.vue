<template>
  <div class="register_sex">
    <div class="middle-box">
      <p class="title">안녕하세요!</p>
      <p class="sub-text">자세한 진단을 위해 몇가지만 답해주세요</p>

      <div class="btn-group">
        <button class="btn pull-left">남성</button>
        <button class="btn pull-right">여성</button>
      </div>
    </div>

  </div>
</template>


<script>
export default {
  name: "register_sex"
};
</script>

<style scoped>
.pull-left { float: left; }
.pull-right { float: right; }

.middle-box {
  position: absolute;
  align-items: center;

  top: 50%;
  left: 50%;
  margin: -64px 0 0 -160px;
}

.title {
  margin: 0;
  font-size: 24px;
  font-weight: bold;
  line-height: 28px;
  color: #505050;
}
.sub-text {
  margin: 0;
  margin-top: 8px;
  font-size: 14px;
  font-weight: 300;
  line-height: 18px;
  color: #505050;
}

.btn-group {
  position: relative;
  display: inline-block;
  width: 100%;
  margin-top: 29px;
}
.btn-group .btn {
  width: 140px;
  height: 40px;
  margin: 0 10px;
  border: 0;
  border-radius: 17px;
  box-shadow: 0 3px 6px 0 rgba(0, 0, 0, 0.16);
  background-color: #91ffb3;

  font-family: SourceHanSansK;
  font-size: 16px;
  font-weight: bold;
  color: #ffffff;

  outline: none;
}
</style>