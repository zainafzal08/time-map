<template>
  <div class="event">
    <div class="accent"></div>
    <div class="details"></div>
  </div>
</template>

<script>
export default {
  name: 'Event',
  props: ['event'],
  data () {
    return {}
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.event{
  width: 100%;
  height: 1rem;
}
.accent {
    border-top-left-radius: 15px;
    border-bottom-left-radius: 15px;
    background-color: #00C9FF;
    width: 20%;
    height: 100%;
}
.details {
    border-top-right-radius: 15px;
    border-bottom-right-radius: 15px;
    width: 80%;
    height: 100%;
}
</style>
