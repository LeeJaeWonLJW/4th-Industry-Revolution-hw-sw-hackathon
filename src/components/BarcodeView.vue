<template>
  <div>
    <v-quagga
      :onDetected="logIt"
      :readerSize="readerSize"
      :readerType="'ean_reader'"
      :aspectRatio="aspectRatio"
    ></v-quagga>
  </div>
</template>

<script>
export default {
	name: 'VueBarcodeTest',
	data () {
		return {
			readerSize: {
				width: 640,
				height: 560
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
