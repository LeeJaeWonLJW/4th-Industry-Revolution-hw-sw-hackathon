<template>
  <div>
    <div class="header">
      <div class="menu-title">친구추가</div>
      <div class="info bg-green-gra-1 box-shadow info-circle">
        <p class="title">'Foodiet'는 친구와 함께 할 때</p>
        <p class="title">목표에 달성하기 더 쉬워집니다.</p>

        <div class="btn-add fd-btn-sm fd-border-white margin-center"
          @click="e => e.target.closest('.info').classList.toggle('find-active')">친구추가</div>

        <input class="fd-input" type="text" placeholder="010-XXXX-XXXX">
        <div class="btn-find fd-btn-sm fd-border-white margin-center"
          @click="e => e.target.closest('.info').classList.toggle('result-active')">검색</div>
      </div>
    </div>

    <div class="contents">
      <div class="search-user-profile">
        <img src="../assets/user1.png">
        <span class="user-name">김철수</span>
        <div class="fd-btn-sm fd-color bg-white fd-border user-add">친구추가</div>
      </div>
    </div>

    <div class="footer">
      <div class="fd-btn fd-btn-lg"
        @click="$router.push('/tab/index')">다음</div>
    </div>
  </div>
</template>

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
  min-height: 280px;
}
.info.result-active {
  min-height: 140px;
}

.info.find-active > .btn-find,
.info.find-active > .fd-input,
.info.result-active > .fd-input
.info.info.result-active >  {
  display: block;
}

.info > .fd-input,
.info > .btn-find,
.info.find-active > .btn-add,
.info.result-active > .btn-find {
  display: none;

}

</style>