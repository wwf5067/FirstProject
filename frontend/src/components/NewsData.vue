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
    <!-- <el-button
    plain
    @click="open2">
    不会自动关闭
    </el-button> -->
  <el-breadcrumb separator="/">
    <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
    <el-breadcrumb-item><a href="/">每日焦点</a></el-breadcrumb-item>
    <el-breadcrumb-item>一周环顾</el-breadcrumb-item>
    <el-breadcrumb-item>月末回望</el-breadcrumb-item>
</el-breadcrumb>
  <div style="font-size: 24px;colr: red;margin-bottom: 20px"></div>
    <el-table
    :data="xdata"
    border
    style="width: 100%">
    <el-table-column label="热点">
      <template slot-scope="scope">
         <el-link v-if="scope.row.link != ''" v-type="primary" target="_blank" :href="scope.row.link">{{scope.row.title}}</el-link>
        <span v-else >{{scope.row.title}}</span>
      </template>
    </el-table-column>
    <el-table-column label="相关">
      <template slot-scope="scope">
        <el-link v-if="scope.row.s_link != ''" v-type="primary" target="_blank" :href="scope.row.s_link">{{scope.row.s_title}}</el-link>
        <!-- <span v-else >{{scope.row.s_title}}</span> -->
      </template>
    </el-table-column>
    <el-table-column
    label="热度" width="150">
        <template slot-scope="scope">
          <el-rate
          v-model="scope.row.hot"
          :colors="['#99A9BF', '#F7BA2A', '#FF9900']"
          disabled
          score-template="{value}">
          </el-rate>
        </template>
    </el-table-column>
    <el-table-column
      prop="source"
      label="来源"
      width="60">
    </el-table-column>
     <el-table-column
      fixed="right"
      prop="update_time"
      label="日期"
      width="100"
     >
    </el-table-column>
    </el-table>

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
  name: 'News',
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
        pageSize: 30, // 每页多少条
        total: 0 // 总记录数
      },
      pageSizes: [30, 40, 50],
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
      this.xdata = this.getData(this.totalData, this.tablePage.pageNum, this.tablePage.pageSize)
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
    axios.get('http://localhost:8000/v1/news').then(response => { this.totalData = response.data.data; this.tablePage.total = this.totalData.length; this.xdata = this.getData(this.totalData, this.tablePage.pageNum, this.tablePage.pageSize) })
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

