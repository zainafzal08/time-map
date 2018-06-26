<template>
  <div class="dashboard-content">
    <div class="row">
      <div class="card availability">
        <div class="card-title card-title-left">Availability</div>
      </div>
      <div class="card events">
        <div class="card-title">Events</div>
        <br>

      </div>
    </div>
    <div class="row">
      <div class="groups">
        <Group v-for="group in groups" :key="group.id" :group="group"></Group>
        <div class="card new-group">
          <span> + </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Group from './Group.vue'

export default {
  name: 'Dashboard',
  components: {Group},
  data () {
    return {
      groups: [
        {
          "name": "Zodiac Killers",
          "id": 1,
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
