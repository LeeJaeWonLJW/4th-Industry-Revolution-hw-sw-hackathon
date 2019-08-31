<template>
  <div class="register">
    <!-- <div class="logo-bg active">
      <h1>FooDiet</h1>
      <p>Food + Diet</p>
    </div> -->

    <div class="footer-group">
      <div class="form">
        <fieldset class="register-input">
          <input type="text" placeholder="전화번호">
        </fieldset>

        <fieldset class="register-input">
          <input type="password" placeholder="암호">
        </fieldset>

        <fieldset class="register-input">
          <input type="text" placeholder="이름">
        </fieldset>
      </div>

      <div @click="$router.push('/register/sex')"  class="btn">
        <p>다음</p>
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
/* fieldset.register-input span {
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
} */
fieldset.register-input input {
  width: 70%;

  padding: 6px 2px;
  margin-bottom: 14px;
  text-align: center;
  
  color: #505050;
  font-size: 15px;

  border: 0;
  outline: 0;
  border-bottom: 1px solid #91ffb3;

  cursor: pointer;
  caret-color: #adadad;
}

.logo-bg {
  position: relative;
  display: inline-block;
  
  width: 100%;
  
  background-image: url('../assets/Peanut-butter-tarts.jpg');
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  min-height: 342px;

  transition: .75s ease-out;

  vertical-align: middle;
  font-size: 25px;
  color: #ffffff;

  margin-bottom: 30px;
  background-color: #91ffb3;
  border-bottom-left-radius: 50% 86px;
  border-bottom-right-radius: 50% 86px;
}

.logo-bg h1 {
  padding-top: 87px;
  margin: 0;
}

.logo-bg p {
  margin: 0;
  font-size: 14px;
}

.footer-group {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  bottom: 35px;
}
.footer-group .btn {
  margin: 0 auto;
  margin-top: 20px;

  width: 280px;
  height: 20px;
  border-radius: 20px;
  border: solid 1px #78e5b1;
  background-color: #78e5b1;
  padding: 10px;
}
.footer-group .btn p {
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