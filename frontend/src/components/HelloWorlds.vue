<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Essential Links</h2>
    <ul>
      <!-- <li>
        <a
          href="https://vuejs.org"
          target="_blank"
        >
          Core Docs
        </a>
      </li>
      <li>
        <a
          href="https://forum.vuejs.org"
          target="_blank"
        >
          Forum
        </a>
      </li>
      <li>
        <a
          href="https://chat.vuejs.org"
          target="_blank"
        >
          Community Chat
        </a>
      </li>
      <li>
        <a
          href="https://twitter.com/vuejs"
          target="_blank"
        >
          Twitter
        </a>
      </li>
      <br> -->
      <li>
        <a
          href="/#/news"
          target="_blank"
        >
          每日新闻
        </a>
      </li>
    </ul>
    <!-- <h2>Ecosystem</h2> -->
    <ul>
      <!-- <li>
        <a
          href="http://router.vuejs.org/"
          target="_blank"
        >
          vue-router
        </a>
      </li>
      <li>
        <a
          href="http://vuex.vuejs.org/"
          target="_blank"
        >
          vuex
        </a>
      </li>
      <li>
        <a
          href="http://vue-loader.vuejs.org/"
          target="_blank"
        >
          vue-loader
        </a>
      </li> -->
      <!-- <li>
        <a
          href=""
          target="_blank"
        >
        test
        </a>
      </li> -->
      <!-- <el-tag>一</el-tag>
      <el-tag type="success">起</el-tag>
      <el-tag type="info">来</el-tag>
      <el-tag type="warning">玩</el-tag>
      <el-tag type="danger">吧</el-tag> -->
  <el-row>
    <el-col>
    <el-card shadow="always">
      <i class="el-icon-time">更多功能未open</i>
    </el-card>
   </el-col>
  </el-row>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to have fun'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
