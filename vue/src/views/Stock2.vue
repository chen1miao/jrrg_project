<template>
  <el-container style="height: 800px; border: 1px solid #eee">
<el-aside width="200px" style="background-color: rgb(238, 241, 246)">
  <el-menu router :default-openeds="['1','2','3']" :default-active="this.$router.path">
    <el-submenu index="1">
      <template slot="title"><i class="el-icon-message"></i>个人信息</template>
      <el-menu-item-group>
        <el-menu-item index="/changepassword">修改密码</el-menu-item>
        <el-menu-item index="/property">当前资产</el-menu-item>
     
      </el-menu-item-group>
      
    </el-submenu>
    <el-submenu index="2">
      <template slot="title"><i class="el-icon-menu"></i>市场数据</template>
      <el-menu-item-group>
        <el-menu-item index="/today">今日大盘</el-menu-item>
        <el-menu-item index="/stock1">上交所</el-menu-item>
        <el-menu-item index="/stock2"  class="current-page" >深交所</el-menu-item>
      </el-menu-item-group>
        
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-setting"></i>量化交易</template>
        
        <el-menu-item index="/trade1">买入股票</el-menu-item>
        <el-menu-item index="/trade2">卖出股票</el-menu-item>
        
        <el-submenu index="3-2">
          <template slot="title">交易策略</template>
          <el-menu-item index="/strategy1">双均线策略</el-menu-item>
          <el-menu-item index="/strategy2">均值回归交易策略</el-menu-item>
      </el-submenu>
    </el-submenu>
  </el-menu>
</el-aside>

<el-container>
  <el-header style="text-align: left; font-size: 16px">
    <el-dropdown @command="handleCommand">
      <i class="el-icon-more" style="margin-right: 20px"></i>
      <el-dropdown-menu slot="dropdown">
        <el-dropdown-item command="home">返回主页</el-dropdown-item>
        <el-dropdown-item command="logout">退出登录</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <span>{{ this.user.user }}</span>
    <span>，欢迎使用 GooseGains 量化交易平台</span>
    <el-button @click="refresh()" style="margin-left: 440px" size="medium">刷新获得实时数据</el-button>
    
  </el-header>
  
  <el-main style="position: relative; background-image: url('https://tse2-mm.cn.bing.net/th/id/OIP-C.z0pyMS3Ek3ggzNiOIaZBxgHaDt?w=315&h=175&c=7&r=0&o=5&dpr=1.5&pid=1.7'); background-size: cover; background-position: center; background-color: rgba(255, 255, 255, 0.6); padding: 20px;">
    <el-table :data="tableData" border style="width: 100%">
      <el-table-column fixed prop="stock_code" label="股票代码" width="110"></el-table-column>
      <el-table-column prop="stock_name" label="股票名称" width="110"></el-table-column>
      <el-table-column prop="stock_date" label="数据来源日期" width="110"></el-table-column>
      <el-table-column prop="stock_time" label="来源时间" width="110"></el-table-column>
      <el-table-column prop="open_price" label="当日开盘价" width="100"></el-table-column>
      <el-table-column prop="close_price" label="昨日收盘价" width="100"></el-table-column>
      <el-table-column prop="cur_price" label="最新价格" width="100"></el-table-column>
      <el-table-column prop="high_price" label="最高价" width="100"></el-table-column>
      <el-table-column prop="low_price" label="最低价" width="100"></el-table-column>
      <el-table-column prop="trade_volume" label="成交量（股）" width="125"></el-table-column>
      <el-table-column prop="trade_amount" label="成交金额" width="125"></el-table-column>
      <el-table-column fixed="right" label="操作" width="100">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" size="small">历史数据</el-button>
        </template>
      </el-table-column>
    </el-table>
  </el-main>

</el-container>
</el-container>
</template>

<script>

export default{
name:"Stock2",
data() {
  
  return {
    user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
    tableData:[]
  }
},
mounted(){
    console.log("渲染")
    console.log(this.tableData)
    this.request.post("getstock2").then(res => {
      this.tableData = res.stock;
      console.log(res.stock)
      console.log(this.tableData)
      })
  },
methods: {
  

  handleCommand(command) {
      if (command==='logout'){
        this.$router.push('/login');
      }
      if (command==='home'){
        this.$router.push('/home')
      }
        
    },
    handleClick(stockdata){
      console.log(stockdata)
      localStorage.setItem("stock", JSON.stringify(stockdata))  // 存储股票信息到浏览器
      this.$router.push('/kline2')
    },
    refresh(){
      this.request.post("getstock2").then(res => {
      this.tableData = res.stock;
      console.log(res.stock)
      console.log(this.tableData)
      })
      this.$router.push('/stock2')
    }
    
    
  }
}
</script>
<style>
.el-header {
background-color: rgb(55, 128, 224,0.4);
color: #333;
line-height: 60px;
}

.el-aside {
  color: #333;
}

.current-page {
  background-color: rgb(55, 128, 224);
  color: white; /* 设置文本颜色，以增加可读性 */
}
</style>