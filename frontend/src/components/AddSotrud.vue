<template>
  <div class="col-md-6">
    <b-link :to="{ name: 'home'}">
      Назад
    </b-link>
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
    </b-form>
  </div>
</template>

<script>
import 'bootstrap/dist/css/bootstrap.css';
import datePicker from 'vue-bootstrap-datetimepicker';
import 'pc-bootstrap4-datetimepicker/build/css/bootstrap-datetimepicker.css';

  import axios from 'axios';
  export default {
    props: ['id'],
    title: `Сотрудник`,
    data() {
      return {
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
        sotrud:Object()
      }
    },
    components: {
      datePicker
    },
    methods: {
      onSubmit (evt) {
      //POST new sotrudnik
      evt.preventDefault();
      const path = 'http://localhost:5000/api/info';
      if (this.sotrud.sex == "муж.") {this.sotrud.sexy = "0";} else{this.sotrud.sexy = "1";}
      var vm = this;
      axios.post(path,
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
          vm.$router.push({path: '/' });
        })
        .catch(function (error) {
          console.log('-----error-------');
          console.log(error);
        });
      },
      getSotrud() {
        //init sotrudnik
        let dat = new Date();
        let str_dat = dat.getDate() + "-0" + (dat.getMonth()+1) + "-" + dat.getFullYear();
        if ((dat.getMonth()+1)>9){
          str_dat = dat.getDate() + "-" + (dat.getMonth()+1) + "-" + dat.getFullYear();
        }
        this.sotrud.fio = "";
        this.sotrud.datr = str_dat;
        this.sotrud.phone = "";
        this.sotrud.sexy = 1;
        this.sotrud.sex = "муж.";
        this.sotrud.otdel = "IT";
        document.title = `Сотрудник - новый`;
      }
  },
  created() {
    this.getSotrud();
  },
  watch: {
    '$route'() {
      this.getSotrud();
    }
  }
}
</script>
