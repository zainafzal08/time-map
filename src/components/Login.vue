<template>
  <div class="content">
    <div class="card card-auto-adjust">
      <div class="section top">
        <h1 class="brand"> Time Map </h1>
        <h2 class="subtitle"> Make Plans With Your Impossible To Plan Around Friends</h2>
      </div>
      <div class="section bottom">
        <div class="info">
          <h3 class="title"> <i class="mdi mdi-clock"></i> Make Groups </h3>
          <h3 class="title"> <i class="mdi mdi-calendar-check"></i> See Availability </h3>
          <h3 class="title"> <i class="mdi mdi-format-list-bulleted"></i> List Options </h3>
        </div>
        <br><br>
        <div class="action-container">
          <button class="facebook btn"><i class="mdi mdi-facebook"></i>Sign in With Facebook</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
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
   display: flex;
   justify-content: center;
   align-items: center;
   width: 100vw;
   height: 100vh;
 }

i {
  color: white;
  margin-right: 1rem;
}
.info i{
  color: #777;
  margin-right: 1rem;
}

.card .section.top {
  height: 30%;
}
.card .section.bottom {
  height: 60%;
  margin-top: 10%;
}

.card-auto-adjust {
  width: 400px;
  height: 450px;
}

.info {
  width: calc(100%-2rem);
  text-align: left;
  background-color: #EBEBEB;
  padding-top: 1rem;
  padding-bottom: 1rem;
  padding-left: 2rem;
}
.action-container {

}

.action-container .facebook {
  width: 60%;
  background-color: rgb(66, 103, 178,1);
}

</style>
