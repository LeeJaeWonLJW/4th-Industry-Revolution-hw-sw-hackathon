<template>
  <div id="app">
    <router-view />
    <!-- <div class="tab"></div> -->
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
@import url("https://use.typekit.net/ngp8myr.css");
@import url("http://fonts.googleapis.com/earlyaccess/notosanskr.css");

body {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 0;
  font-family: 'Noto Sans KR', sans-serif;
}

#app {
  position: relative;
  width: 100vw;
  height: 100%;
  min-height: 100vh;
  max-width: 640px;

  margin: 0;

  text-align: center;
  color: #2c3e50;

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  box-shadow: 0 4px 4px rgba(0, 23, 80, 0.02), 0 1px 6px rgba(0, 23, 80, 0.03),
    0 8px 8px rgba(0, 23, 80, 0.024), 0 16px 16px rgba(0, 23, 80, 0.024),
    8px 32px 32px rgba(0, 23, 80, 0.036), 8px 64px 64px rgba(0, 23, 80, 0.036);
}

.container {
  width: 90%;
  margin-left: auto;
  margin-right: auto;
}
.row {
  position: relative;
  width: 100%;
}
.row [class^="col"] {
  float: left;
  margin: 0.5rem 2%;
  min-height: 0.125rem;
}
.col-1,
.col-2,
.col-3,
.col-4,
.col-5,
.col-6,
.col-7,
.col-8,
.col-9,
.col-10,
.col-11,
.col-12 {
  width: 96%;
}
.col-1-sm {
  width: 4.33%;
}
.col-2-sm {
  width: 12.66%;
}
.col-3-sm {
  width: 21%;
}
.col-4-sm {
  width: 29.33%;
}
.col-5-sm {
  width: 37.66%;
}
.col-6-sm {
  width: 46%;
}
.col-7-sm {
  width: 54.33%;
}
.col-8-sm {
  width: 62.66%;
}
.col-9-sm {
  width: 71%;
}
.col-10-sm {
  width: 79.33%;
}
.col-11-sm {
  width: 87.66%;
}
.col-12-sm {
  width: 96%;
}
.row::after {
  content: "";
  display: table;
  clear: both;
}
.hidden-sm {
  display: none;
}

@media only screen and (min-width: 45em) {
  /* 720px */
  .col-1 {
    width: 4.33%;
  }
  .col-2 {
    width: 12.66%;
  }
  .col-3 {
    width: 21%;
  }
  .col-4 {
    width: 29.33%;
  }
  .col-5 {
    width: 37.66%;
  }
  .col-6 {
    width: 46%;
  }
  .col-7 {
    width: 54.33%;
  }
  .col-8 {
    width: 62.66%;
  }
  .col-9 {
    width: 71%;
  }
  .col-10 {
    width: 79.33%;
  }
  .col-11 {
    width: 87.66%;
  }
  .col-12 {
    width: 96%;
  }
  .hidden-sm {
    display: block;
  }
}


/* Custom Style */

.slider {
  display: flex;
  overflow-x: scroll;
  -webkit-overflow-scrolling: touch;
  scroll-snap-type: x mandatory;
  transition: 1s;
  scroll-behavior: smooth;
}
.slider::-webkit-scrollbar,
.slider::-webkit-scrollbar-thumb {
  display: none;
}

.slider > .item:first-child:after {
  position: relative;
  content: 'More >';
  bottom: 0;
  float: right;

  cursor: pointer;
}

.slider > .item {
  flex-shrink: 0;
  margin-right: 30px;
  scroll-snap-align: start;
}
.slider .item > h3,
.slider .item > p {
  margin-left: 4px;
}

.header {
  position: relative;
}
.header .menu-title {
  position: relative;
  height: 20px;
  padding: 16px 0;

  background-color: #ffffff;

  font-size: 14px;
  text-align: center;
  color: #505050;

  z-index: 99;
}
.header .info {
  position: relative;
  padding: 50px 16px 36px 16px;

  font-size: 12px;
  text-align: center;
  color: #ffffff;

  box-shadow: 0 0 14px 0 rgba(0, 0, 0, 0.16);
}
.header .info .title {
  font-size: 18px;
  text-shadow: 0 0 6px rgba(0, 0, 0, 0.16);
}

.contents {
  padding: 0 16px;
  margin-top: 44px;
  font-size: 10px;
  color: #505050;
}
.contents p {
  margin: 0;
}
.contents h3 {
  font-size: 16px;
  margin: 4px 0;
}
.contents h4 {
  font-size: 12px;
  margin: 4px 0;
}

.slider .item {
  width: 258px;
}

.diet-card {
  position: relative;
  margin: 8px 0;

  width: 100%;
  height: 160px;
  object-fit: contain;
  border-radius: 4px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.16);

  background-size: cover;
  background-repeat: no-repeat;

  cursor: pointer;
}


.footer {
  position: absolute;
  width: 100%;
  bottom: 0;
  margin-bottom: 16px;
}

.box-shadow {
  box-shadow: 0 0 6px 0 rgba(0, 0, 0, 0.16);
}
.info-circle {
  border-bottom-left-radius: 50% 54px;
  border-bottom-right-radius: 50% 54px;
}
.bg-green-gra-1 {
  background-image: linear-gradient(to top, #a7ffa3, #a1ffae, #8cffd1, #8bffd3);
}

.bg-white { background-color: #ffffff; }
.fd-color { color: #91ffb3; }

.fd-btn {
  width: 100%;
  height: 40px;
  line-height: 40px;
  border-radius: 20px;
  text-align: center;
  vertical-align: middle;
}
.fd-btn-sm {
  width: 110px;
  height: 28px;
  line-height: 28px;
  border-radius: 27px;
  text-align: center;
  vertical-align: middle;
}
.fd-btn-lg {
  width: 100%;
  max-width: 280px;

  margin: 16px auto;

  font-size: 14px;
  color: #ffffff;
  background-color: #91ffb3;
}
</style>