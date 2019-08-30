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
        <p class="position-relative">GOAL&nbsp;<i class="triangle_under position-absolute"></i></p>
      </div>
      <div class="container">
        <div class="row">
          <ProgressBar :image="require('../assets/user1.png')"></ProgressBar>
          <ProgressBar :image="require('../assets/user2.png')"></ProgressBar>
          <ProgressBar :image="require('../assets/profile.png')"
                       :active='true'></ProgressBar>
          <ProgressBar :image="require('../assets/user3.png')"></ProgressBar>
          <ProgressBar :image="require('../assets/user4.png')"></ProgressBar>

          <!-- <div class="col-2-sm goal-box">
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
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ProgressBar from '@/components/ProgressBar'
export default {
  name: 'index',
  components: {
    ProgressBar
  }
}
</script>

<style scoped>
.position-relative {
  position: relative;
}
.position-absolute {
  position: absolute;
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
