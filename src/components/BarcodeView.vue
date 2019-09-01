<template>
  <div>
    <v-quagga :onDetected="logIt" :readerSize="readerSize" :readerTypes="['ean_reader']"></v-quagga>
  </div>
</template>

<script>
export default {
  name: "barcode-view",
  data: () => ({
    readerSize: {
      width: 100,
      height: 400
    },
    detecteds: []
  }),
  methods: {
    logIt(data) {
      //   window.console.log(JSON.stringify(data));
      this.$router.push("/tab/barcode");
    }
  }
};
</script>

<style scoped>
</style>