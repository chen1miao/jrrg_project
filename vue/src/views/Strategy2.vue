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
          <el-menu-item index="/strategy1">双均线策略</el-menu-item>
          <el-menu-item index="/strategy2" class="current-page" >均值回归交易策略</el-menu-item>
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
  <div style="position: relative;">
    <!-- 调整黑框位置 -->
    <div style="position: absolute; top: 60px; left: 20px; width: calc(100% - 40px); padding: 20px; background-color: rgba(0, 0, 0, 0.5); border-radius: 10px;">
      <!-- 添加标题 -->
       <br>
      <h1 style="color: white; font-size: 27px; margin-top:0px;margin-bottom: 10px;">策略二：均值回归交易策略</h1>
      <!-- 添加文字内容 -->
       
      <div style="color: white; line-height: 1.8;">
        <p style="font-weight: bold;font-size: 20px;">均值回归交易策略-原理介绍：</p>

<div style="background-color: rgba(0, 0, 0, 0.5); margin-top:10px;padding: 10px;border-radius: 10px;">
  <p style="text-indent:15px;font-size: 18px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color: white;">均值回归：股票价格无论高于或低于价值中枢(或均值)都会以很高的概率向价值中枢回归的趋势。</p>
</div>

<p style="font-size: 18px;font-weight: bold;margin-top:20px;">本策略将计算偏离均值最低的一支推荐买入，最高的一支推荐卖出。</p>
<p style="font-size: 24px;font-weight: bold;margin-top:16px;">以下是本策略所推荐的买卖股票情况：</p>
<div style="background-color: rgba(0, 0, 0, 25); margin-top:10px;padding: 10px;border-radius: 10px;">
<p style="font-size: 18px;font-weight: bold;margin-top:2px;">根据本策略的分析，我们目前推荐买入的股票为 {{ buy_name }}</p>
<p style="font-size: 18px;font-weight: bold;margin-top:20px;">根据本策略的分析，我们目前推荐卖出的股票为 {{ sell_name }}</p></div>
    </div>
  </div>
</div>
</el-main>
</el-container>
</el-container>
</template>

<script>
export default{
name:"Strategy2",
data() {
  return {
    user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
    buy_name:'',//推荐买的
    sell_name:''//推荐卖的
  }
},
mounted(){
  this.request.post("strategy2").then(res => {
      this.buy_name=res.data.buy_name
      this.sell_name=res.data.sell_name
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