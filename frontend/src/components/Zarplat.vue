<template>
  <div class="col-md-12">
    <h3>Зарплаты</h3>
    <b-link :to="{ name: 'sotrud',params: { id: this.id }}">
      Назад
    </b-link>
    <b-table hover :items="all" :fields="fields" class="col-md-6">
    </b-table>
  </div>
</template>
<script>
  import axios from 'axios';
  export default {
    props: ['id'],
    title: `Зарплаты`,
    data(){
    return {
    all: [],
    fields: [
      {
        key: 'datz',
        label: 'Дата выплаты',
        sortable: true
      },
    {
      key: 'fio',
      label: 'Фамилия И.О.',
      sortable: false
    },

    {
      key: 'sumz',
      label: 'Сумма',
      sortable: true
    }

  ],}
    },
    methods: {
      getZarplati(id) {
        //GET list zarplat
        const path = 'http://localhost:5000/api/zarplata/' + id
        axios(path)
          .then(response => {
            this.all = response.data;
          })
          .catch( error => {
            console.log('-----error-------');
            console.log(error)
          })
      }
    },
    created() {
      this.getZarplati(this.id);
    },
    watch: {
      '$route'() {
        this.getZarplati(this.id);
      }
    }
  }
</script>
