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
  </div>
</template>

<script>
export default {
  name: "index"
};
</script>

<style scoped>
.top {
  width: 100%;
  height: 192px;
  background-image: linear-gradient(to top, #a7ffa3, #8bffd3);
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.16);
  border-radius: 0px 0px 105px 105px;
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
}
</style>
