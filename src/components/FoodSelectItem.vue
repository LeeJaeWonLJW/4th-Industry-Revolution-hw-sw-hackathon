<template>
  <div
    :class="{'active': this.active }"
    @click="check()"
    class="col-6-sm item"
  >
    <img :src="this.image" />
    <div class="checkbox">
      <img src="../assets/icon/check_btn.png" />
    </div>
    <span class="text">{{this.food}}</span>
  </div>
</template>

<script>
export default {
  name: 'select-box-item',
  data: () => ({
    active: false
  }),
  props: {
    label: {
      type: Number
    },
    food: {
      type: String
    },
    image: {
      type: String
    }
  },
  methods: {
    check: async function() {
			let foodData = await window.localStorage.getItem('foodData')
			let array = foodData != 'undefined' ? JSON.parse(foodData) : []
			let check = this.find(array, this.food)

			if(!this.active) {
				if(check) await array.push(this.food)
				
				await this.$emit('send-add')
				this.active = true
			} else {
				if(check) await array.splice(array.indexOf(label), 1)
				
				await this.$emit('send-remove')
				this.active = false
			}
			
			await window.localStorage.setItem('foodData', JSON.stringify(array))
    },
    find: function(data, label) {
      let count = 0
      for (let i = 0; i < Object.keys(data).length; i++) {
        if (data[i] === label) {
          count++
        }
      }

      if (count !== 0) {
        return false
      }
      return true
    },
    findAll: async function(label) {
      let foodData = window.localStorage.getItem('foodData')
      let count = 0

      if (foodData !== null) {
        foodData = JSON.parse(foodData)
        for (let i = 0; i < Object.keys(foodData).length; i++) {
          if (foodData[i] === label) {
            count++
          }
        }
      }

      if (count === 1) {
        return true
      }

      return false
    }
  }
}
</script>

<style scoped>
.item {
  position: relative;
  display: inline-block;

  /* padding: 13px 8px; */

  opacity: 1;
  cursor: pointer;

  transition: 0.5s ease;
}
.item > img {
  position: relative;
  width: 100%;
  border-radius: 4px;
  transition: 0.5s ease-out;
}
.item .checkbox {
  opacity: 0;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  -ms-transform: translate(-50%, -50%);
  text-align: center;
  transition: 0.5s ease-out;
}
.item .checkbox img {
  width: 100%;
}

.item:hover .text {
  color: #91ffb3;
}
.item:hover > img,
.item.active > img {
  opacity: 0.4;
}
.item:hover .checkbox,
.item.active .checkbox {
  opacity: 1;
}

.item .text {
  position: relative;
  margin-left: auto;
  margin-right: auto;
  left: 0;
  right: 0;
  font-size: 12px;
  color: #909090;
  border-bottom: 1px solid #91ffb3;
  padding: 6px 0;
  transition: 0.5s ease-out;
}
</style>
