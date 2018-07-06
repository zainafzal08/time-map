<template>
  <div v-show="active" class="content">
    <div class="modal-wrapper card">
      <div class="accent">
        <div class="group-title-icon"><i class="mdi mdi-account-multiple"></i></div>
      </div>
      <div class="modal">
        <div class="row">
          <input maxlength="18" class="group-title" type="text" value="my awesome group"></input>
        </div>
        <div class="btns">
          <button @click="close()" class="card-btn btn-red"> Cancel </button>
          <button @click="close()" class="card-btn"> Make </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'newGroupModal',
  props: ["isActive","kill","id"],
  data () {
    return {}
  },
  computed: {
    active: function(){
      return this.isActive(this.id);
    }
  },
  methods: {
    close: function() {
      this.kill(this.id);
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

 .content {
   position: fixed;
   z-index: 9998;
   top: 0;
   left: 0;
   display: flex;
   justify-content: center;
   align-items: center;
   width: 100vw;
   height: 100vh;
   background-color: rgba(0,0,0,0.6);
 }

.modal-wrapper {
  width: 500px;
  height: 7rem;
  display: flex;
  flex-direction: row;
}
.accent {
  width: 15%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #00C9FF;
  border-top-left-radius: 15px;
  border-bottom-left-radius: 15px;
}
 .modal {
   width: 85%;
   height: 100%;
   display: flex;
   justify-content: center;
   align-items: center;
   flex-direction: column;
 }
 .btns {
   width: 90%;
   height: 13%;
   margin-left: 5%;
   margin-right: 5%;
   margin-bottom: 2%;
   display: flex;
   justify-content: space-around;
   align-items: center;
 }

 .row {
   display: flex;
   align-items: center;
   justify-content: center;
   flex-direction: row;
   width: 90%;
   height: 85%;
   margin-left: 5%;
   margin-right: 5%;
 }
 .group-title-icon {
   font-size: 2rem;
   color: #FFF;
 }
 .group-title {
   width: 85%;
   height: 2.7rem;
   border: none;
   outline: none;
   color: #777;
   font-size: 2rem;
   text-align: center;
   background-color: #EEEEEE;
   border-radius: 25px;
   margin-bottom: 1rem;

 }

 .group-title:focus {
   outline: none;
 }
</style>
