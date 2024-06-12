<template>
    <el-container style="height: 800px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu router :default-openeds="['1','2','3']" :default-active="this.$router.path">
      <el-submenu index="1">
        <template slot="title"><i class="el-icon-message"></i>个人信息</template>
        <el-menu-item-group>
          <el-menu-item index="/changepassword">修改密码</el-menu-item>
          <el-menu-item index="/property" class="current-page">当前资产</el-menu-item>
       
        </el-menu-item-group>
        
      </el-submenu>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-menu"></i>市场数据</template>
        <el-menu-item-group>
          <el-menu-item index="/today">今日大盘</el-menu-item>
          <el-menu-item index="/stock1">上交所</el-menu-item>
          <el-menu-item index="/stock2">深交所</el-menu-item>
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
      
    </el-header>
    
    <el-main style="position: relative; background-image: url('https://tse2-mm.cn.bing.net/th/id/OIP-C.z0pyMS3Ek3ggzNiOIaZBxgHaDt?w=315&h=175&c=7&r=0&o=5&dpr=1.5&pid=1.7'); background-size: cover; background-position: center; background-color: rgba(255, 255, 255, 0.6); padding: 20px;">
      <h3>当前现金：{{ this.cash }}</h3>
      <br><p>买入股票记录</p><br>
      <el-table :data="tableData1"  height="160" border style="width: 100%">
        <el-table-column fixed prop="stock_code" label="股票代码" width="191"></el-table-column>
        <el-table-column prop="date" label="交易日期" width="191"></el-table-column>
        <el-table-column prop="price" label="当时价格" width="191"></el-table-column>
        <el-table-column prop="amount" label="交易量（股）" width="191"></el-table-column>
        <el-table-column prop="total" label="交易金额" width="190"></el-table-column>
      </el-table>
      <br><p>卖出股票记录</p><br>
      <el-table :data="tableData2"  height="160" border style="width: 100%">
        <el-table-column fixed prop="stock_code" label="股票代码" width="191"></el-table-column>
        <el-table-column prop="date" label="交易日期" width="191"></el-table-column>
        <el-table-column prop="price" label="当时价格" width="191"></el-table-column>
        <el-table-column prop="amount" label="交易量（股）" width="191"></el-table-column>
        <el-table-column prop="total" label="交易金额" width="190"></el-table-column>
      </el-table>
      <br><p>股票持有情况</p><br>
      <el-table :data="tableData3"  height="160" border style="width: 70%">
        <el-table-column fixed prop="stock_code" label="股票代码" width="223"></el-table-column>
        <el-table-column prop="amount" label="当前持有量（股）" width="223"></el-table-column>
        <el-table-column prop="price" label="当前价格" width="222"></el-table-column>
      </el-table>
    </el-main>
  </el-container>
  </el-container>
  </template>
  
  <script>
  export default{
  name:"Property",
  data() {
    return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
      cash:1,
      tableData1:[],
      tableData2:[],
      tableData3:[]
    }
  },
  mounted(){
    console.log(this.user)
    this.request.post("get_cash",this.user).then(res =>{
      console.log(res.cash)
      this.cash=res.cash
    })
    this.request.post("TransactionInDisplay", this.user).then(res => {
      console.log(res.stock_in)
      this.tableData1 = res.stock_in;
    })
    this.request.post("TransactionOutHistoryDisplay", this.user).then(res => {
      console.log(res.stock_out)
      this.tableData2 = res.stock_out;
    })
    this.request.post("HoldingsDisplay", this.user).then(res => {
      console.log(res.stock_hold)
      this.tableData3 = res.stock_hold
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