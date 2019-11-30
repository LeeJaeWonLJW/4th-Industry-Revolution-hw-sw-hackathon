<template>
  <div>
    <div class="top">
      <p class="date">{{ this.today }}</p>

      <div class="daily-purpose-progress">
        <div class="today-kcal">
          <p class="h3">{{ this.kcal }}</p>
          <p class="h4">오늘 먹은 칼로리</p>
        </div>
        
        <div class="now-kcal">
          <p class="h3">{{ 2000 - this.kcal }}</p>
          <p class="h4">남은 칼로리</p>
        </div>

        <div class="now-percent">
          <p class="h3">17%</p>
          <p class="h4">현재 수행률</p>
        </div>
      </div>

      <div class="nutrient">
        <div class="item dan">
          <p class="gram">{{ this.protein }}g먹음</p>
          <p class="explain">단백질</p>
        </div>

        <div class="item tan">
          <p class="gram">{{ this.crab }}g먹음</p>
          <p class="explain">탄수화물</p>
        </div>

        <div class="item ji">
          <p class="gram">{{ this.fat }}g먹음</p>
          <p class="explain">지방</p>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="diary-kg">
        <div class="pull-left">
          <p class="kg">{{ this.now_weight }}</p>
          <p>현재 체중</p>
        </div>
        <div class="pull-right">
          <p class="kg">{{ this.goal_weight }}</p>
          <p>목표 체중</p>
        </div>
      </div>

      <div class="diary-update">
        <div class="btn-kg-update" @click="visible_form = true">
          오늘 몸무게 업데이트하기
        </div>

        <div class="meal-update">
          <div class="item">
            <img src="../assets/breakfast_1.png">
            <div class="info">
              <p>아침 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus" @click="$router.push('/tab/addmeal/breakfast')"></a>
          </div>

          <div class="item">
            <img src="../assets/breakfast.png">
            <div class="info">
              <p>점심 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus" @click="$router.push('/tab/addmeal/lunch')"></a>
          </div>

          <div class="item">
            <img src="../assets/bell-covering-hot-dish.png">
            <div class="info">
              <p>저녁 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus" @click="$router.push('/tab/addmeal/dinner')"></a>
          </div>

          <div class="item">
            <img src="../assets/chocolate.png">
            <div class="info">
              <p>간식 추가</p>
              <p>추천 498 - 697 Kcal</p>
            </div>
            <a class="btn-plus" @click="$router.push('/tab/addmeal/none')"></a>
          </div>
        </div>
      </div>
    </div>

		<div v-if="visible_form" class="overlay" @click="visible_form=false"></div>
		<div v-if="visible_form" class="update-form">
			<div class="update-form-header">
				몸무게 업데이트
				<span class="pull-right" @click="visible_form=false">&#215;</span>	
			</div>
			<div class="update-form-body">
				<div style="width: 100%;">
					<label>KG</label>
					<input type="number" v-model="update_weight">
				</div>
				
				<div style='display: -webkit-inline-box; margin: 24px 0;'>
					<button class="btn" @click="submit()">입력</button>
				</div>
			</div>
		</div>
  </div>
</template>

<script>
import moment from 'moment'
import { APIService } from '../api/APIService'
import { async } from 'q'
const apiService = new APIService()

export default {
	name: 'diary',
	data: () => ({
		kcal: 0,
		crab: 0,
		protein: 0,
		fat: 0,
		goal_weight: 0,
		now_weight: 0,
		visible_form: false,
		today: '',
		clean_today: '',
		update_weight: 0,
	}),
	beforeMount: async function() {
		let date = new Date()
		let month = date.getMonth() >= 10 ? date.getMonth() : '0' + date.getMonth()
		let day = date.getDate() >= 10 ? date.getDate() : '0' + date.getDate()
		let year = date.getFullYear()
		this.today = year + '.' + month + '.' + day
		this.clean_today = String(year) + String(month) + String(day)

		if(!localStorage.accessToken) this.$router.push('/')

		this.set_user()

		let res = await apiService.get_meal(this.clean_today)
	
		await res.breakfast.forEach(async (key, index) => {
			let info = await apiService.foodInfo(key)
			this.kcal += info.kcal
			this.protein += info.protein
			this.crab += info.carbohydrate
			this.fat += info.fat
		})
		await res.lunch.forEach(async (key, index) => {
			let info = await apiService.foodInfo(key)
			this.kcal += info.kcal
			this.protein += info.protein
			this.crab += info.carbohydrate
			this.fat += info.fat
		})
		await res.dinner.forEach(async (key, index) => {
			let info = await apiService.foodInfo(key)
			this.kcal += info.kcal
			this.protein += info.protein
			this.crab += info.carbohydrate
			this.fat += info.fat
		})

	},
	methods: {
		set_user: async function() {
			let user = await apiService.userInfo()
			let payload = user.payload.identity
			this.goal_weight = payload.goal_weight
			this.now_weight = payload.now_weight
		},
		submit: async function() {
			let res = await apiService.post_weight(this.clean_today, this.update_weight)
			if(res.success == true) {
				alert('업데이트 완료')
				this.visible_form = false
				
				let res2 = await apiService.get_weight(this.clean_today)
				this.now_weight = parseInt(res2.weight)
			}
		}
	}
}
</script>

<style scoped>
.pull-left { float: left; }
.pull-right { float: right; }

