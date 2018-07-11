<template>
  <div class="day" v-on:mouseover="expand" v-on:mouseleave="collapse">
    <div class="date"> {{date}} </div>
    <svg v-show="visible" class="day-stats" :width="this.statSize+'rem'" :height="this.statSize+'rem'" viewBox="0 0 110 110">
      <g v-for="i in segNum" :transform="'rotate('+(15*(i-1))+' 55 55)'">
        <linearGradient :id="'linearColors'+i+'-'+date">
          <stop offset="0%" :stop-color="getColor(i-2)"></stop>
          <stop offset="100%" :stop-color="getColor(i-1)"></stop>
        </linearGradient>
        <path :fill="getColor(i-1)" :stroke="'url(#linearColors'+i+'-'+date+')'" :stroke-width="statThickness" v-bind:d="path">
        </path>
      </g>
    </svg>
  </div>
</template>

<script>
export default {
  name: 'Day',
  props: ['date','heat','visible'],
  data () {
    return {
      expanded: false,
      statOpacity: 0.7,
      statSize: 3,
      statThickness: 3,
      segNum: 24,
      path: "M 55 5 A 50 50 0 0 1 67.9410 6.7037"
    }
  },
  methods : {
    expand: function(){
      this.expanded = true;
      this.statOpacity = 1;
      this.statSize = 7;
      this.statThickness = 8;
    },
    collapse: function() {
      this.expanded = false;
      this.statOpacity = 0.7;
      this.statSize = 3;
      this.statThickness = 3;
    },
    getColor: function(i) {
      if(i<0) i = 24 + i;
      else i = i % 24;
      var g = ["#00C9FF","#92FE9D"];
      var r;
      if (!this.expanded) r = (this.heat.reduce((a, c) => a + c)/24);
      else r = this.heat[i];
      return this.getGradientColor(r,g);
    },
    normalise: function (a){
    	if(a < 0)
    		return 360+a;
    	if(a>360)
    		return a%360;
    	return a;
    },
    circularInterpol: function (x,y,t){
    	// 191 -> 215
    	if (y >= x && y-x <= 180) {
    		return this.normalise(x+(y-x)*t);
    	} else if (y >= x && y-x > 180) {
    		return this.normalise(x-t*(360-(y-x)));
    	} else if (x > y && x-y <= 180) {
    		return this.normalise(x-t*(x-y));
    	} else if (x > y && x-y > 180) {
    		return this.normalise(x+t*(360-(x-y)));
    	}
    },
    getGradientColor: function (num,gradient) {
    	let start = this.hextoHSV(gradient[0]);
    	let end = this.hextoHSV(gradient[1]);
    	let h = this.circularInterpol(start[0],end[0],num);
    	let s = start[1]+((end[1]-start[1]))*num;
    	let v = start[2]+((end[2]-start[2]))*num;
    	return this.HSVtoHex(h,s,v);
    },
    mod: function (a,n){
        return ((a%n)+n)%n;
    },
    calcHue: function (r,g,b,m,d){
      var res = null;
    	if(d == 0) {
    		res = 0;
    	}else if(m == r){
    		res = 60*(this.mod(((g-b).toFixed(2)/d),6));
    	}else if(m == g){
    		res = 60*(((b-r).toFixed(2)/d)+2);
    	}else if(m == b){
    		res = 60*(((r-g).toFixed(2)/d)+4);
    	}
    	return res;
    },
    calcSat: function (d,m){
    	if(m == 0) {
    		return 0;
    	}else{
    		return d/m;
    	}
    },
    hextoHSV: function (hex){
    	let red = parseInt(hex.substring(1,3),16)/255;
    	let green = parseInt(hex.substring(3,5),16)/255;
    	let blue = parseInt(hex.substring(5,7),16)/255;
    	let cMax = Math.max(red,green,blue);
    	let cMin = Math.min(red,green,blue);
    	let delta = cMax-cMin;
    	let value = cMax;
    	let hue = this.calcHue(red,green,blue,cMax,delta);
    	let sat = this.calcSat(delta, cMax);
    	return [hue,sat,value];
    },
    collapseHue: function (h,c,x){
    	if(h >= 0 && h <60) {
    		return [c,x,0];
    	}else if(h>=60 && h <120){
    		return [x,c,0];
    	}else if(h>=120 && h <180){
    		return [0,c,x];
    	}else if(h>=180 && h <240){
    		return [0,x,c];
    	}else if(h>=240 && h <300){
    		return [x,0,c];
    	}else if(h>=300 && h < 360){
    		return [c,0,x];
    	}
    },
    HSVtoHex: function (h,s,v){
    	let c = v*s;
    	let x = c*(1-Math.abs(((h/60)%2)-1));
    	let m = v-c;
    	let raw = this.collapseHue(h,c,x);
    	let r = Math.floor((raw[0]+m)*255);
    	let g = Math.floor((raw[1]+m)*255);
    	let b = Math.floor((raw[2]+m)*255);
    	return this.rgbToRgba(r,g,b);
    },
    rgbToRgba: function (r, g, b) {
        return `rgba(${r},${g},${b},${this.statOpacity})`;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.day {
  width: 3rem;
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.day .date {
  color: #BBB;
  font-size: 0.8rem;
}
.day .day-stats {
  position: absolute;
}
</style>
