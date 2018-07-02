<template>
  <div class="cal">
    <div class="header"></div>
    <div class="content">
      <div class="row">
        <div class="table-heading"> <span>Mon</span> </div>
        <div class="table-heading"> <span>Tue</span> </div>
        <div class="table-heading"> <span>Wed</span> </div>
        <div class="table-heading"> <span>Thu</span> </div>
        <div class="table-heading"> <span>Fri</span> </div>
        <div class="table-heading"> <span>Sat</span> </div>
        <div class="table-heading"> <span>Sun</span> </div>
      </div>
      <div v-for="i in 5" class="data-row">
          <div v-for="j in 7" class="table-data">
            <div class="cell-wrapper" v-if="validDate(i,j)" >
              <Day :date="getDate(i,j)" :heat="getHeat(i,j)"></Day>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>

import Day from './Day.vue'

export default {
  name: 'Calendar',
  props: ['month','year'],
  data () {
    return {
      'monthStartDay': 4, // 0 = mon 6 = sun
      'daysInMonth': 30,
      'heatData': {
        'may': [
          [1,0.6,1,1,0.5,1,1,0.5,1,1,1,0,0,0,0,1,1,1,0.1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        ]
      }
    }
  },
  components: {Day},
  methods : {
    getDate: function(i,a) {
      return (this.monthStartDay*-1)+(i-1)*7+a;
    },
    validDate: function(i,a) {
      var d = this.getDate(i,a);
      if (d <= 0) return false;
      if (d > this.daysInMonth) return false;
      return true;
    },
    getHeat: function(i,a) {
      var d = this.getDate(i,a);
      return this.heatData[this.month][d-1];
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.cal {
  width: 90%;
  height: 90%;
  margin: 5%;
}
.cal .header {
  width: 100%;
  height: 0%;

}
.cal .content {
  width: 100%;
  height: 100%;
}
.cal .row {
  width: 100%;
  height: 10%;
  margin-bottom: 2%;
  display: flex;
  flex-direction: row;
}
.cal .data-row {
  width: 100%;
  display: flex;
  flex-direction: row;
  height: 17%;
}
.cal hr {
  width: 95%;
  margin-left: 0%;
  margin-bottom: 5%;
}
.cal .table-heading {
  width: calc(100% / 7);
  font-family: 'Comfortaa', cursive;
  color: #00C9FF;
  text-align: center;
}

.cal .table-data {
  width: calc(100% / 7);
  font-family: 'Comfortaa', cursive;
  color: #BBB;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.cal .table-data .cell-wrapper {
    width: 100%;
    height: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
}
</style>
