<template>
  <div class="dashboard-content">
    <div class="row">
      <div class="card availability">
        <div class="card-title card-title-left">Availability</div>
      </div>
      <div class="card events">
        <div class="card-title">Events</div>
      </div>
    </div>
    <div class="row">
      <div class="groups">
        <div v-for="group in groups" class="card group">
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

        <div class="card new-group">
          <span> + </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data () {
    return {
      groups: [
        {
          "name": "Zodiac Killers",
          "members": [
            {"imgSrc":"http://s3.amazonaws.com/projects-assets/ted/images/ted-cruz.jpg"},
            {"imgSrc":"http://lanetadurango.com/wp-content/uploads/2016/05/08-ted-cruz.w529.h529.jpg"},
            {"imgSrc":"http://brewminate.com/wp-content/uploads/2016/03/Cruz06.jpg"},
            {"imgSrc":"http://brewminate.com/wp-content/uploads/2016/03/Cruz06.jpg"},
            {"imgSrc":"http://brewminate.com/wp-content/uploads/2016/03/Cruz06.jpg"}
          ],
          "stats": {
            "upcomingEvents": 3,
            "totalEvents": 6,
            "members": 3
          }
        }
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
/*
 * Written by Zain Afzal
 * 21/6/2018
 * Box shadow from https://codepen.io/sdthornton/pen/wBZdXq
 */

 .dashboard-content {
   display: flex;
   flex-direction: column;
   width: 100vw;
 }
.dashboard-content .row {
  display: flex;
  width: 100%;
  flex-direction: row;
  flex-wrap: wrap;
}

.availability {
  width: 66%;
  height: 70vh;
  margin: 2%;
}

.events {
  width: 26%;
  height: 70vh;
  margin: 2%;
}

.seperator {
  width: 96%;
  margin: 2%;
}

.groups {
  width: 96%;
  margin: 2%;
  display: flex;
  flex-direction: row;
}

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
  opacity: 0.8;
  margin-left: 0.25rem;
  margin-right: 0.25rem;
  border: 2px solid #BBB;
}
.group .footer {
  background-color: rgb(245,245,245);
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

.new-group {
  width: 250px;
  height: 200px;
  background-color: rgba(255,255,255,0.3);
  box-shadow: none;
  font-family: 'Comfortaa', cursive;
  color: rgba(255,255,255,0.4);
  font-size: 6rem;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: box-shadow 0.2s ease-in-out;
}
.new-group:hover {
  box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
}
</style>
