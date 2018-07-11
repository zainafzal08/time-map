<template>
  <div class="cal">
    <div class="header">
      <i @click="shiftBackward()" class="mdi mdi-chevron-double-left"></i>
      <h1 class="heading"> {{this.year}} {{this.month}} </h1>
      <i @click="shiftForward()" class="mdi mdi-chevron-double-right"></i>
    </div>
    <div class="seperator"></div>
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
      <div v-for="i in 6" class="data-row">
          <div v-for="j in 7" class="table-data">
            <div @mouseover="focus(i,j)" @mouseleave="unfocus()" class="cell-wrapper" v-if="validDate(i,j)" >
              <Day :visible="isVisible(i,j)" :date="getDate(i,j)" :heat="getHeat(i,j)"></Day>
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
  props: ['events'],
  data () {
    return {
      'time': null,
      'focused': null,
      'heatData': {
        'july': [
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
        ],
        'june': [
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
      let cpy = new Date(this.time.getTime());
      cpy.setDate(1);
      let sd = (cpy.getDay()+6)%7;
      return (sd*-1)+(i-1)*7+a;
    },
    focus: function(i,a) {
      this.focused = this.getDate(i,a);
    },
    unfocus: function(i,a){
      this.focused = null;
    },
    isVisible: function(i,a) {
      var d = this.getDate(i,a);
      if (this.focused === d) return true;
      if (this.focused === null) return true;
      return false;
    },
    validDate: function(i,a) {
      var d = this.getDate(i,a);
      let daysInMonth = 30;
      if (d <= 0) return false;
      if (d > daysInMonth) return false;
      return true;
    },
    shiftForward: function(i,a) {
      let newTime = new Date(this.time.getTime());
      var d = this.time.getDate();
      newTime.setMonth(this.time.getMonth() + 1);
      if (newTime.getDate() != d) {
        newTime.setDate(0);
      }
      this.time = newTime;
    },
    shiftBackward: function(i,a) {
      let newTime = new Date(this.time.getTime());
      newTime.setMonth(this.time.getMonth() - 1);
      this.time = newTime;
    },
    capitalise: function(s){
      return s.charAt(0).toUpperCase() + s.substr(1);
    },
    getMonthName: function(d){
      const monthNames = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"];
      return monthNames[d];
    },
    getHeat: function(i,a) {
      var d = this.getDate(i,a);
      try{
        return this.heatData[this.getMonthName(this.time.getMonth())][d-1];
      }catch(e){
        return Array.from(Array(24)).map((arg, index) => 0);
      }
    }
  },
  computed: {
    month: function() {
      return this.getMonthName(this.time.getMonth());
    },
    year: function(){
      return this.time.getFullYear();
    }
  },
  created: function(){
    this.time = new Date();
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.heading {
  margin: 0%;
  font-family: 'Montserrat', sans-serif;
  font-size: 1.3rem;
  text-transform: capitalize;
  color: rgba(228, 66, 50,0.8);
  width: 60%;
}
.cal {
  width: 100%;
  height: 100%;
}
.cal .header {
  width: 90%;
  padding-left: 5%;
  padding-right: 5%;
  height: 15%;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: row;
  background-color: #EEE;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}
.cal i {
  margin-top: 0.2rem;
  color: #777;
  font-size: 1.5rem;
  cursor: pointer;
}
.cal i:hover {
  color: rgba(228, 66, 50,0.8);
}
.cal .content {
  width: 90%;
  height: 75%;
  margin: 5%;
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
  height: 14%;
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
