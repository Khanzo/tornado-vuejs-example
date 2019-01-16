
<template>
  <div class="col-md-12">
    <p>Случайное число с сервера: {{ randomNumber }}</p>
    <b-button size="sm" variant="primary" @click="getRandom">Получить новое</b-button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  title: `Случайное число`,
  data () {
    return {
      randomNumber: 0
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
      .then(response => {
        this.randomNumber = response.data.randomNumber
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
  created () {
    document.title = `Случайное число`;
    this.getRandom()
  }
}
</script>
