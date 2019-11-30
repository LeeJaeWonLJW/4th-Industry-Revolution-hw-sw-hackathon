<template>
  <div class="container-box">
    <v-quagga class="barcode-scanner"
      :onDetected="logIt"
      :readerSize="readerSize"
      :readerType="'ean_reader'"
      :aspectRatio="aspectRatio"
    ></v-quagga>

		<!-- <span>바코드를 스캔해 주세요</span>
		<hr/>
		<button></button> -->
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
	background-color: #d5d5d5;
}
.barcode-scanner {
	display: inline-block;
	position: absolute;
	position: fixed;
}
/* .barcode-scanner hr {
	display: inline;
	position: fixed;
	width: 60%;
	top: 50%;
	border: 1px solid red;
} */
</style>