<template>
  <!--使用class来绑定css的样式文件-->
  <div class="hello">
    <!--{{}} 输出对象属性和函数返回值-->
    <h1>{{ msg }}</h1>
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h3>{{details()}}</h3>
    <!-- <h1 v-for="data in ydata" :key="data">{{data}}</h1> -->
    <h3 v-for="item in xdata" :key="item">{{item}}</h3>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Hello',
  // data用来定义返回数据的属性
  data () {
    return {
      msg: 'hello,xxbandy！',
      site: 'bgops',
      url: 'https://xxbandy.github.io',
      xdata: null,
      ydata: null
    }
  },
  // 用于定义js的方法
  methods: {
    details: function () {
      return this.site
    }
  },
  mounted () {
    axios.get('http://localhost:8000/v1/topmv').then(response => { this.xdata = response.data.data })
  }
}
</script>

<!--使用css的class选择器[多重样式的生效优先级]-->
<style>
.hello {
  font-weight: normal;
  text-align:center;
  font-size:8pt;
}
h3
{
  text-align:center;
  font-size:20pt;
  color:red;
}
</style>
