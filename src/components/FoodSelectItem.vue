<template>
  <div class="col-6-sm item">
    <img :src="this.image"/>
    <div class="checkbox">
      <img src="../assets/icon/checked.png">
    </div>
    <span class="text">{{this.food}}</span>
  </div>
</template>

<script>
export default {
  name: "select-box-item",
  props: {
    food: {
      type: Number
    },
    image: {
      type: String
    }
  }
};
</script>

<style scoped>
.item {
  position: relative;
  display: inline-block;
  
  /* padding: 13px 8px; */

  opacity: 1;
  cursor: pointer;

  transition: 0.5s ease;
}
.item > img {
  position: relative;
  width: 100%;
  border-radius: 4px;
  transition: 0.5s ease-out;
}
.item .checkbox {
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
  transition: 0.5s ease-out;
}

.item:hover .text {
  color: #91ffb3
}
.item:hover > img,
.item.active > img {
  opacity: 0.4;
}
.item:hover .checkbox,
.item.active .checkbox {
  opacity: 1;
}

.item .text {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  font-size: 12px;
  color: #909090;
  border-bottom: 1px solid #91ffb3;
  padding: 6px 0;
  transition: 0.5s ease-out;
}
</style>