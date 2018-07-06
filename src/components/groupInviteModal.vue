<template>
  <div v-show="active" class="content">
    <div class="modal-wrapper card">
      <div class="accent">
        <div class="title-icon"><i class="mdi mdi-link-variant"></i></div>
      </div>
      <div class="modal">
        <div class="row">
          <input id="inviteLink" readonly class="modal-title" type="text" :value="grabData(id)"></input>
          <div class="modal-title-action">
              <a :data-tooltip="msg"><i @click="copyToClipBoard()" class="mdi mdi-content-copy"></i></a>
          </div>
        </div>
      </div>
      <div class="close-btn-wrapper">
        <i @click="close()" class="mdi mdi-close-circle"></i>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'groupInviteModal',
  props: ["grabData","isActive","kill","id"],
  data () {
    return {
      msg: "copy to clipboard"
    }
  },
  computed: {
    active: function(){
      return this.isActive(this.id);
    }
  },
  methods: {
    close: function() {
      this.msg = "copy to clipboard";
      this.kill(this.id);
    },
    copyToClipBoard: function() {
      let copyText = document.getElementById("inviteLink");
      copyText.select();
      document.execCommand("copy");
      this.msg = "copied."
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
 .close-btn-wrapper {
   position: relative;
   width: 1rem;
   height: 1rem;
   font-size: 1rem;
   margin-top: 0.4rem;
   margin-right: 0.4rem;
   color: #BBB;
   cursor: pointer;
 }
 .close-btn-wrapper:hover {
   color: #777;
 }

 .row {
   display: flex;
   align-items: center;
   justify-content: center;
   flex-direction: row;
   width: 90%;
   height: 100%;
   margin-left: 5%;
   margin-right: 5%;
 }
 .title-icon {
   font-size: 2rem;
   color: #FFF;
 }
 .modal-title {
   width: calc(80% + 2rem);
   height: 2.7rem;
   border: none;
   outline: none;
   color: #777;
   font-size: 1.8rem;
   text-align: center;
   background-color: #EEEEEE;
   border-radius: 25px;
   font-family: 'Montserrat', sans-serif;
   overflow: scroll;
   padding-left: 1rem;
   padding-right: 1rem;
 }
 .modal-title-action {
   width: calc(20% - 2rem);
   height: 100%;
   display: flex;
   align-items: center;
   justify-content: flex-end;
   font-size: 1.2rem;
   color: #BBB;
   cursor: pointer;
 }

  .modal-title-action:hover{
    color: #777;
  }
 .group-title:focus {
   outline: none;
 }
 /**
  * Tooltip Styles
  * https://codepen.io/cbracco/pen/qzukg
  */

 /* Add this attribute to the element that needs a tooltip */
 [data-tooltip] {
   position: relative;
   z-index: 2;
   cursor: pointer;
 }

 /* Hide the tooltip content by default */
 [data-tooltip]:before,
 [data-tooltip]:after {
   visibility: hidden;
   -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=0)";
   filter: progid: DXImageTransform.Microsoft.Alpha(Opacity=0);
   opacity: 0;
   pointer-events: none;
 }

 /* Position tooltip above the element */
 [data-tooltip]:before {
   position: absolute;
   bottom: 150%;
   left: 50%;
   margin-bottom: 5px;
   margin-left: -80px;
   padding: 7px;
   width: 160px;
   -webkit-border-radius: 3px;
   -moz-border-radius: 3px;
   border-radius: 3px;
   background-color: #000;
   background-color: hsla(0, 0%, 20%, 0.9);
   color: #fff;
   font-family: 'Montserrat', sans-serif;
   content: attr(data-tooltip);
   text-align: center;
   font-size: 14px;
   line-height: 1.2;
 }

 /* Triangle hack to make tooltip look like a speech bubble */
 [data-tooltip]:after {
   position: absolute;
   bottom: 150%;
   left: 50%;
   margin-left: -5px;
   width: 0;
   border-top: 5px solid #000;
   border-top: 5px solid hsla(0, 0%, 20%, 0.9);
   border-right: 5px solid transparent;
   border-left: 5px solid transparent;
   content: " ";
   font-size: 0;
   line-height: 0;
 }

 /* Show tooltip content on hover */
 [data-tooltip]:hover:before,
 [data-tooltip]:hover:after {
   visibility: visible;
   -ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=100)";
   filter: progid: DXImageTransform.Microsoft.Alpha(Opacity=100);
   opacity: 1;
 }
</style>
