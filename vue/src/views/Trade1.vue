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
          
            <el-menu-item index="/trade" class="current-page" >买入股票</el-menu-item>
            <el-menu-item index="/trade2">卖出股票</el-menu-item>
          
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
          <el-dropdown-item command="home">返回主页</el-dropdown-item>
          <el-dropdown-item command="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>{{ this.user.user }}</span>
      <span>，欢迎使用 GooseGains 量化交易平台</span>
      
    </el-header>
    
    <el-main>
      <div style="margin: 80px auto; background-color: rgb(55, 128, 224,0.2); width: 350px; height: 360px; padding: 20px; border-radius: 10px">
      <div style="margin: 20px 0; text-align: center; font-size: 24px"><b>买入股票</b></div>
      <el-form :model="stock" :rules="rules" ref="stockForm">
        <el-form-item prop="buy_code">
          <el-input placeholder="请输入要买入的股票代码" size="medium" prefix-icon="el-icon-s-marketing"v-model="stock.buy_code"></el-input>
        </el-form-item>
        <el-form-item prop="buy_price">
          <el-input placeholder="每股当前价格为：" size="medium" prefix-icon="el-icon-coin"v-model="stock.buy_price"></el-input>
          <!--这里还不大对，怎么修改？让这个当前价格能自动显示在表格这边-->
        </el-form-item>
        <el-form-item prop="buy_number">
          <el-input placeholder="请输入要买入的数量" size="medium" prefix-icon="el-icon-shopping-cart-2" v-model="stock.buy_number"></el-input>
        </el-form-item>
        <el-form-item prop="total_cost">
          <el-input placeholder="该笔交易支出为：" size="medium" prefix-icon="el-icon-s-data" v-model="stock.total_cost"></el-input>
          <!--这里还不大对，怎么修改？让这个支出自己算出来显示在表格这边-->
        </el-form-item>
        <el-form-item style="margin: 5px 0; text-align: right">
          <el-button type="primary" size="small"  autocomplete="off" @click="buy">确定</el-button>
        </el-form-item>
      </el-form>
    </div>
    </el-main>
  </el-container>
  </el-container>
  </template>
  
  <script>
  export default{
  name:"Trade",
  data() {
    return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
      stock: {},
      rules: {
        
      }
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
    buy() {
      this.$refs['stockForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          if (this.stock.buy_code!=='1') {
            this.$message.error("您输入的股票代码不存在")
            return false
          }
          else if(this.stock.buy_number !== '100' ){ // else if(this.stock.total_cost < this.user.cash){
            this.$message.error("您的资金不足")
            return false
          }
          else{
            this.$message.success("买入股票成功")
            this.$router.push("/Property")
            return true
          }
        }
      });
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