<template>
  <div :class="{'active': visible}" class="login">
    <div class="logo">
      <h1>FooDiet</h1>
      <p>Food + Diet</p>
    </div>
    <div v-if="!visible" class="welcome">
      <p>환영합니다</p>
    </div>
    <div v-if="!visible" class="btn-group">
      <div @click="visible = true" class="btn">
        <p>회원가입</p>
      </div>
      <div class="btn">
        <p>로그인</p>
      </div>
    </div>
    <!-- <Register v-if="visible"></Register> -->
    <div v-if="visible" class="register">
      <div class="footer-group">
        <div class="profile">
          <div class="profile-pic">
            <img src="../assets/icon/camera.png" />
          </div>
          <span>프로필</span>
        </div>

        <div class="form">
          <fieldset class="register-input">
            <input v-model="phone" type="text" placeholder="전화번호" />
          </fieldset>

          <fieldset class="register-input">
            <input v-model="password" type="password" placeholder="암호" />
          </fieldset>

          <fieldset class="register-input">
            <input v-model="username" type="text" placeholder="이름" />
          </fieldset>
        </div>

        <div @click="submit()" class="btn">
          <p>다음</p>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import { async } from "q";
// import Register from '@/components/Register'
export default {
  name: "login",
  data: () => ({
    visible: false,
    phone: "",
    password: "",
    username: ""
  }),
  components: {
    // Register
  },
  methods: {
    submit: async function() {
      let json = {
        phone: this.phone,
        password: this.password,
        username: this.username
      };
      try {
        await window.localStorage.setItem("data", json);
        await this.$router.push("/register/sex");
      } catch (e) {
        window.alert(e);
      }
    }
  }
};
</script>

<style scoped>
.login {
  background-image: url("../assets/Peanut-butter-tarts.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  min-height: 100vh;

  transition: 0.75s ease-out;
  /* -webkit-transition:width 2s, height 2s, background-color 2s, -webkit-transform 2s;
  transition:width 2s, height 2s, background-color 2s, transform 2s; */
}

.login.active {
  min-height: 350px;
  border-bottom-left-radius: 50% 104px;
  border-bottom-right-radius: 50% 104px;
}

.logo {
  padding-top: 87px;
  font-size: 25px;
  color: white;
}

.logo h1 {
  margin: 0;
}

.logo p {
  margin: 0;
  font-size: 14px;
}

.welcome {
  padding-top: 33px;
}

.welcome p {
  margin: 0;
  color: white;
  font-weight: bold;
  font-size: 20px;
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
  /* border: solid 1px #78e5b1; */
  background-color: white;
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
  color: #4ca066;
}

.register {
  background-color: #fff;
  height: 100%;
  z-index: 99;
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

  background-image: url("../assets/Peanut-butter-tarts.jpg");
  background-repeat: no-repeat;
  background-size: cover;
  height: 100%;
  min-height: 342px;

  transition: 0.75s ease-out;

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
.profile {
  display: inline-block;
  margin: 16px auto;
}
.profile span {
  margin-top: 6px;
  font-size: 10px;
  color: #505050;
}
.profile-pic {
  position: relative;
  margin: 0 auto;
  padding: 10px;
  width: 44px;
  height: 44px;

  border-radius: 50%;
  box-shadow: 0 0 6px 0 rgba(0, 0, 0, 0.16);
  background-color: #ffffff;

  display: table-cell;
  vertical-align: middle;
}
.profile-pic img {
  width: 100%;
}
</style>