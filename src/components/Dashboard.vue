<template>
  <div>
    <groupInviteModal :grabData="modalData" :isActive="modalActive" :kill="hideModal" id="groupInviteLink"></groupInviteModal>
    <newGroupModal :grabData="modalData" :isActive="modalActive" :kill="hideModal" id="newGroup"></newGroupModal>
    <div class="dashboard-content">
      <div class="row">
        <div class="card availability">
          <Calendar month="may" year="2018"></Calendar>
        </div>
        <div class="card events">
          <div class="card-title">Events</div>
          <br><hr><br>
          <div class="events-content">
            <Event v-for="e in events"  :key="e.id" :event="e"></Event>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="groups">
          <Group v-for="group in groups" :key="group.id" :group="group" :showModal="showModal"></Group>
          <div class="card new-group" @click="showModal('newGroup')">
            <span> + </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Group from './Group.vue'
import Calendar from './Calendar.vue'
import newGroupModal from './newGroupModal.vue'
import groupInviteModal from './groupInviteModal.vue'
import Event from './Event.vue'

export default {
  name: 'Dashboard',
  components: {Group,Calendar,newGroupModal,groupInviteModal,Event},
  data () {
    return {
      modals: {
        newGroup: {
          active: false,
          data: null
        },
        groupInviteLink: {
          active: false,
          data: null
        }
      },
      groups: [
        {
          "name": "Zodiac Killers",
          "id": 1,
          "members": [
            {"imgSrc":"/static/imgs/cruz.jpg"},
            {"imgSrc":"/static/imgs/cruz.jpg"},
            {"imgSrc":"/static/imgs/cruz.jpg"},
            {"imgSrc":"/static/imgs/cruz.jpg"},
            {"imgSrc":"/static/imgs/cruz.jpg"}
          ],
          "stats": {
            "upcomingEvents": 3,
            "totalEvents": 6,
            "members": 3
          },
          "inviteLink": "www.lolfuckyou.com"
        }
      ],
      events: [
        {id: 1}
      ]
    }
  },
  methods: {
    showModal: function(m,d){
      document.body.style.overflow = 'hidden';
      this.modals[m].active = true;
      this.modals[m].data = d;
    },
    hideModal: function(m){
      document.body.style.overflow = 'scroll';
      this.modals[m].active = false;
    },
    modalActive: function(m){
      return this.modals[m].active;
    },
    modalData: function(m){
      return this.modals[m].data;
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
.events-content {
  display: flex;
  align-items: flex-start;
  justify-content: center;
  flex-direction: column;
  width: 80%;
  padding-left: 10%;
  padding-right: 10%
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
