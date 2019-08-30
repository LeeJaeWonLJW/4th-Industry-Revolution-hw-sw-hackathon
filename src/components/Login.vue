<template>
  <div class="login">
    <div class="logo">
      <h1>FooDiet</h1>
      <p>Food + Diet</p>
    </div>
    <div class="welcome">
      <p>환영합니다</p>
    </div>
    <div class="btn-group">
      <div class="btn">
        <p>회원가입</p>
      </div>
      <div class="btn">
        <p>로그인</p>
      </div>
    </div>
  </div>
</template>


<script>
export default {
  name: "login"
};
</script>

<style scoped>
.login {
  background-color: #91ffb3;
  height: 100%;
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
  border: solid 1px #ffffff;
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
  color: #60fd91;
}
</style>