.update-form {
	width: 300px;
	height: 200px;
	position: fixed;
	top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
	z-index: 99;
	background-color: #ffffff;
	border-radius: 20px;
	box-shadow: 0 1px 4px 1px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24);
	transition: all 0.5s ease-out;
}
.update-form-header {
	display: block;
	position: relative;
	padding: 10px 20px;
	border-radius: 20px 20px 0 0;
	background-color: #91b5f3;
	color: #ffffff;
	font-size: 16px;
}
.update-form-header span {
	font-size: 16px;
}
.update-form-body {
	position: relative;
	padding: 20px;
	padding-top: 40px;
	text-align: center;
}
.update-form-body label {
	position: absolute;
	right: 20%;
}
.update-form-body input {
	width: 70%;
	border: 0;
	border-bottom: 2px solid #8f8f8f;
	padding: 4px;
}
.update-form-body input:focus {
	outline: none;
}
.update-form-body button {
	display: block;
	width: 54px;
	height: 24px;
	border-radius: 12px;
	border: 1px solid #91b5f3;
	background-color: transparent;
	color: #91b5f3;
}
.overlay {
  position: fixed; /* Sit on top of the page content */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255,255,255,0.5); /* Black background with opacity */
  z-index: 2; /* Specify a stack order in case you're using a different order for other elements */
  cursor: pointer; /* Add a pointer on hover */
	transition: all 0.5s ease-out;
}
.update-notice {
	width: 16px;
	height: 16px;
	padding: 2px;
	border-radius: 50%;
	background-color: red;
	color: #ffffff;
	font-size: 10px;
}
.top {
  position: relative;
  display: inline-block;

  width: 100%;
  height: 276px;
  padding-top: 12px;
  box-shadow: 0 0 14px 0 rgba(0, 0, 0, 0.16);
  background-image: linear-gradient(to bottom, #91a2ff, #91ffc9);
  border-bottom-left-radius: 50% 86px;
  border-bottom-right-radius: 50% 86px;

  font-family: SofiaPro;
  text-align: center;
  color: #ffffff;
}

.top .h3 {
  font-size: 20px;
  margin: 0;
}
.top .h4 {
  font-size: 10px;
  margin: 0;
}

.top .date {
  font-family: SofiaPro;
  font-size: 14px;
}

.top .daily-purpose-progress {
  position: relative;
  height: 93px;
  padding: 0 32px 0 22px;
}
.top .daily-purpose-progress > div {
  position: relative;
  display: inline-block;
  text-align: center;
}

.top .daily-purpose-progress .now-kcal {
  position: absolute;
  width: 93px;
  height: 100%;
  border: 1px solid #ffffff;
  border-radius: 50%;

  margin-right: auto;
  margin-left: auto;
  left: 0;
  right: 0;
}
.now-kcal p.h3 {
  margin-top: 18px;
}
.now-kcal p.h4 {
  margin-top: 2px;
}

.top .today-kcal {
  position: absolute;
  float: left;
  height: 100%;
  margin-top: 18px;
}

.top .now-percent {
  position: absolute;
  float: right;
  height: 100%;
  margin-top: 18px;
}


.top .nutrient {
  position: relative;
  min-height: 48px;
  padding: 20px 56px;

  font-size: 10px;
}
.nutrient .item {
  position: relative;
  display: inline-block;
}

.nutrient .item p {
  margin: 0;
}
.nutrient .item p.explain {
  margin-top: 4px;
  padding-top: 4px;
  border-top: 1px solid #ffffff;
}

.nutrient .item.dan {
  float: left;
}
.nutrient .item.ji {
  float: right;
}
.nutrient .item.tan {
  margin-right: auto;
  margin-left: auto;
  left: 0;
  right: 0;
}


.diary-kg {
  position: relative;
  padding: 25px 24px;
  color: #91b1f6;
  font-size: 12px;
}
.diary-kg > div {
  position: relative;
  display: inline-block;
}
.diary-kg p {
  margin: 0;
}
.diary-kg .kg {
  font-size: 18px;
}


.diary-update {
  padding: 25px 30px;
  margin-top: 10px;
}
.diary-update .btn-kg-update {
  min-width: 262px;
  height: 46px;
  line-height: 46px;
  border-radius: 23px;
  background-color: #91b5f3;

  vertical-align: middle;
  font-size: 12px;
  color: #ffffff;
}

.diary-update .meal-update {
  color: #808080;
  font-size: 12px;
}
.meal-update p {
  margin: 0;
}
.meal-update .item {
  position: relative;
  display: inline-block;
  width: 100%;
  height: 36px;
  margin-top: 24px;
  text-align: left;
}
.meal-update .item img {
  width: 40px;
  max-height: 36px;
}
.meal-update .item .info {
  display: inline-block;
  height: 100%;
  margin-left: 20px;
}
.meal-update .item .info p:first-child {
  font-size: 14px;
  font-weight: bold;
}
.meal-update .btn-plus {
  float: right;
  margin-top: 6px;
  width: 24px;
  height: 24px;
  background-color: #91b1f6;
  border-radius: 50%;
}
.meal-update .btn-plus {
  background-image: url('../assets/icon/add.png');
  background-repeat: no-repeat;
  background-position: center;
  background-size: 14px;
}

.view-type {
  margin: 25px 0 10px 0;
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
