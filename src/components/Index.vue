<template>
  <div>
    <div class="top">
      <div class="profile">
        <img width="64" src="../assets/profile.png" />
      </div>
      <div class="username">
        <p>공유</p>
      </div>
      <div class="type">
        <p>LOSE WEIGHT</p>
      </div>
    </div>
    <div>
      <div class="ranking-top">
        <p class="position-relative">GOAL<i class="triangle_under position-absolute"></i></p>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-2-sm goal-box">
            <p class="goal-kg">52KG</p>
            <div class="progress-bar" data-value="40%"></div>
            <p class="start-kg">60KG</p>
            <img class="user-img" src="../assets/user1.png">
          </div>
          <div class="col-2-sm goal-box">
            <p class="goal-kg">52KG</p>
            <div class="progress-bar" data-value="40%"></div>
            <p class="start-kg">60KG</p>
            <img class="user-img" src="../assets/user2.png">
          </div>
          <div class="col-4-sm goal-box active">
            <p class="goal-kg">52KG</p>
            <div class="progress-bar" data-value="40%"></div>
            <p class="start-kg">60KG</p>
            <img class="user-img" src="../assets/profile.png">
          </div>
          <div class="col-2-sm goal-box">
            <p class="goal-kg">52KG</p>
            <div class="progress-bar" data-value="40%"></div>
            <p class="start-kg">60KG</p>
            <img class="user-img" src="../assets/user3.png">
          </div>
          <div class="col-2-sm goal-box">
            <p class="goal-kg">52KG</p>
            <div class="progress-bar" data-value="40%"></div>
            <p class="start-kg">60KG</p>
            <img class="user-img" src="../assets/user4.png">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "index"
};
</script>

<style scoped>
.position-relative {
  position: relative;
}
.position-absolute {
  position: absolute;
}

.goal-box {
  align-items: center;
}
.goal-box.active {
  border-radius: 14px;
  background-color: #e7e7e7;
}
.goal-box.active .progress-bar {
  width: 33.4px;
  background-color: #fff;
}
.goal-box.active .progress-bar::after {
  opacity: 1;
}
.goal-box.active p {
  font-size: 11px;
}
.goal-box.active img.user-img {
  width: 54.8px;
  height: 54.8px;
}

.goal-box p {
  font-family: sofia-pro, sans-serif;
  text-align: center;
  font-size: 10px;
  margin: 0;
  color: #9d9d9d;
}
.goal-box p.goal-kg {
  margin: 8px 0;
}
.goal-box p.start-kg {
  margin: 5px 0;
}

.goal-box .progress-bar {
  position: relative;
  display: inline-block;
  width: 28px;
  height: 108px;
  margin: 5px 0;
  border-radius: 12px;
  background-color: #f4f2f2;
}
.goal-box .progress-bar::after {
  position: absolute;
  display: inline-block;
  left: 0;
  bottom: 0;
  width: 100%;
  height: 54px;

  content: '';
  opacity: 0.3;
  border-radius: 12px;
  background-color: #a7ffa3;
}

.goal-box img.user-img {
  display: inline-block;
  width: 40px;
  height: 40px;
  margin: 8px 0;
  border-radius: 50%;
}

.top {
  width: 100%;
  height: 192px;
  background-image: linear-gradient(to top, #a7ffa3, #8bffd3);
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.16);
  border-radius: 0px 0px 65px 65px;
}

.top p {
  margin: 9px;
}

.profile {
  padding-top: 44px;
}

.username {
  font-weight: bold;
  font-size: 23px;
  color: white;
  letter-spacing: normal;
}

.type {
  color: white;
  font-size: 12px;
}

.ranking-top p {
  padding-top: 11px;
  font-family: safia-pro, sans-serif;
  color: #9d9d9d;
  line-height: 1.2;
  font-weight: normal;
  font-size: 15px;
}

.triangle_under {
  width: 0px;
  height: 0px;
  top: 60%;
  border-top: 6px solid #9d9d9d;
  border-bottom: 6px solid none;
  border-right: 5px solid transparent;
  border-left: 5px solid  transparent;
}
</style>
