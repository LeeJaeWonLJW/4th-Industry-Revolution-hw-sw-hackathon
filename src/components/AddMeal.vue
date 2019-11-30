<template>
  <div>
    <div class="header">
      <div class="info info-circle bg-blgn-gra-1 box-shadow">
        <span class="title">기록</span>
        <div class="fd-input-search">
          <img src="../assets/icon/input_icon.png">
          <input class="fd-input" type="text" placeholder="음식 검색">
        </div>
      </div>
    </div>

    <div class="contents">
      <div class="add-item-box">
        <span class="title">추가한 항목:</span>
        <div class="item">
					<div class="pull-left" @click="$router.push('/tab/mealdetail')">
						<span class="title">핫식스</span>
						<span class="info">115 Kcal, 1캔 (240ml)</span>
					</div>
					<div class="pull-right">
					<span style="padding-top: 12px; padding-right:8px;"><img :src="this.check ? require('../assets/icon/un_like.png') : require('../assets/icon/like.png')" @click="this.check = !this.check"></span>
					<span style="padding-top: 6px; padding-right:4px;" class="close" @click="this.check = false">&#215;</span>
					</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
	name: 'addMeal',
	data: () => ({
		check: false
	})
}
</script>

<style scoped>
.item img {
	width: 24px;
}
.item .close {
	font-size: 20px;
}
.header .info {
  padding: 16px;
  padding-bottom: 78px;
}
.fd-input-search {
  margin-top: 18px;
  position: relative;
}
.fd-input-search img {
  position: absolute;
  display: inline;
  top: 8px;
  left: 8px;
  width: 24px;
  height: 24px;
  
}
.fd-input {
  width: 90%;
  height: 40px;
  border-radius: 20px;
  text-align: left;
  padding-left: 38px;
}

.contents {
  padding: 0;
  text-align: left;
}

.add-item-box span {
  padding-left: 16px;
  margin-bottom: 12px;
  font-size: 16px;
  color: #94b4ee;
}
.add-item-box .item {
	display: flex;
	position: relative;
  padding: 14px 28px;
  margin-top: 12px;
  color: #505050;
  background-color: rgba(144, 255, 202, .2);
}
.add-item-box .item .pull-left {
	position: relative;
	display: flex;
	flex: 1;
	flex-direction: column;
}
.add-item-box .item .pull-right {
	display: flex;
	position: relative;
}
.add-item-box .item .pull-right span {
}
.add-item-box .item span {
  position: relative;
  display: block;
	margin: 0;
	padding: 0;
}	
.add-item-box .item span.title {
  font-size: 16px;
  font-weight: bold;
  top: 0;
}
.add-item-box .item span.info {
  font-size: 12px;
  bottom: 0;
}
</style>