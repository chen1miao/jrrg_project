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
          <el-menu-item index="/stock1" class="current-page">上交所</el-menu-item>
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
      <el-button @click="return_to_stock()" style="margin-left: 440px" size="medium">返回</el-button>
      
    </el-header>
    
    <el-main style="background-color: rgb(210, 212, 217)">
      <img :src="this.img_path" alt="" style="width: 960px; height: 500px;">
    </el-main>
  </el-container>
  </el-container>
  </template>
  
  <script>
  export default{
  name:"Kline1",
  data() {
    return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
      stock: localStorage.getItem("stock") ? JSON.parse(localStorage.getItem("stock")) : {},
      img_path:''
    }
  },

  mounted(){
    console.log(this.stock.stock_code)
    
    if (this.stock.stock_code==='600000.SH'){
      this.img_path=require('../assets/600000_sh.png');
    }
    if (this.stock.stock_code==='600004.SH'){
      this.img_path=require('../assets/600004_sh.png');
    }
    if (this.stock.stock_code==='600007.SH'){
      this.img_path=require('../assets/600007_sh.png');
    }
    if (this.stock.stock_code==='600031.SH'){
      this.img_path=require('../assets/600031_sh.png');
    }
    if (this.stock.stock_code==='600056.SH'){
      this.img_path=require('../assets/600056_sh.png');
    }
    if (this.stock.stock_code==='600064.SH'){
      this.img_path=require('../assets/600064_sh.png');
    }
    if (this.stock.stock_code==='600089.SH'){
      this.img_path=require('../assets/600089_sh.png');
    }
    if (this.stock.stock_code==='688046.SH'){
      this.img_path=require('../assets/688046_sh.png');
    }
    if (this.stock.stock_code==='688113.SH'){
      this.img_path=require('../assets/688113_sh.png');
    }
    if (this.stock.stock_code==='688131.SH'){
      this.img_path=require('../assets/688131_sh.png');
    }
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
      return_to_stock(){
        this.$router.push('/stock1')
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