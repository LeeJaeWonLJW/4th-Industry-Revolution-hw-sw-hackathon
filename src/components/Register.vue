<template>
  <div class="register">
    <div class="logo">
      <h1>FooDiet</h1>
      <p>Food + Diet</p>
    </div>

    <div class="form">
      <fieldset class="register-input">
        <span class="label">이메일:</span>
        <input>
      </fieldset>

      <fieldset class="register-input">
        <span class="label">암호:</span>
        <input type="password">
      </fieldset>

      <fieldset class="register-input">
        <span class="label">이름:</span>
        <input>
      </fieldset>
    </div>

    <div class="btn-group">
      <div class="btn">
        <p>회원가입</p>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "register"
};
</script>

<style scoped>
.register {
  background-color: #fff;
  height: 100%;
}

.form {
  padding: 0 16px;
}
fieldset.register-input {
  position: relative;
  border: 0;
  overflow: hidden;
}
fieldset.register-input span {
  position: absolute;
  bottom: 15px;
  width: 52px;
  height: 21px;
  font-family: SourceHanSansK;
  font-size: 15px;
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  letter-spacing: normal;
  text-align: left;
  color: #60fd91;
}
fieldset.register-input input {
  width: 100%;
  padding: 7px 0 7px 58px;
  
  color: #6a6a6a;
  font-size: 15px;

  border: 0;
  outline: 0;
  border-bottom: 1px solid #60fd91;

  cursor: pointer;
  caret-color: #adadad;
}

.logo {
  padding-top: 87px;
  font-size: 25px;
  color: #91ffb3;
  margin-bottom: 60px;
}

.logo h1 {
  margin: 0;
}

.logo p {
  margin: 0;
  font-size: 14px;
}

.btn-group {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  bottom: 35px;
}
.btn-group .btn {
  margin: 0 auto;
  margin-top: 20px;

  width: 280px;
  height: 20px;
  border-radius: 20px;
  border: solid 1px #91ffb3;
  background-color: #91ffb3;
  padding: 10px;
}
.btn-group .btn p {
  height: 20px;
  margin: 0;
  text-align: center;

  font-family: SourceHanSansKR;
  font-size: 15px;
  font-weight: bold;
  letter-spacing: normal;
  color: #ffffff;
}
</style>