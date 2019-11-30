<template>
  <div>
    <div class="top">
      <div class="profile">
        <img width="64" :src="this.profile" />
      </div>
      <div class="username">
        <p>{{this.name}}</p>
      </div>
      <div class="type">
        <p>{{this.purpose}}</p>
      </div>

      <div class="add-user"
        @click="$router.push('/tab/adduser')">
        <img src="../assets/icon/add_user.png">
      </div>
      <div class="setting"
				@click="$router.push('/')">
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
				<ProgressBar v-for="item in friendList" v-bind:active="item.index == 2 ? true : false"
					v-bind:key="item.index" v-bind:image="item.profile" v-bind:data-value="item.percent"
					v-bind:goal="item.goal_weight" v-bind:pre="item.weight" />
        <!-- <ProgressBar :image="require('../assets/user1.png')"
                      value="40%"></ProgressBar>
        <ProgressBar :image="require('../assets/user2.png')"
                     value="-10%"></ProgressBar>
        <ProgressBar :image="require('../assets/profile.png')"
                     :active='true'
                     value="60%"></ProgressBar>
        <ProgressBar :image="require('../assets/user3.png')"
                     value="70%"></ProgressBar>
        <ProgressBar :image="require('../assets/user4.png')"
                     value="80%"></ProgressBar> -->
      </div>
    </div>

    <div class="row">
      <ul class="menu-list">
        <li @click="$router.push('/tab/dietlist')">
          <img src="../assets/icon/cooking.png">
          <span>식단</span>
        </li>
        <li @click="$router.push('/tab/diarydetail')">
          <img src="../assets/icon/diagram.png">
          <span>상세정보</span>
        </li>
        <li>
          <img src="../assets/icon/bitcoin.png">
          <span>보유량: 10,000 point</span>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import ProgressBar from '@/components/ProgressBar'
import { APIService } from '../api/APIService'
import { async } from 'q'
import { parse } from 'path'
const apiService = new APIService()

export default {
	name: 'index',
	data: () => ({
		phone: '',
		name: '',
		profile: '',
		purpose: '',
		weight: 0,
		goal_weight: 0,
		now_weight: 0,
		friendList: Array,
	}),
  components: {
    ProgressBar
	},
	async beforeMount() {
		if(!localStorage.accessToken) this.$router.push('/')

		let user = await apiService.userInfo()
		let payload = user.payload.identity

		this.phone = payload.email
		this.name = payload.name
		this.purpose = payload.purpose
		this.weight = payload.weight
		this.goal_weight = payload.goal_weight
		this.now_weight = payload.now_weight

		let profile = await apiService.friendSearch(this.phone)
		this.profile = 'data:image/png;base64,' + profile.data.profile.replace('data:image/png;base64,', '').replace('data:image/jpeg;base64,', '')

		let friendList = await apiService.friendList()
		let array = []

		await friendList.friends.forEach((obj, index) => {
			if(index == 2) {
				let data = {}
				data.index = index
				data.percent = Math.abs( (parseInt(this.now_weight) - parseInt(this.weight)) / (parseInt(this.goal_weight)-parseInt(this.weight)) ) * 100 + '%'
				data.profile = this.profile
				data.weight = this.weight
				data.goal_weight = this.goal_weight
				array.push(data)
				index++
			}

			let data = {}
			data.index = index
			data.percent = Math.abs( (parseInt(obj.now_weight) - parseInt(obj.weight)) / (parseInt(obj.goal_weight)-parseInt(obj.weight)) ) * 100 + '%'
			data.profile = obj.profile
			data.weight = obj.weight
			data.goal_weight = obj.goal_weight
			array.push(data)
		})
		
		if(friendList.length <= 1) {
			let data = {}
			data.index = 2
			data.percent = Math.abs( (parseInt(this.now_weight) - parseInt(this.weight)) / (parseInt(this.goal_weight)-parseInt(this.weight)) ) * 100 + '%'
			data.profile = this.profile
			data.weight = this.weight
			data.goal_weight = this.goal_weight
			array.push(data)
		}
		this.friendList = array
		console.log(this.friendList)
	}
}
</script>

<style scoped>
.menu-list {
  position: relative;
  /* display: inline-block; */

  margin: 16px 16px;
  padding: 6px 0;
  border-top: 8px solid #d3ffe1;
  border-bottom: 8px solid #d3ffe1;

  list-style: none;
}
.menu-list li {
  text-align: left;
  padding: 16px 24px;
  margin: auto 8px;
  border-bottom: 1px solid #eeeeee;
  cursor: pointer;
}
.menu-list li span {
  margin-left: 20px;
  font-size: 14px;
  line-height: 24px;
  color: #808080;
}
.menu-list li img {
  width: 24px;
  vertical-align: bottom;
}
.menu-list li:last-child {
  border: none;
}

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

.add-user {
  position: absolute;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  margin: 20px 0 0 26px;
}
.add-user img {
  width: 100%;
  height: 100%;
}

.top {
  width: 100%;
  height: 192px;
  background-image: linear-gradient(to top, #a7ffa3, #8bffd3);
  box-shadow: 0 5px 20px 0 rgba(0, 0, 0, 0.16);
  border-bottom-left-radius: 50% 86px;
  border-bottom-right-radius: 50% 86px;
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
