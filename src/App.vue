<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
body {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin: 0;
  padding: 0;
}

#app {
  position: relative;
  width: 100vw;
  max-width: 640px;

  margin: 0;
  /* padding: 16px; */
  
  text-align: center;
  color: #2c3e50;

  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  box-shadow: 0 4px 4px rgba(0, 23, 80, 0.02),
    0 1px 6px rgba(0, 23, 80, 0.03),
    0 8px 8px rgba(0, 23, 80, 0.024),
    0 16px 16px rgba(0, 23, 80, 0.024),
    8px 32px 32px rgba(0, 23, 80, 0.036),
    8px 64px 64px rgba(0, 23, 80, 0.036);
}
</style>
