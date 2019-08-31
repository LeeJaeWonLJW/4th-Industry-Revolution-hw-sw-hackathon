<template>
  <div class="register">
    <div class="logo-bg">
      <h1>FooDiet</h1>
      <p>Food + Diet</p>
    </div>

    <div class="form">
      <fieldset class="register-input">
        <span class="label">이메일</span>
        <input>
      </fieldset>

      <fieldset class="register-input">
        <span class="label">암 호</span>
        <input type="password">
      </fieldset>

      <fieldset class="register-input">
        <span class="label">이 름</span>
        <input>
      </fieldset>
    </div>

    <div class="btn-group">
      <div @click="$router.push('/register/sex')"  class="btn">
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
  padding: 0;
  padding-top: 12px;

  border: 0;
  overflow: hidden;
  background-color: none;
}
.form input:-webkit-autofill,
.form input:-webkit-autofill:hover, 
.form input:-webkit-autofill:focus {
  background-color: none;
  transition: background-color 5000s ease-in-out 0s;
}
fieldset.register-input span {
  position: absolute;
  left: 2px;
  bottom: 5px;
  width: 52px;
  height: 21px;
  font-family: SourceHanSansK;
  font-size: 15px;
  font-weight: 600;
  font-style: normal;
  font-stretch: normal;
  letter-spacing: normal;
  text-align: left;
  color: #505050;
}
fieldset.register-input input {
  width: 100%;
  padding: 7px 0 7px 58px;
  
  color: #505050;
  font-size: 15px;

  border: 0;
  outline: 0;
  border-bottom: 1px solid #aeaeae;

  cursor: pointer;
  caret-color: #adadad;
}

.logo-bg {
  position: relative;
  display: inline-block;
  
  width: 100%;
  height: 251px;
  vertical-align: middle;
  font-size: 25px;
  color: #ffffff;

  margin-bottom: 30px;
  background-color: #91ffb3;
  border-radius: 0 0 50% 50%;
}

.logo-bg h1 {
  padding-top: 87px;
  margin: 0;
}

.logo-bg p {
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