<template>

<div>
    <router-view/>
    <div class="tab">
        <div class="tab-button">
            <div class="btn btn-diary">
                <div class="icon"></div>
                <span class="text">Diary</span>
            </div>
            <div class="btn-barcode"></div>
            <div class="btn btn-me">
                <div class="icon"></div>
                <span class="text">Me</span>
            </div>
        </div>
    </div>
</div>

</template>

<style>
#app {
    min-height: calc(100vh - 56px);
    overflow: hidden;
}

.tab {
  position: fixed;
  bottom: 0;
  width: 100%;
  height: 56px;
  background: white;
}
.tab .tab-button {
    padding: 8px 54px;
}
.tab-button > div.active.focus, .tab-button > div.active:focus,
.tab-button > div.focus, .tab-button > div:active.focus, 
.tab-button > div:active:focus, .tab-button > div:focus {
  outline: none;
  box-shadow: none;
  background-color: white;
    pointer-events: auto;
}

.btn {
    color: #aaaaaa;
}
.btn.active {
    color: #91ffb3;
}

.btn-diary {
    float: left;
    width: 32px;
    margin: 0 auto;

    cursor: pointer;
    outline: none;
}
.btn-diary .icon {
    position: relative;
    width: 32px;
    height: 24px;
    background-image: url('../assets/btn_diary.png');
    background-repeat: no-repeat;
    background-size: cover;
}
.btn-diary .text {
    width: 24px;
    height: 8px;
    font-family: sofia-pro;
    font-size: 8px;
    font-weight: 500;
    font-style: normal;
    font-stretch: normal;
    letter-spacing: normal;
    text-align: center;
}

.btn-barcode {
    position: absolute;
    margin-left: auto;
    margin-right: auto;
    left: 0;
    right: 0;
    width: 52px;
    height: 34px;
    background-image: url('../assets/btn_barcode.png');
    background-repeat: no-repeat;
    background-size: cover;
    cursor: pointer;
    outline: none;
}

.btn-me {
    float: right;
    width: 32px;
    margin: 0 auto;

    cursor: pointer;
    outline: none;
}
.btn-me .icon {
    position: relative;
    width: 32px;
    height: 24px;
    background-image: url('../assets/btn_me.png');
    background-repeat: no-repeat;
    background-size: cover;
}
.btn-me .text {
    width: 24px;
    height: 8px;
    font-family: sofia-pro;
    font-size: 8px;
    font-weight: 500;
    font-style: normal;
    font-stretch: normal;
    letter-spacing: normal;
    text-align: center;
    color: #aaaaaa;
}
</style>

<script>
export default {
  name: 'default-layout'
}
</script>