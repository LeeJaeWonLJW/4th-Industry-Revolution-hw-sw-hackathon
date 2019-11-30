<template>
  <div class="container-box">
    <v-quagga class="barcode-scanner"
      :onDetected="logIt"
      :readerSize="readerSize"
      :readerType="'ean_reader'"
      :aspectRatio="aspectRatio"
    ></v-quagga>

		<span>바코드를 스캔해 주세요</span>
		<hr/>
		<button>직접 추가</button>
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
	position: fixed;
	width: 100%;
	height: 100%;
}
.barcode-scanner {
	position: fixed;
	z-index: 9;
}
.barcode-scanner span {
	color: #ffffff;
	font-size: 16px;
	text-align: center;

}
.barcode-scanner hr {
	position: fixed;
	width: 60%;	
	top: 50%;
	color: red;
	border: 1px solid red;
	z-index: 19;
}
.barcode-scanner button {
	width: 141px;
  height: 34px;
  border-radius: 20px;
  background-color: #ffffff;
	font-size: 15px;
  font-weight: normal;
  font-stretch: normal;
  font-style: normal;
  line-height: 1.4;
  letter-spacing: normal;
  text-align: center;
  color: #82d09a;
}
</style>