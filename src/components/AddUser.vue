<template>
  <div>
    <div class="header">
      <div class="menu-title">친구추가</div>
      <div class="info bg-green-gra-1 box-shadow info-circle">
        <p class="title">'Foodiet'는 친구와 함께 할 때</p>
        <p class="title">목표에 달성하기 더 쉬워집니다.</p>

        <div class="btn-add fd-btn-sm fd-border-white margin-center"
          @click="e => e.target.closest('.info').classList.toggle('find-active')">친구추가</div>

        <input v-model="user_phone" class="fd-input" type="text" placeholder="010-XXXX-XXXX">
        <div class="btn-find fd-btn-sm fd-border-white margin-center"
          @click="find()">검색</div>
      </div>
    </div>

    <div class="contents" v-if="user">
      <div class="search-user-profile">
        <img :src="this.user_profile">
        <span class="user-name">{{this.user_name}}</span>
        <div @click="add()" class="fd-btn-sm fd-color bg-white fd-border user-add">친구추가</div>
      </div>
    </div>
		<div class='contents' v-else>
			<span class='user-name'>검색 결과가 없습니다</span>
		</div>
  </div>
</template>

<script>
import { APIService } from '../api/APIService'
import { async } from 'q'
const apiService = new APIService()

export default {
	name: 'freind_add',
	data: () => ({
		user: false,
		user_name: '',
		user_phone: '',
		user_profile: '',
  }),
	methods: {
		find: async function() {
			let friend = await apiService.friendSearch(this.user_phone)
			
			if(friend.success == true) this.user = true
			else this.user = false

			if(friend.data.name) this.user_name = friend.data.name
			if(friend.data.profile) this.user_profile = friend.data.profile
		},
		add: async function() {
			let friend = await apiService.friendAdd(this.user_phone)

			if(friend.success == true) alert('친구로 추가하였습니다')
			else console.error(friend.msg)
		}
	}
}
</script>

<style scoped>
.search-user-profile {
  position: relative;
  display: block;
}
.search-user-profile .user-name {
  position: relative;
  display: block;
}
.search-user-profile img {
  width: 80px;
}
.search-user-profile .fd-btn-sm {
  margin: 12px auto;
  border: 1px solid #505050;
}

.info {
  min-height: 10px;
}
.info .title {
  margin: 0;
}
.info .fd-btn-sm {
  margin-top: 24px;
}
.info .fd-input {
  margin: 0 auto;
  margin-top: 56px;
}

.info.find-active {
  min-height: 240px;
}
.info.result-active {
  min-height: 140px;
}

.info > .fd-input,
.info > .btn-find,
.info.find-active > .btn-add {
  display: none;
}

.info.find-active > .btn-find,
.info.find-active > .fd-input  {
  display: inline-block;
}

</style>
