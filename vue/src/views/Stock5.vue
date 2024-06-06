<template>
    <el-container style="height: 800px; border: 1px solid #eee">
  <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu router :default-openeds="['2']" :default-active="this.$router.path">
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
          
          <el-menu-item index="/stock1">选项1</el-menu-item>
            <el-menu-item index="/stock2">选项2</el-menu-item>
            <el-menu-item index="/stock3">选项3</el-menu-item>
            <el-menu-item index="/stock4">选项4</el-menu-item>
            <el-menu-item index="/stock5" class="current-page" >选项5</el-menu-item>
            <el-menu-item index="/stock6">选项6</el-menu-item>
            <el-menu-item index="/stock7">选项7</el-menu-item>
            <el-menu-item index="/stock8">选项8</el-menu-item>
            <el-menu-item index="/stock9">选项9</el-menu-item>
            <el-menu-item index="/stock10">选项10</el-menu-item>
  
          </el-menu-item-group>
          
        </el-submenu>
        <el-submenu index="3">
          <template slot="title"><i class="el-icon-setting"></i>量化交易</template>
          
            <el-menu-item index="/trade">买入卖出</el-menu-item>
          
          <el-submenu index="3-2">
            <template slot="title">交易策略</template>
            <el-menu-item index="/strategy1">策略1</el-menu-item>
            <el-menu-item index="/strategy2">策略2</el-menu-item>
        </el-submenu>
      </el-submenu>
    </el-menu>
  </el-aside>
  
  <el-container>
    <el-header style="text-align: right; font-size: 12px">
      <el-dropdown @command="handleCommand">
        <i class="el-icon-setting" style="margin-right: 15px"></i>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="logout">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
      <span>{{ user.username }}</span>
    </el-header>
    
    <el-main>
      <p>股票5</p>
    </el-main>
  </el-container>
  </el-container>
  </template>
  
  <script>
  export default{
  name:"Stock5",
  data() {
    return {
      user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
    }
  },
  methods: {
      handleCommand(command) {
        this.$router.push('/login')
      }
    }
  }
  </script>
  <style>
  .el-header {
    background-color: #B3C0D1;
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