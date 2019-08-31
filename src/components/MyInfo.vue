<template>
  <div>
    <div class="top">
    </div>
    <div class="container">
      
    </div>
  </div>
</template>

<script>
import ProgressBar from '@/components/ProgressBar'
export default {
  name: 'index',
  components: {
    ProgressBar
  }
}
</script>

<style scoped>
.pull-left { float: left; }
.pull-right { float: right; }

.top {
  width: 100%;
  height: 276px;
  box-shadow: 0 0 14px 0 rgba(0, 0, 0, 0.16);
  background-image: linear-gradient(to bottom, #91a2ff, #91ffc9);
  border-bottom-left-radius: 50% 86px;
  border-bottom-right-radius: 50% 86px;
}

.top p {
  margin: 9px;
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
