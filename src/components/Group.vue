<template>
  <div class="card group">
    <div class="header">
      <h1 class="card-title card-title-left"> {{group.name}} </h1>
      <hr>
      <br>
      <div class="members">
        <img class="member" src="https://www.ienglishstatus.com/wp-content/uploads/2018/04/Cute-Whatsapp-DP.jpg"></img>
        <img class="member" src="https://www.ienglishstatus.com/wp-content/uploads/2018/04/Anonymous-Whatsapp-profile-picture.jpg"></img>
      </div>
    </div>
    <div class="content">

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
.group i{
  margin-left: 1rem;
  color: #BBB;
  font-size: 1.5rem;
}
.group .member {
  width: 30px;
  height: 30px;
  border-radius: 50%;
  margin-left:-15px;
}
.group .members {
  margin-left: calc(10% + 15px);
}
.group .header {
  width: 100%;
  height: 50%;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  text-align: left;
}
.group .card-title {
  font-size: 1.1rem;
  color: #777;
  font-weight:200;
  margin-left: 10%;
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
.group i {
  margin-right: 0.5rem;
}
.group .content {
  width: 100%;
  height: 30%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.group .footer {
  width: 100%;
  height: 20%;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  display: flex;
  align-items: center;
  background-color: rgb(245,245,245);
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
