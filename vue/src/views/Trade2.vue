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
          <el-menu-item index="/trade2" class="current-page">卖出股票</el-menu-item>
        
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
  <div style="margin: 80px auto; background-color: rgb(55, 128, 224,0.2); width: 500px; height: 500px; padding: 20px; border-radius: 10px">
  <div style="margin: 20px 0; text-align: center; font-size: 24px"><b>卖出股票</b></div>
  <el-form :model="stock" :rules="rules" ref="stockForm">
    <el-form-item label="股票代码" label-position="left">
<template #label>
  <span style="margin-left: 10px;">股票代码</span>
</template>
<el-input placeholder="请输入要卖出的股票代码" size="medium" prefix-icon="el-icon-s-marketing" v-model="stock.sell_code"></el-input>
</el-form-item>

<el-form-item label="卖出数量" label-position="left">
<template #label>
  <span style="margin-left: 10px;">卖出数量</span>
</template>
<el-input placeholder="请输入要卖出的数量" size="medium" prefix-icon="el-icon-shopping-cart-2" v-model="stock.sell_number"></el-input>
</el-form-item>

<el-form-item label="当前价格" label-position="left">
<template #label>
  <span style="margin-left: 10px;">当前价格</span>
</template>
<el-input placeholder="每股当前价格" size="medium" prefix-icon="el-icon-coin" v-model="stock.sell_price"></el-input>
<!-- 这里还不大对，怎么修改？让这个当前价格能自动显示在表格这边 -->
</el-form-item>

<el-form-item label="该笔收入" label-position="left">
<template #label>
  <span style="margin-left: 10px;">该笔支出</span>
</template>
<el-input placeholder="该笔交易收入为" size="medium" prefix-icon="el-icon-s-data" v-model="stock.total_in"></el-input>
<!-- 这里还不大对，怎么修改？让这个支出自己算出来显示在表格这边 -->
</el-form-item>

<el-form-item style="margin: 5px 0; text-align: right">
<el-button type="primary" size="small" autocomplete="off" @click="sell">确定</el-button>
</el-form-item>


  </el-form>
</div>
</el-main>
</el-container>
</el-container>
</template>


<script>
import axios from 'axios';

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
  watch: {
  'stock.sell_code': function(newVal, oldVal) {
    // 在股票代码发生变化时触发
    // 可在此处编写获取当前价格的逻辑，例如发送 HTTP 请求到后端
    // 假设你有一个名为 getStockPrice 的方法用来获取股票价格和花了多少钱
    this.getStockPrice(newVal);
  }
},
getStockPrice(stockCode) {
  // 发送 HTTP POST 请求到后端，传递当前用户ID、买入的数据量和当前选中股票的代码
  axios.post('http://127.0.0.1:5001/trade2', {
    id_num: this.userId, // 假设 this.userId 是当前用户的ID
    amount_out: this.sell_number, // 假设 this.buyAmount 是买入的数据量
    stock_code: this.sell_code // 传递当前选中股票的代码
  })
    .then(response => {
      // 成功获取到股票价格和总花费
      this.stock.sell_price = response.data.datas[0]; // 第一个元素是当前股票价格
      this.total_in = response.data.datas[1]; // 第二个元素是总花费
    })
    .catch(error => {
      console.error('获取股票价格失败：', error);
    });
},
sell() {
  this.$refs['stockForm'].validate((valid) => {
      if (valid) {  // 表单校验合法
              // 构造发送到后端的数据对象
              const data = {
                  user: localStorage.getItem('user'),
                  stock_code: this.stock.sell_code,
                  amount_out: this.stock.sell_number
              };
              // 发送POST请求到后端API端点
              axios.post('http://127.0.0.1:5001/transaction_out', data)
                  .then(response => {
                      // 处理成功响应
                      
                      const aaa = response.data.data["aaa"]
                      const cur_price = response.data.data["cur_price"]
                      this.$message.success("卖出股票成功，当前价格为："+cur_price);
                      // this.$message.success("买入股票成功");
                      this.$router.push("/Property");
                      return true;
                  })
                  .catch(error => {
                      // 处理错误响应
                      console.error('Error:', error);
                      this.$message.error("卖出股票失败，请稍后重试");
                      return false;
                  });
          
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