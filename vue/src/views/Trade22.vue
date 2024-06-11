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
          <el-menu-item index="/stock2">深交所</el-menu-item>
  
        </el-menu-item-group>
        
      </el-submenu>
      <el-submenu index="3">
        <template slot="title"><i class="el-icon-setting"></i>量化交易</template>
        
          <el-menu-item index="/trade1">买入股票</el-menu-item>
          <el-menu-item index="/trade2"  class="current-page">卖出股票</el-menu-item>
        
        <el-submenu index="3-2">
          <template slot="title">交易策略</template>
          <el-menu-item index="/strategy1">策略1</el-menu-item>
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
          <el-dropdown-item command="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>{{ this.user.user }}</span>
      <span>，欢迎使用 GooseGains 量化交易平台</span>
      
    </el-header>
  
  
  <el-main>
    <div style="display: flex; align-items: center;">
        <div style="margin: 150px 0px 110px 260px; background-color: rgb(55, 128, 224,0.2); width: 700px; height: 500px; padding: 20px; border-radius: 15px;">
            <div style="margin: 20px 0; margin-bottom: 30px; text-align: center; font-size: 35px;"><b>卖出股票</b></div>            
            <el-button disabled class="extra-large-tag_price">当前股票价格：{{ price }}</el-button>
            <br><br>
            <el-button disabled class="extra-large-tag_num">计划卖出手数：{{ number }}(实际为
              {{ number*100 }}支)</el-button>
            <br><br>
            <el-button disabled class="extra-large-trade_totalcost">当前该笔收入：{{ number*100*price }}</el-button>
            <br><br><br>
            <el-button  @click="Click_property()" class="yes_or_no"type="primary" round>确认交易</el-button> <el-button @click="Click_home()"class="yes_or_no"  type="primary" round>取消交易</el-button>
            <!--取消交易可以跳回主页-->
            <!--确认交易可以跳回财产页面-->
        </div></div>
    </el-main>
  
  
  
  </el-container>
    </el-container>
  </template>
  
  <script>
  export default{
  name:"Trade22",
  data() {
    return {
        user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},//当前用户
        price: localStorage.getItem("price") ? JSON.parse(localStorage.getItem("price")) : {},//当前股票价格
        number:localStorage.getItem("number") ? JSON.parse(localStorage.getItem("number")) : {},//当前计划卖出手数
    };
    
  },
  mounted() {
    const storedUser = localStor
    
    age.getItem("user");
    if (storedUser) {
      // 如果存在存储的用户信息，则解析并更新 user 数据
      this.user = JSON.parse(storedUser);
      console.log("用户信息：", this.user)
    }
  },
  methods: {
      Click_property()//如果点确定交易，
      {
        console.log("成功交易，可看目前的财产情况")
        this.$router.push('/property')
      },
      Click_home()//如果点取消交易，
      {
        console.log("取消交易，返回主页")
        this.$router.push('/home')
      },
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
    background-color: #8694a7;
    color: #333;
    line-height: 60px;
  }
  
  .el-aside {
    color: #333;
  }
  .extra-large-tag_price {
    font-size: 20px; /* 调整字体大小 */
  padding: 23px 30px; /* 调整内边距 */
  text-align: center; /* 让文字居中 */
  margin-left: 210px; /* 调整左侧边距 */
  display: inline-block; /* 使元素变成行内块元素 */
  background-color: #ffffff; /* 设置背景颜色为白色 */
  min-width: 200px; /* 设置最小宽度 */
  border-radius: 10px; /* 设置圆角 */
}
.extra-large-tag_num {
    font-size: 20px; /* 调整字体大小 */
  padding: 23px 30px; /* 调整内边距 */
  text-align: center; /* 让文字居中 */
  margin-left: 161px; /* 调整左侧边距 */
  display: inline-block; /* 使元素变成行内块元素 */
  background-color: #ffffff; /* 设置背景颜色为白色 */
  min-width: 200px; /* 设置最小宽度 */
  border-radius: 10px; /* 设置圆角 */
}

.extra-large-trade_totalcost {
  font-size: 20px; /* 调整字体大小 */
  padding: 23px 30px; /* 调整内边距 */
  text-align: center; /* 让文字居中 */
  margin-left: 210px; /* 调整左侧边距 */
  display: inline-block; /* 使元素变成行内块元素 */
  background-color: #ffffff; /* 设置背景颜色为白色 */
  min-width: 200px; /* 设置最小宽度 */
  border-radius: 10px; /* 设置圆角 */
}
.yes_or_no{
font-size: 24px; /* 调整字体大小 */
  padding: 120px 120px; /* 调整内边距 */
  text-align: center; /* 让文字居中 */
  margin-left: 196px; /* 调整左侧边距 */
}
  </style>