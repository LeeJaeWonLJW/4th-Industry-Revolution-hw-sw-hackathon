<template>
	<div>
		<div class="container-box">
			<v-quagga class="barcode-scanner"
				:onDetected="logIt"
				:readerSize="readerSize"
				:readerType="'ean_reader'"
				:aspectRatio="aspectRatio"
			></v-quagga>
		</div>
		<div class="overlay"></div>
		<div class="barcode-ect">
			<span>바코드를 스캔해 주세요</span>
			<hr/>
			<div></div>
			<button @click="$router.push('/tab/barcode/input')">직접 추가</button>
		</div>
	</div>
</template>

<script>
export default {
	name: 'VueBarcodeTest',
	data () {
		return {
			readerSize: {
				width: 640,
				height: 640
			},
			aspectRatio: { min: 1, max: 2 },
			detecteds: []
		}
	},
	methods: {
		logIt (data) {
			console.log('detected', data)
		}

	}
}
</script>

<style scoped>
.container-box {
	width: 100%;
	height: 100%;
}
.barcode-scanner {
	position: fixed;
	z-index: 1;
}

.barcode-ect {
	position: fixed;
	z-index: 99;

	width: 300px;
	height: 300px;
	position: fixed;
	top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
	background: transparent;
	border: 1px solid #eee;
}
.barcode-ect span {
	width: 100%;
	position: absolute;
	color: #ffffff;
	font-size: 16px;
	text-align: center;
	top: -40px;
	transform: translate(-50%, -50%);
}
.barcode-ect hr {
	position: fixed;
	left: 20%;
	width: 60%;
	top: 50%;
	color: red;
	border: 1px solid red;
	z-index: 19;
}
.barcode-ect button {
	position: absolute;
	bottom: -80px;
	width: 141px;
  height: 34px;
  border-radius: 20px;
	border: 0;
  background-color: #ffffff;
	font-size: 15px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.4;
  letter-spacing: normal;
  text-align: center;
  color: #82d09a;
	transform: translate(-50%, -50%);
}
.tab {
	z-index: 99;
}
.overlay {
  position: fixed; /* Sit on top of the page content */
  width: 100%; /* Full width (cover the whole page) */
  height: 100%; /* Full height (cover the whole page) */
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(255,255,255,0.2); /* Black background with opacity */
  z-index: 10; /* Specify a stack order in case you're using a different order for other elements */
  cursor: pointer; /* Add a pointer on hover */
	transition: all 0.5s ease-out;
}
</style>