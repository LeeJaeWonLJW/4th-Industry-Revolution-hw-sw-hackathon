<template>
  <div class="col-6-sm item">
    <img :src="this.image"/>
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
  padding: 13px 8px;
}
.item img {
  position: relative;
  width: 100%;
  border-radius: 4px;
}
.item .text {
  position: absolute;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  width: 80%;
  font-size: 12px;
  color: #909090;
  border-bottom: 1px solid #91ffb3;
  padding: 6px 0;
}
</style>