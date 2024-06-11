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
  <div style="display: flex; align-items: center;">
        <div style="margin: 150px 0px 110px 260px; background-color: rgb(55, 128, 224,0.2); width: 400px; height: 300px; padding: 20px; border-radius: 15px;">
            <div style="margin: 20px 0; margin-bottom: 30px; text-align: center; font-size: 24px;"><b>卖出股票</b></div>            
            <el-form :model="stock" :rules="rules" ref="stockForm">
                <el-form-item prop="code">
                    <el-input placeholder="请输入要卖出的股票代码" size="medium" prefix-icon="el-icon-goods" v-model="stock.code"></el-input>
                </el-form-item>
                <el-form-item prop="sell_number">
                    <el-input placeholder="请输入要卖出的数量（单位为手）" size="medium" prefix-icon="el-icon-s-marketing" v-model="stock.sell_number"></el-input>
                </el-form-item>
                
                <el-form-item style="margin: 35px 10px; text-align: right">
                  <el-button type="primary" size="small" autocomplete="off" @click="getStockPrice_curprice">查询</el-button>
                </el-form-item>
            </el-form>
        </div>



</div>
</el-main>
</el-container>
</el-container>
</template>


<script>
 import axios from 'axios';
export default{
name:"Trade2",
data() {
  return {
    user: localStorage.getItem("user") ? JSON.parse(localStorage.getItem("user")) : {},
    // a: localStorage.getItem("number") ? JSON.parse(localStorage.getItem("number")) : {},
    sell_price:'',
    stock:{},
    rules: {
      code: [
          { required: true, message: '请输入要卖出的股票代码', trigger: 'blur' }
        ],
        sell_number: [
          { required: true, message: '请输入要卖出的数量(单位为手)', trigger: 'blur' }
        ],
    }
    
  }
},
methods: 
{
getStockPrice_curprice() {
  
  this.$refs['stockForm'].validate((valid) => {
        if (valid) {  // 表单校验合法
          console.log(this.stock)
          if(this.stock.code!=='600000.SH'&&this.stock.code!=='600004.SH'&&this.stock.code!=='600007.SH'&&this.stock.code!=='600056.SH'&&this.stock.code!=='600064.SH'&&this.stock.code!=='600031.SH'&&this.stock.code!=='600089.SH'&&this.stock.code!=='688046.SH'&&this.stock.code!=='688113.SH'&&this.stock.code!=='688131.SH'&&this.stock.code!=='000001.SZ'&&this.stock.code!=='000002.SZ'&&this.stock.code!=='000008.SZ'&&this.stock.code!=='000009.SZ'&&this.stock.code!=='000019.SZ'&&this.stock.code!=='000027.SZ'&&this.stock.code!=='000028.SZ'&&this.stock.code!=='000069.SZ'&&this.stock.code!=='000155.SZ'&&this.stock.code!=='000428.SZ'){
            this.$message.error("您输入的股票代码不存在")
            return
          }
          
          //if(this.stock.code!=='600000.SH')||this.stock.code!=='600004.SH'||this.stock.code!=='600007.SH'||this.stock.code!=='600056.SH'||this.stock.code!=='600064.SH'||this.stock.code!=='600031.SH'||this.stock.code!=='600089.SH'||this.stock.code!=='688046.SH'||this.stock.code!=='688113.SH'||this.stock.code!=='688131.SH'||this.stock.code!=='000001.SZ'||this.stock.code!=='000002.SZ'||this.stock.code!=='000008.SZ'||this.stock.code!=='000009.SZ'||this.stock.code!=='000019.SZ'||this.stock.code!=='000027.SZ'||this.stock.code!=='000028.SZ'||this.stock.code!=='000069.SZ'||this.stock.code!=='000155.SZ'||this.stock.code!=='000428.SZ'
          else
          {
          this.request.post("get_cur_price", this.stock).then(res => {
            console.log(this.stock)
            console.log(res.cur_price)
            this.stock.sell_price=res.cur_price
            localStorage.setItem("price", JSON.stringify(res.cur_price)) 
            localStorage.setItem("number", JSON.stringify(this.stock.sell_number)) 
            
            this.$router.push('/trade22')
            this.$message.success("查询成功")
          })
        }
        }
      });
  
},
sell() {
  console.log("sell")
  /*this.$refs['stockForm'].validate((valid) => {
      if (valid) {  // 表单校验合法
          if(this.stock.total_cost < this.user.cash) { 
              this.$message.error("您的资金不足");
              return false;
          } else {
              // 构造发送到后端的数据对象
              const data = {
                  name: this.user,
                  stock_code: this.stock.code,
                  amount_in: this.stock.buy_number
              };
              console.log(data)
              // 发送POST请求到后端API端点
              axios.post('http://127.0.0.1:5001/transaction_in', data)
                  .then(response => {
                      // 处理成功响应
                      this.$message.success("买入股票成功");
                      this.$router.push("/Property");
                      return true;
                  })
                  .catch(error => {
                      // 处理错误响应
                      console.error('Error:', error);
                      this.$message.error("买入股票失败，请稍后重试");
                      return false;
                  });
          }
      }
  });*/
},
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