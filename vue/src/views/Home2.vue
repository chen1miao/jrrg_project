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
        <el-dropdown-item command="logout">退出登录</el-dropdown-item>
      </el-dropdown-menu>
    </el-dropdown>
    <span>{{ this.user.user }}</span>
    <span>，欢迎使用 GooseGains 量化交易平台</span>
    
  </el-header>



  <el-main style="position: relative; background-image: url('https://cdn.pixabay.com/photo/2017/03/29/23/16/steel-2186813_1280.jpg'); background-size: cover; background-position: center; background-color: rgba(255, 255, 255, 0.6); padding: 20px;">
    <div style="position: relative;">
      <!-- 调整黑框位置 -->
      <div style="position: absolute; top: 5px; left: 20px; width: calc(100% - 40px); padding: 20px; background-color: rgba(0, 0, 0, 0.5); border-radius: 10px;">
        <!-- 添加标题 -->
        <h1 style="color: white; font-size: 30px; margin-top:5px;margin-bottom: 10px;">关于 GooseGains</h1>
        <!-- 添加文字内容 -->
         
        <div style="color: white; line-height: 1.8;">
          <p style="font-size: 23px;font-weight: bold;">欢迎来到量化交易平台 GooseGains ！当前版本为1.0.</p>
         
          <p style="font-weight: bold;font-size: 20px;">我们的导航页包括了三个主要部分：</p>

<div style="background-color: rgba(0, 0, 0, 0.5); margin-top:10px;padding: 10px;">
    <p style="text-indent:20px;font-size: 18px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); color: white;">1.个人信息：在这里，您可以轻松访问和管理您的个人资料、账户设置和偏好设定。我们致力于为您提供最佳的个性化体验，确保您能够充分利用我们的平台功能。</p>
</div>
<div style="background-color: rgba(0, 0, 0, 0.5); padding: 10px;">
<p style="text-indent:20px;font-size: 18px; text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);">2.市场数据： GooseGains 提供最全面的市场数据服务。我们涵盖了上交所和深交所上千支股票的当日数据，以及上交所和深交所各10支股票的当日和历史数据。不论您是初学者还是专业人士，我们的市场数据都能满足您的需求，助您做出明智的投资决策。</p>
</div>

<div style="background-color: rgba(0, 0, 0, 0.5); padding: 10px;">
<p style="text-indent:20px;font-size: 18px;">3.量化交易：在 GooseGains ，我们致力于提供最先进的量化交易工具和策略。我们的平台结合了最新的技术和深度分析，帮助您实现自动化交易执行，降低风险并最大化收益。无论您是寻求长期投资还是短期交易，我们都能为您提供量身定制的解决方案。</p>
</div>
<p style="font-size: 18px;margin-top:20px;">在市场数据部分，我们采用了多种策略，以确保您获取到最准确、最及时的数据。我们的数据团队精心筛选和整理了上交所和深交所的大量股票数据，包括当日交易数据和历史数据。我们还提供了多种数据分析工具，帮助您更好地理解市场走势和趋势。

无论您是新手投资者还是资深交易员， GooseGains 都能为您提供所需的市场数据和量化交易工具，助您实现投资目标并取得成功！</p>
      </div>
    </div>
  </div>
  </el-main>



</el-container>
  </el-container>
</template>

<script>
export default{
name:"Home2",
data() {
  return {
    user: {}, // 初始化为空对象
  };
},
mounted() {
  const storedUser = localStorage.getItem("user");
  if (storedUser) {
    // 如果存在存储的用户信息，则解析并更新 user 数据
    this.user = JSON.parse(storedUser);
    console.log("用户信息：", this.user)
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
  background-color: #8694a7;
  color: #333;
  line-height: 60px;
}

.el-aside {
  color: #333;
}
</style>