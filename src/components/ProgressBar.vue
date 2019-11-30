<template>
  <div :class="this.column">
    <p class="goal-kg">{{this.goal}}KG</p>
    <div class="progress-bar">
      <div v-bind:style="this.height" class="percent" v-bind:data-value="this.value"></div>
    </div>
    <p class="start-kg">{{this.pre}}KG</p>
    <img class="user-img" :src="this.image" />
  </div>
</template>

<script>
export default {
  name: 'progress-bar',
  props: {
    goal: {
      type: Number,
      default: 0
    },
    pre: {
      type: Number,
      default: 0
    },
    active: {
      type: Boolean,
      default: false
    },
    value: {
      type: String,
      default: ''
    },
    image: {
      type: String,
      default: ''
    }
  },
  computed: {
    column: function() {
      return this.active ? 'per-32 goal-box active' : 'per-16 goal-box'
    },
    height: function() {
      return 'height: ' + this.value + ';'
    }
  }
}
</script>

<style scoped>
.scroll-box {
	display: -webkit-inline-box;
	overflow-x: scroll;
}
.per-16 {
	width: 16.6%;
}
.per-32 {
	width: 34%;
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
.goal-box.active .progress-bar .percent {
  opacity: 1;
  background-color: #a7ffa3;
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

.goal-box .progress-bar .percent {
  position: absolute;
  display: inline-block;
  left: 0;
  bottom: 0;
  width: 100%;

  content: "";
  border-radius: 12px;
  background-color: #91a2ff;
}

.goal-box img.user-img {
  display: inline-block;
  width: 40px;
  height: 40px;
  margin: 8px 0;
  border-radius: 50%;
}
</style>
