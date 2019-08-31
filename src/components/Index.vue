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

      <div class="setting">
        <img class="rotating" src="../assets/setting.png">
      </div>
    </div>
    <div class="container">
      <div class="row view-type">
        <div class="pull-left">
          <ul class="view-purpose-type">
            <li>체중감량</li>
            <li class="active">목표수행</li>
          </ul>
        </div>
        <div class="pull-right">
          <select class="view-data-type">
            <option>친구</option>
          </select>
        </div>
      </div>

      <div class="row user-friends">
        <ProgressBar :image="require('../assets/user1.png')"
                      value="40%"></ProgressBar>
        <ProgressBar :image="require('../assets/user2.png')"
                     value="50%"></ProgressBar>
        <ProgressBar :image="require('../assets/profile.png')"
                     :active='true'
                     value="60%"></ProgressBar>
        <ProgressBar :image="require('../assets/user3.png')"
                     value="70%"></ProgressBar>
        <ProgressBar :image="require('../assets/user4.png')"
                     value="80%"></ProgressBar>
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
.pull-left { float: left; }
.pull-right { float: right; }

.setting {
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  height: 20px;
  margin: 20px 26px 0 0;
}
.setting img {
  width: 100%;
  height: 100%;
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

.view-type {
  margin: 35px 0 10px 0;
}

ul.view-purpose-type {
  color: #d5d5d5;
  list-style: none;
  padding: 0;
  margin: 0;

  font-size: 12px;
  font-family: SourceHanSansK;
}
ul.view-purpose-type li {
  float: left;
  margin-right: 8px;
  padding-right: 8px;
  border-right: 1px solid #d5d5d5;
  cursor: pointer;
}
ul.view-purpose-type li:last-child {
  margin-right: 0px;
  padding-right: 0px;
  border: 0;
}
ul.view-purpose-type li.active {
  color: #505050;
}

select.view-data-type {
  background: none;
  border: none;
  
  height: 17px;
  font-family: SourceHanSansK;
  font-size: 12px;
  color: #91a2ff;
}

.triangle_under {
  position: absolute;
  width: 0px;
  height: 0px;
  top: 60%;
  border-top: 6px solid #9d9d9d;
  border-bottom: 6px solid none;
  border-right: 5px solid transparent;
  border-left: 5px solid  transparent;
}

@-webkit-keyframes rotating /* Safari and Chrome */ {
  from {
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes rotating {
  from {
    -ms-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -webkit-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  to {
    -ms-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -webkit-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
.rotating {
  -webkit-animation: rotating 2s linear infinite;
  -moz-animation: rotating 2s linear infinite;
  -ms-animation: rotating 2s linear infinite;
  -o-animation: rotating 2s linear infinite;
  animation: rotating 2s linear infinite;
}
</style>
