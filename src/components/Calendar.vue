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
            <div v-if="validDate(i,j)">
              <div class="date">{{getDate(i,j)}}<i v-if="eventOn(i,j)" class="mdi mdi-checkbox-blank-circle event-tag"></i></div>
            </div>
          </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Calendar',
  props: ['month','year'],
  data () {
    return {
      'monthStartDay': 4, // 0 = mon 6 = sun
      'daysInMonth': 30,
      'eventData': {
        'may': [null,null,null,null,null]
      }
    }
  },
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
    eventOn: function(i,a) {
      if (this.eventData[this.month][0]) return true;
      return false;
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
  margin-bottom: 5%;
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
  text-align: left;
}
.cal .table-heading span {
  margin-left:1rem;
}
.cal .table-data {
  width: calc(100% / 7);
  font-family: 'Comfortaa', cursive;
  color: #BBB;
  height: 100%;
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
}
.cal .table-data .date {
  width: 10%;
  margin-left: 1rem;
  height: 100%;
  font-size: 0.6rem;
  display: flex;
  align-items: flex-start;
  justify-content: flex-start;
}
.cal .event-tag {
  margin-left: 0.3rem;
  color: #e44232;
}
</style>
