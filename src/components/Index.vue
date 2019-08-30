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
        <p>GOAL</p>
      </div>
      <div class="container">
        <div class="row">
          <div class="col-2-sm">
            <div class="kg">
              <p>52KG</p>
            </div>
          </div>
          <div class="col-2-sm">
            <div class="kg">
              <p>52KG</p>
            </div>
          </div>
          <div class="col-4-sm">
            <div class="kg">
              <p>52KG</p>
            </div>
          </div>
          <div class="col-2-sm">
            <div class="kg">
              <p>52KG</p>
            </div>
          </div>
          <div class="col-2-sm">
            <div class="kg">
              <p>52KG</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'index'
}
</script>

<style scoped>
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

.kg p {
  font-family: sofia-pro, sans-serif;
  text-align: center;
  font-size: 8px;
  margin: 0;
  color: #9d9d9d;
}
</style>
