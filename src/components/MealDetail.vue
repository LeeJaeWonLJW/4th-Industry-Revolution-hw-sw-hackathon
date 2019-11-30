<template>
  <div>
    <div class="header">
      <div class="info info-circle bg-blgn-gra-1 box-shadow">
        <span class="meal-title">{{ this.name }}</span>
      </div>
    </div>

    <div class="contents">
      <div>
        <input class="fd-input" type="text" v-model="count" />
        <input class="fd-input volume" type="text" v-model="amount" />
      </div>

			<div class="control-box">
				<span @click="check('breakfast')" v-bind:class="{ active: select == 'breakfast' }">아침</span>
				<span @click="check('lunch')" v-bind:class="{ active: select == 'lunch' }">점심</span>
				<span @click="check('dinner')" v-bind:class="{ active: select == 'dinner' }">저녁</span>
				<span @click="check('g')" v-bind:class="{ active: select == 'g' }">간식</span>
			</div>
      <div class="fd-btn fd-btn-lg" @click="submit()">Diary에 담기</div>

      <p class="title">{{ this.kcal }}Kcal</p>

      <div class="pigure">
        <div class="pull-left">{{ this.ex1 }}</div>
        <div class="pull-right">{{ this.ex2 }}</div>
      </div>

      <p class="title">영양정보</p>
      <ul class="nut">
        <li class="bold">
          <span class="nut-name">탄수화물</span>
          <span class="nut-val">{{ this.crab }}g</span>
        </li>
        <li>
          <span class="nut-name">섬유질</span>
          <span class="nut-val">{{ this.sumu }}g</span>
        </li>
        <li>
          <span class="nut-name">설탕</span>
          <span class="nut-val">{{ this.sugar }}g</span>
        </li>
        <li class="bold">
          <span class="nut-name">단백질</span>
          <span class="nut-val">{{ this.protein }}g</span>
        </li>
        <li class="bold">
          <span class="nut-name">지방</span>
          <span class="nut-val">{{ this.fat }}g</span>
        </li>
        <li>
          <span class="nut-name">불포화지방</span>
          <span class="nut-val">{{ this.fat1 }}g</span>
        </li>
        <li>
          <span class="nut-name">포화지방</span>
          <span class="nut-val">{{ this.fat2 }}g</span>
        </li>
        <li class="bold">
          <span class="nut-name">기타</span>
          <span class="nut-val">{{ this.etc }}g</span>
        </li>
        <li>
          <span class="nut-name">칼륨</span>
          <span class="nut-val">{{ this.ca }}g</span>
        </li>
        <li>
          <span class="nut-name">콜레스트롤</span>
          <span class="nut-val">{{ this.co }}g</span>
        </li>
        <li>
          <span class="nut-name">나트륨</span>
          <span class="nut-val">{{ this.na }}mg</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { APIService } from '../api/APIService'
import { async } from 'q'
import { parse } from 'path'
const apiService = new APIService()
export default {
	name: 'diary_',
	data: () => ({
		food_id: '',
		name: '',
		select: 'breakfast',
		count: 1,
		amount: '250ml',
		kcal: 0,
		crab: 0,
		sumu: 0,
		sugar: 0,
		protein: 0,
		fat: 0,
		fat1: 0,
		fat2: 0,
		etc: 0,
		ca: 0,
		co: 0,
		na: 0,
		ex1: '200 Nice',
		ex2: '404 Foward',
		clean_today: '',
	}),
	beforeMount: async function() {
		let id = location.pathname.split('/')[3]
		let res = await apiService.foodInfo(id)

		this.food_id = id
		this.name = res.name
		this.amount = res.volume
		this.kcal = res.kcal
		this.crab = res.carbohydrate
		this.sugar = res.sugar
		this.protein = res.protein
		this.fat = res.fat
		this.fat1 = res.saturated_fat
		this.fat2 = res.monounsaturated_fat
		this.ca = res.calcium
		this.co = res.cholesterol
		this.na = res.sodium

		let date = new Date()
		let month = date.getMonth() >= 10 ? date.getMonth() : '0' + date.getMonth()
		let day = date.getDate() >= 10 ? date.getDate() : '0' + date.getDate()
		let year = date.getFullYear()
		this.clean_today = String(year) + String(month) + String(day)
	},
	methods: {
		check: function(val) {
			this.select = val
		},
		submit: async function() {
			let res = await apiService.foodAddEat(this.clean_today, this.select, this.food_id)
			console.log(res)
		}
	}
}
</script>

<style scoped>
.meal-title {
  font-size: 44px;
    text-shadow: 0 0 6px rgba(0, 0, 0, 0.16);
  line-height: 0.64;

}

.control-box {
	margin: 12px;
}
.control-box > span {
	display: inline-block;
	position: relative;
	margin: 0 6px;
	min-width: 57px;
	line-height: 28px;
  height: 28px;
  border-radius: 14px;
  border: solid 0.2px #808080;
  background-color: #ffffff;
	font-size: 14px;
	vertical-align: middle;	
}
.control-box > span.active {
	color: #ffffff;
	border: none;
	background-color: #91ffb3;
}
.control-Ad {
	width: 57px;
  height: 34px;
  border-radius: 16px;
  background-color: #91ffb3;
}

.fd-input {
  margin: auto 13px;
  width: 58px;
  height: 34px;
  border-radius: 8px;
  border: solid 1px #808080;
}
.fd-input.volume {
  padding-right: 8px;
  text-align: right;
  width: 142px;
}
.contents .title {
  font-family: SofiaPro;
  font-size: 16px;
  font-weight: bold;
  text-align: left;
  margin: 14px 0 6px 28px;
  color: #808080;
}

.pigure {
  margin: 8px auto;
  padding: 16px 8px;
  border-top: 1px solid #94b2ef;
  border-bottom: 1px solid #94b2ef;
}
.pigure:after {
  position: relative;
  display: block;
  height: 15px;
  left: 50%;
  border-left: 1px solid #94b2ef;
  content: "";
}
.pigure > div {
  position: relative;
  display: block;
  width: 50%;
}
.pigure > div:first-child {
  font-size: 12px;
  color: #94b2ef;
}
.pigure > div:last-child {
  font-size: 12px;
  color: #ff7676;
}

ul.nut {
  position: relative;
  list-style: none;
  margin: 0;
  padding: 0;

  color: #808080;
}
ul.nut li {
  position: relative;
  display: inline-block;
  width: 80%;
  margin: 2px auto;
}
ul.nut li span.nut-name {
  width: 48px;
  float: left;
  text-align: right;
}
ul.nut li span.nut-val {
  min-width: 48px;
  float: right;
  text-align: left;
}
ul.nut li:after {
  position: absolute;

  width: 55%;
  height: 1px;
  margin: 7px auto;
  left: 0;
  right: 0;

  border-top: 1px dashed #808080;
  content: "";
}

ul.nut li.bold {
  color: #505050;
}
ul.nut li.bold:after {
  border-top: 1px solid #909090;
}

ul.nut li.bold {
  padding-top: 4px;
  border-top: 2px solid #eff4fd;
}
</style>
