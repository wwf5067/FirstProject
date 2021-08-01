<template>
  <!--使用class来绑定css的样式文件-->
  <!-- <div class="hello"> -->
    <!--{{}} 输出对象属性和函数返回值-->
    <!-- <h1>{{ msg }}</h1>
    <h1>site : {{site}}</h1>
    <h1>url : {{url}}</h1>
    <h3>{{details()}}</h3>
    <h1 v-for="data in ydata" :key="data">{{data}}</h1>
    <h3 v-for="item in xdata" :key="item">{{item}}</h3>
  </div> -->
<div>
    <el-breadcrumb separator="/">
    <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
    <el-breadcrumb-item><a href="/">每日焦点</a></el-breadcrumb-item>
    <el-breadcrumb-item>一周环顾</el-breadcrumb-item>
    <el-breadcrumb-item>月末回望</el-breadcrumb-item>
    </el-breadcrumb>
    <el-row>
  <el-col :span="8" v-for="(o, index) in xdata" :key="index">
    <el-card :body-style="{ padding: '3px' }">
      <img src="../assets/p480747492.jpg" />
      <div style="padding: 14px;">
        <span>{{o.title}}</span>
        <div class="bottom clearfix">
          <time class="time">{{ currentDate }}</time>
        </div>
      </div>
    </el-card>
  </el-col>
</el-row>

    <!-- <ul> -->
          <!-- <h3 v-for="item in xdata" :key="item.id">{{item.title}}</h3> -->
       <!-- <li v-for="item in xdata" :key="item.id">
        <div>
          <span style="width: 80px;"><a :href="item.link" target="_blank">{{item.title}}</a></span>
          <span style="margin-left: 20px">{{item.creation_time}}</span>
          <span style="margin-left: 20px">{{item.source}}</span>
        </div> -->
        <!-- <div style="color: red">{{item}}</div> -->
      <!-- </li>
    </ul> -->
  <div class="pagination">
    <el-pagination
      background
      layout="total, sizes, prev, pager, next, jumper"
      :current-page.sync="tablePage.pageNum"
      :page-size="tablePage.pageSize"
      :page-sizes="pageSizes"
      :total="tablePage.total"
      @size-change="handleSizeChange"
      @current-change="handlePageChange"
    />
  </div>
</div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Topmv',
  // data用来定义返回数据的属性
  data () {
    return {
      // msg: 'hello,xxbandy！',
      // site: 'bgops',
      // url: 'https://xxbandy.github.io',
      // xdata: null,
      // ydata: null
      tablePage: {
        pageNum: 1, // 第几页
        pageSize: 10, // 每页多少条
        total: 0 // 总记录数
      },
      pageSizes: [10, 20, 30],
      xdata: null,
      totalData: null
    }
  },
  // 用于定义js的方法
  methods: {
    // details: function () {
    //   return this.site
    // }
    // open2 () {
    //     this.$notify({
    //       title: '提示',
    //       message: '这是一条不会自动关闭的消息',
    //       duration: 0
    //     });
    //   },
    handlePageChange (currentPage) {
      this.tablePage.pageNum = currentPage
      // 在此刷新数据
      this.xdata = this.getList(this.totalData, this.tablePage.pageNum, this.tablePage.pageSize)
    },
    handleSizeChange (pageSize) {
      this.tablePage.pageSize = pageSize
      // 在此刷新数据
      this.xdata = this.getData(this.totalData, this.tablePage.pageNum, this.tablePage.pageSize)
    },
    /**
     * 分页数据处理
     * @param data [Array] 需要分页的数据
     * @param num [Number] 当前第几页
     * @param size [Number] 每页显示多少条
     */
    getList: function getList (data, num, size) {
      let list, total, start, end, isFirst, isLast

      total = data.length
      isFirst = total < size
      isLast = Math.ceil(total / size) === num
      start = (num - 1) * size
      end = isFirst || isLast ? start + (total % size) : start + size
      list = data.slice(start, end)
      // list.forEach((item, index) => {
      //   item.seq = index + start
      // })
      return list
    },
    getData: function getData (data, num, size) {
      let list, start, end
      start = (num - 1) * size
      end = start + size
      list = data.filter((item, index) => {
        return index >= start && index < end
      })

      return list
    }
  },
  mounted () {
    axios.get('http://localhost:8000/v1/topmv').then(response => { this.totalData = response.data.data; this.tablePage.total = this.totalData.length; this.xdata = this.getData(this.totalData, this.tablePage.pageNum, this.tablePage.pageSize) })
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

  #box {
    padding: 20px;
  }

  ul {
    padding: 0px;
    list-style-type: none;
  }

  li {
    margin-top: 5px;
    color: red;
    font-size: 20px;
    border-bottom: 1px white dashed;
  }

  .pageView {
    height: 30px;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
  }
 </style>
