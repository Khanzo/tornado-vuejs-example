<template>
  <div class="col-md-6">
    <b-link :to="{ name: 'home'}">
      Назад
    </b-link>
    <b-link :to="{ name: 'zarplat', params: { id: this.sotrud.id }}" style="float:right">
      Список выплат
    </b-link>
    <b-alert variant="success" show >{{ message }}</b-alert>
    <b-form @submit="onSubmit"  style="margin:10px">
      <b-form-group id="fioGroup"
                    label="Фамилия И.О.:"
                    label-for="fio">
        <b-form-input id="fio"
                      type="text"
                      v-model="sotrud.fio"
                      required
                      placeholder="Введите ФИО">
        </b-form-input>
      </b-form-group>
      <b-form-group id="phoneGroup"
                    label="Телефон:"
                    label-for="phone">
        <b-form-input id="phone"
                      type="text"
                      v-model="sotrud.phone"
                      placeholder="Введите телефон">
        </b-form-input>
      </b-form-group>
      <b-form-group id="datrGroup"
                    label="Дата рождения:"
                    label-for="datr">
      <date-picker v-model="sotrud.datr" :config="options" id="datr"></date-picker>
      </b-form-group>
      <b-form-group id="sexGroup"
                    label="Пол:"
                    label-for="sex">
        <b-form-radio-group id="sex"
                      :options="sex"
                      v-model="sotrud.sex">
        </b-form-radio-group>
      </b-form-group>
      <b-form-group id="otdelGroup"
                    label="Отдел:"
                    label-for="otdel">
        <b-form-select id="otdel"
                      :options="otdel"
                      v-model="sotrud.otdel">
        </b-form-select>
      </b-form-group>
      <b-button type="submit" size="sm" variant="primary" style="float:right">Сохранить</b-button>
      <b-button size="sm" variant="danger" @click="del()">Удалить</b-button>
    </b-form>
  </div>
</template>

<script>
  import axios from 'axios';
  import 'bootstrap/dist/css/bootstrap.css';
  import datePicker from 'vue-bootstrap-datetimepicker';
  import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';

  export default {
    props: ['id'],
    title: `Сотрудник`,
    data() {
      return {
        date: new Date(),
        options: {
          format: 'DD-MM-YYYY',
          useCurrent: false,
          locale:'ru',
        },
      sex: [
        'муж.', 'жен.'
      ],
      otdel: [
        'Склад', 'Бухгалтерия','IT'
      ],
        sotrud:Object(),
        message:''
      }
    },
    components: {
      datePicker
    },
    methods: {
      onSubmit (evt) {
      //send PUT info sotrudnik
      evt.preventDefault();
      const path = 'http://localhost:5000/api/info/' + this.sotrud.id;
      if (this.sotrud.sex == "муж.") {this.sotrud.sexy = "0";} else{this.sotrud.sexy = "1";}
      var vm = this
      vm.message = "";
      axios.put(path,
        {
            fio: this.sotrud.fio,
            datr: this.sotrud.datr,
            phone: this.sotrud.phone,
            sex: this.sotrud.sexy,
            otdel: this.sotrud.otdel,
        }
      )
        .then(function (response) {
          console.log(response);
          vm.message = "Сохранено";
        })
        .catch(function (error) {
          console.log('-----error-------');
          console.log(error);
        });
      },

      del(){
        //swnd DELETE sotrudnik
        const path = 'http://localhost:5000/api/info/' + this.sotrud.id;
        var vm = this
        axios.delete( path )
            .then(function (response) {
                vm.$router.push({path: '/' });
            })
            .catch(function (error) {
              console.log('-----error-------');
              console.log(error);
            });

      },
      getSotrud(id) {
        //init sotrudnik
        const path = 'http://localhost:5000/api/info/' + id
        axios(path)
          .then(response => {
            var info = response.data[0];
            this.sotrud = info;
            this.sotrud.sexy = info.sex;
            if (info.sex >0){this.sotrud.sex = 'жен.';}else{this.sotrud.sex = 'муж.';}
            this.sotrud.id = info.id;
            this.sotrud.fio = info.fio.fio;
            this.sotrud.otdel = info.otdel;
            document.title = `Сотрудник - ` + this.sotrud.fio;
            message = "";
          })
          .catch( error => {
            console.log('-----error-------');
            console.log(error)
          })
      }
    },

    created() {
      this.getSotrud(this.id);
    },
    watch: {
      '$route'() {
        this.getSotrud(this.id);
      }
    }
  }
</script>
