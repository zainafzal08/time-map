<template>
  <div class="card group">
    <div class="header">
      <h1 class="title"> {{group.name}} </h1>
      <hr>
      <div class="group-stats">
        <div><i class="mdi mdi-clock"></i>{{group.stats.upcomingEvents}}</div>
        <div><i class="mdi mdi-chart-line"></i>{{group.stats.totalEvents}}</div>
        <div><i class="mdi mdi-account"></i>{{group.stats.members}}</div>
      </div>
    </div>
    <div v-if="group.members.length < 5" class="content">
      <img v-for="m in group.members" class="member" :src="m.imgSrc"></img>
    </div>
    <div v-else class="content">
      <img v-for="m in group.members.slice(0,4)" class="member" :src="m.imgSrc"></img>
    </div>
    <div class="footer">
      <div class="btns">
        <button class="card-btn btn-red"> Leave </button>
        <button class="card-btn"> Open </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Group',
  props: ['group'],
  data () {
    return {}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.group {
  width: 250px;
  height: 200px;
  margin-right: 2rem;
}

.group .header {
  width: 100%;
  height: 50%;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}
.group .group-stats {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  color: #BBB;
  font-size: 1rem;
  font-family: 'Montserrat', sans-serif;
  width: 80%;
  margin-left: 10%;
  margin-top: 1rem;
}
.group .group-stats i {
  margin-right: 0.5rem;
}
.group .content {
  width: 100%;
  height: 30%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: rgb(245,245,245);
}
.group .content i{
  margin-left: 1rem;
  color: #BBB;
  font-size: 1.5rem;
}
.group .content .member {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  opacity: 0.7;
  margin-left: 0.25rem;
  margin-right: 0.25rem;
  box-shadow: 0 1px 4px rgba(0,0,0,0.16), 0 1px 4px rgba(0,0,0,0.23);
}
.group .footer {
  width: 100%;
  height: 20%;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  display: flex;
  align-items: center;
}

.group .footer .btns {
  width: 90%;
  margin-left: 5%;
  margin-right: 5%;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
