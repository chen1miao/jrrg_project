<template>
    <el-container style="height: 800px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu router :default-openeds="['1','2','3', '3-2']" :default-active="this.$router.path">
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
          <el-menu-item index="/stock2">深交所</el-menu-item>
        </el-menu-item-group>
          
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>量化交易</template>
          
          <el-menu-item index="/trade1">买入股票</el-menu-item>
          <el-menu-item index="/trade2">卖出股票</el-menu-item>
          
          <el-submenu index="3-2">
            <template slot="title">交易策略</template>
            <el-menu-item index="/strategy1" class="current-page" >策略1</el-menu-item>
            <el-menu-item index="/strategy2">策略2</el-menu-item>
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
    
    <el-main style="background-color: white">
        <div v-if="back_name === '600000.sh'">
                当前回测股票收益率：20.43%
        </div>
        <div v-else-if="back_name === '600004.sh'">
            当前回测股票收益率：1.00%
        </div>
        <div v-else-if="back_name === '600007.sh'">
            当前回测股票收益率：21.66%
        </div>
        <div v-else-if="back_name === '600031.sh'">
            当前回测股票收益率：-10.93%
        </div>
        <div v-else-if="back_name === '600056.sh'">
            当前回测股票收益率：-9.19%
        </div>
        <div v-else-if="back_name === '600064.sh'">
            当前回测股票收益率：11.59%
        </div>
        <div v-else-if="back_name === '600089.sh'">
            当前回测股票收益率：0.98%
        </div>
        <div v-else-if="back_name === '688046.sh'">
            当前回测股票收益率：0.62%
        </div>
        <div v-else-if="back_name === '688113.sh'">
            当前回测股票收益率：-38.16%
        </div>
        <div v-else-if="back_name === '688131.sh'">
            当前回测股票收益率：-23.12%
        </div>
        <br>
        <img :src="this.img_path" alt="" style="width: 850px; height: 636px;margin-left:70px;">
      </el-main>
  </el-container>
  </el-container>
  </template>
  
  <script>
  export default{
  name:"Strategy_show1",
  data() {
    return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
      img_path:'',
      back_name:localStorage.getItem("name") ? JSON.parse(localStorage.getItem("name")) : {},//当前想要看回测股票
      
    }
  },
  mounted(){
      console.log(this.back_name)
      if (this.back_name==='600000.sh'){
        this.img_path=require('../assets/600000_sh_b.png');
      }
      if (this.back_name==='600004.sh'){
        this.img_path=require('../assets/600004_sh_b.png');
      }
      if (this.back_name==='600007.sh'){
        this.img_path=require('../assets/600007_sh_b.png');
      }
      if (this.back_name==='600031.sh'){
        this.img_path=require('../assets/600031_sh_b.png');
      }
      if (this.back_name==='600056.sh'){
        this.img_path=require('../assets/600056_sh_b.png');
      }
      if (this.back_name==='600064.sh'){
        this.img_path=require('../assets/600064_sh_b.png');
      }
      if (this.back_name==='600089.sh'){
        this.img_path=require('../assets/600089_sh_b.png');
      }
      if (this.back_name==='688046.sh'){
        this.img_path=require('../assets/688046_sh_b.png');
      }
      if (this.back_name==='688113.sh'){
        this.img_path=require('../assets/688113_sh_b.png');
      }
      if (this.back_name==='688131.sh'){
        this.img_path=require('../assets/688131_sh_b.png');
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