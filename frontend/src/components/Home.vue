<template>
  <div class="col-md-12">
    <h3>Сотрудники</h3>
    <button @click="add" class="btn btn-primary btn-sm" style="margin-bottom:10px">Добавить</button>
    <b-table hover :items="all" :fields="fields" class="col-md-6 sotrud">
      <template slot="actions" slot-scope="row">
        <b-button size="sm" variant="info" @click="zp(row.item, row.index, $event.target)" class="mr-2">
         Зарплата
        </b-button>
      </template>
      <template slot="fio" slot-scope="data">
      <b-link :to="{ name: 'sotrud', params: { id: data.value.id }}">
        {{data.value.fio}}
      </b-link>
    </template>
    </b-table>
    <!-- Info modal -->
        <b-modal id="modalZp" ref="modalZp" :title="modalZp.title" ok-only @ok="handleOk">
          <form @submit.stop.prevent="handleOk">
            <b-form-input type="text"
                      placeholder="Сумма"
                      v-model="summ" value="0"></b-form-input>
            </form>
        </b-modal>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  title: `Сотрудники`,
  data () {
      return {
        fields: [
        {
          key: 'id',
          label: 'id',
          sortable: false
        },
        {
          key: 'fio',
          label: 'Фамилия И.О.',
          sortable: true
        },
        {
          key: 'datr',
          label: 'Дата рождения',
          sortable: true
        },
        {
          key: 'phone',
          label: 'Телефон',
          sortable: true
        },
        {
          key: 'sex',
          label: 'Пол',
          sortable: true,
          formatter: (value) => { if (value == 0){ return "муж." }else{ return "жен." } }
        },
        {
          key: 'otdel',
          label: 'Отдел',
          sortable: true
        },
        {
          key: 'actions',
          label: 'Действия',
          sortable: false
        },
      ],
      modalZp: { title: '', content: '', id: 0 },
      all: [],
      summ:0,
      sotrud:0,
      endpoint: 'http://localhost:5000/api/all',
      }
    },
    created() {
      this.getAll();
    },
    methods: {
            getAll() {
              //all sotrudniki
              axios.get(this.endpoint)
                .then(response => {
                  console.log(response.data);
                  this.all = response.data;
                })
                .catch(error => {
                  console.log('-----error-------');
                  console.log(error);
                })
            },
            add () {
              //new sotrud
              this.$router.push({path: '/add' });
            },
            handleOk (evt) {
              //modal input zarplata
              evt.preventDefault()
              if (this.summ == 0 || this.summ.match(/^-?\d*(\.\d+)?$/) == null || this.summ < 0) {
                alert('Введите Сумму > 0')
              } else {
                this.handleSubmit()
              }
            },
            handleSubmit () {
              //POST summ zarplata sotrudnika
              const path = 'http://localhost:5000/api/zarplata';
              var vm = this
              axios.post(path,
                {
                    sotrud:  vm.sotrud,
                    sumz:  vm.summ
                }
              )
                .then(function (response) {
                  console.log(response);
                })
                .catch(function (error) {
                  console.log('-----error-------');
                  console.log(error);
                });
              this.$refs.modalZp.hide();
            },
            zp (item, index, button) {
              //init modal
              this.modalZp.title = `Зарплата для: ${item.fio.fio}`;
              this.modalZp.id = item.id;
              this.sotrud = item.id;
              this.$root.$emit('bv::show::modal', 'modalZp', button);
            },
          },
}

</script>

<style>

</style>
